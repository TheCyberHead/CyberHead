from ib.opt import ibConnection, message, Connection
from time import sleep, strftime
from brokers.interactive_brokers.interactive import makeStkContract
from brokers.interactive_brokers.database import Historical, Scraped
from brokers.interactive_brokers.config import historical_from, bar_length
from datetime import datetime
from brokers.interactive_brokers.config import ib_host, ib_port, ib_client_id

# Source https://interactivebrokers.github.io/tws-api/historical_bars.html

tickerStore = {}

def historical_handler(msg):
    if not "finished" in msg.date:
        print('{} / Open: {}  Close: {}'.format(tickerStore[msg.reqId],msg.open, msg.close))
        checkRecord = Historical.select().where(Historical.date_history==date_f).where(Historical.ticker==tickerStore[msg.reqId])
        if not checkRecord.exists():
            print('Inserting {} at {}'.format(tickerStore[msg.reqId],date_f))
            Historical.create(
                    ticker=tickerStore[msg.reqId],
                    open_price=msg.open,
                    high=msg.high,
                    low=msg.low,
                    closing_price=msg.close,
                    date_history=date_f,
                    hasGaps=msg.hasGaps
                )
        else:
            print('Existing record for {} at {}'.format(tickerStore[msg.reqId],date_f))

def load_scraped_symbols():
    query = Scraped.select()
    return [(record.id, record.symbol) for record in query]

def watcher(msg):
    print("IB Watch : {}".format(msg))

def historical_request(tickerId: int, tickerSymbol: str) -> None:
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
    sleep(5)
    con.disconnect()
    sleep(2)

def collect(symbols: list) -> None:
    for symbol in load_scraped_symbols():
        historical_request(symbol[0],symbol[1])

def recurrent_action():
    scraped_symbols = load_scraped_symbols()
    collect(scraped_symbols)

if __name__ == '__main__':
    recurrent_action()
