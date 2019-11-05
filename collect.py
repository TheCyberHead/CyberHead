from datetime import datetime, timedelta, date
from ib.ext.Contract import Contract
from ib.opt import ibConnection, message
from time import sleep, strftime
from brokers.interactive_brokers.database import Scraped, Fundamentals, Historical
from brokers.interactive_brokers.interactive import makeContract, makeStkContract
from brokers.interactive_brokers.config import historical_from, bar_length, ib_host, ib_port, ib_client_id 
from brokers.interactive_brokers.scraper import scrape_ib
import schedule
import time

tickersId = {}
tickerStore = {}

def watcher(msg):
    print(msg)


def historical_handler(msg):
    if not "finished" in msg.date:
        date_f = datetime.strptime(msg.date, '%Y%m%d').strftime('%Y-%m-%d')
        Historical.create(
                ticker=tickerStore[msg.reqId],
                open_price=msg.open,
                high=msg.high,
                low=msg.low,
                closing_price=msg.close,
                date_history=date_f,
                hasGaps=msg.hasGaps
            )

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

def load_scraped_symbols():
    query = Scraped.select()
    return [(record.symbol, record.exchange, record.id) for record in query]


def historical_request(tickerId: int, tickerSymbol: str, totalSymbols) -> None:
    print(f"{tickerSymbol} : {tickerId}/{totalSymbols}")
    contract = (tickerSymbol, 'STK', 'SMART', 'USD', '', 0.0, '')
    con = ibConnection(ib_host,port=ib_port, clientId=ib_client_id)
    con.registerAll(watcher)
    con.register(historical_handler, message.historicalData)
    con.connect()
    sleep(1)
    stkContract = makeStkContract(contract)
    con.reqMarketDataType(4)
    sleep(5)
    endtime = strftime('%Y%m%d %H:%M:%S')
    tickerStore[tickerId] = stkContract.m_symbol
    con.reqHistoricalData(tickerId,stkContract,endtime,historical_from,bar_length,"MIDPOINT",1,1)
    sleep(30)
    con.disconnect()
    sleep(2)

def collect(symbols: list) -> None:
    tws = ibConnection(ib_host,port=ib_port, clientId=ib_client_id)
    tws.registerAll(watcher)
    tws.register(tickPriceHandler, 'TickString')
    for symbol in symbols:
        tws.connect()
        ticker = symbol[0]
        print(ticker)
        stock_fundamental = {}
        tws.reqMktData(symbol[2], makeContract(ticker), "233, 236, 258", False)
        tickersId[symbol[2]] = [symbol[0],symbol[1]]
        sleep(5)
        tws.disconnect()

def recurrent_action():
    scrape_ib()
    scraped_symbols = load_scraped_symbols()
    for symbol in scraped_symbols:
        historical_request(symbol[2], symbol[0], len(scraped_symbols))
    collect(scraped_symbols)


if __name__ == '__main__':
    recurrent_action()
    schedule.every().monday.do(recurrent_action)
    while True:
        schedule.run_pending()
        time.sleep(1)