from ib_insync import *
from brokers.interactive_brokers.database import Scraped, Fundamentals, Historical
from brokers.interactive_brokers.scraper import scrape_ib
from brokers.interactive_brokers.config import db_host, db_user, db_password, db_name, db_port
import schedule
from sqlalchemy import create_engine 
import pandas as pd

def historical(symbols: list) -> None:
	ib = IB()
	ib.connect("134.209.160.105", 7496, clientId=100)
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

def fundamentals(symbols: list) -> None:
	ib = IB()
	ib.connect("134.209.160.105", 7496, clientId=100)
	print(f'Fetching fundamental information for {len(symbols)} symbols.')
	for index, symbol in enumerate(symbols):
		print(f"{symbol} {index+1}/{len(symbols)}")
		contract = Stock(symbol, 'SMART', 'USD')
		ticker = ib.reqMktData(contract, '258')
		ib.sleep(2)


def import_csv(file_name):
	df = pd.read_csv(file_name,sep=',')
	engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}").connect()
	df['hasGaps'] = False
	df.to_sql(name='historical', con=engine, if_exists='append',index=False)


def recurrent_action():
    scrape_ib()
    scraped_symbols = [record.symbol for record in Scraped.select()]
    historical(scraped_symbols)

if __name__ == '__main__':
	recurrent_action()