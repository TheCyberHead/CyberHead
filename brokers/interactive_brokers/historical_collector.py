from ib.opt import ibConnection, message, Connection
from time import sleep, strftime
from brokers.interactive_brokers.interactive import makeStkContract
from brokers.interactive_brokers.database import Historical, Scraped
from datetime import datetime

# Source https://interactivebrokers.github.io/tws-api/historical_bars.html

tickerStore = {}

def historical_handler(msg):
    if not "finished" in msg.date:
        print('{} / Open: {}  Close: {}'.format(tickerStore[msg.reqId],msg.open, msg.close))
        Historical.create(
                ticker=tickerStore[msg.reqId],
                open_price=msg.open,
                high=msg.high,
                low=msg.low,
                closing_price=msg.close,
                date_history=datetime.strptime(msg.date, '%Y%m%d').strftime('%Y-%m-%d'),
                hasGaps=msg.hasGaps
            )

def load_scraped_symbols():
    query = Scraped.select()
    return [(record.id, record.symbol) for record in query]

def watcher(msg):
    print("IB Watch : {}".format(msg))

def historical_request(tickerId: int, tickerSymbol: str) -> None:
    contract = (tickerSymbol, 'STK', 'SMART', 'USD', '', 0.0, '')
    con = ibConnection("127.0.0.1",port=7496, clientId=100)
    con.registerAll(watcher)
    con.register(historical_handler, message.historicalData)
    con.connect()
    sleep(1)
    stkContract = makeStkContract(contract)
    con.reqMarketDataType(4)
    sleep(5)
    endtime = strftime('%Y%m%d %H:%M:%S')
    tickerStore[tickerId] = stkContract.m_symbol
    con.reqHistoricalData(tickerId,stkContract,endtime,"7 Y","1 day","MIDPOINT",1,1)
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
    # Note: Option quotes will give an error if they aren't shown in TWS
    # FORMAT ('GOOG', 'STK/FUT/FOP/CASH', 'SMART/GLOBEX/IDEALPRO', 'USD', '', 0.0, '')
    '''contractTuple = ('GOOG', 'STK', 'SMART', 'USD', '', 0.0, '')
    historical_request(21,contractTuple)'''
    recurrent_action()
