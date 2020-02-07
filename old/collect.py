from ib_insync import *
from database import Scraped, Fundamentals, Historical
from brokers.interactive_brokers.scraper import scrape_ib
from brokers.interactive_brokers.interactive import makeContract, makeStkContract
from random_tools.graphs.calc import generate
from random_tools.graphs.heatmap import generateMaps
from config import db_host, db_user, db_password, db_name, db_port
import schedule
from ib.ext.Contract import Contract
from ib.opt import ibConnection, message
from sqlalchemy import create_engine 
import pandas as pd
from config import historical_from, bar_length, ib_host, ib_port, ib_client_id 
import time
from datetime import datetime
import shutil

tickersId = {}
tickerStore = {}

def historical(symbols: list) -> None:
	ib = IB()
	ib.connect(ib_host, ib_port, clientId=ib_client_id)
	print(f'Fetching historical information for {len(symbols)} symbols.')
	for index, symbol in enumerate(symbols):
		try:
			print(f"{symbol} {index+1}/{len(symbols)}")
			contract = Stock(symbol, 'SMART', 'USD')
			historical_bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='1 Y',
			        barSizeSetting='1 day', whatToShow='MIDPOINT', useRTH=True)
			df = util.df(historical_bars)
			df['symbol'] = symbol
			df = df[['symbol','date', 'open', 'high', 'low', 'close']]
			if index == 0:
				df.to_csv("historical.csv", index=False)
			else:
				df.to_csv("historical.csv", mode='a', header=False, index=False)
		except Exception as e:
			print(f'Error while fetching {symbol}')

def load_scraped_symbols():
    query = Scraped.select().where(Scraped.id > 3500)
    return [(record.symbol, record.exchange, record.id) for record in query]

def tickPriceHandler(msg):
    fundamentals = str(msg).split('value=')[1].split(';')
    handler_dict = {}
    if msg.tickType == 47 and len(fundamentals) > 10:
        for val in fundamentals:
            try:
                data = val.split('=')
                if data != ['']:
                    handler_dict[data[0]] = data[1].replace('>','')
            except Exception as e:
                print(e)
                continue
        handler_dict['TICKER'] = tickersId[msg.tickerId][0]
        handler_dict['EXCHANGE'] = tickersId[msg.tickerId][1]
        handler_dict['DATE'] = datetime.now()
        Fundamentals.create(**handler_dict)
        print("Inserting fundamentals for {}".format(handler_dict['TICKER']))

def collect(symbols: list) -> None:
    tws = ibConnection(ib_host,port=ib_port, clientId=ib_client_id)
    tws.register(tickPriceHandler, 'TickString')
    for symbol in symbols:
        tws.connect()
        ticker = symbol[0]
        print(ticker)
        stock_fundamental = {}
        tws.reqMktData(symbol[2], makeContract(ticker), "233, 236, 258", False)
        tickersId[symbol[2]] = [symbol[0],symbol[1]]
        time.sleep(5)
        tws.disconnect()

def import_csv(file_name):
    engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}").connect()
    for df in pd.read_csv(file_name,sep=',', chunksize=500):
        df.columns = ['ticker','date_history','open_price','high','low','closing_price']
        df['hasGaps'] = False
        df.to_sql(name='historical', con=engine, if_exists='append',index=False)

def recurrent_action():
    scrape_ib()
    scraped_symbols = [record.symbol for record in Scraped.select()]
    historical(scraped_symbols)
    import_csv('historical.csv')
    time.sleep(35)
    sc_symbols = load_scraped_symbols()
    collect(sc_symbols)
    generate()
    generateMaps()

if __name__ == '__main__':
    recurrent_action()
    schedule.every().monday.do(recurrent_action)
    while True:
        schedule.run_pending()
        time.sleep(1)