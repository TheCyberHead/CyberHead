import os
import peewee
from datetime import datetime, timedelta, date
from ib.ext.Contract import Contract
from ib.opt import ibConnection
from time import sleep, strftime


collector = peewee.MySQLDatabase('collector',
                                 host='localhost',
                                 port=3306,
                                 user='root',
                                 password='deidei')


class Scraped(peewee.Model):
    exchange = peewee.CharField()
    symbol = peewee.CharField()
    symbol_type = peewee.CharField()
    market = peewee.CharField()
    currency = peewee.CharField()

    class Meta:
        database = collector
        db_table = 'scraped_symbols'


class Fundamentals(peewee.Model):
    DATE = peewee.DateField()
    EXCHANGE = peewee.CharField(max_length=20)
    TICKER = peewee.CharField(max_length=20)
    AATCA = peewee.DecimalField(max_digits=8, decimal_places=2)
    ACFSHR = peewee.DecimalField(max_digits=8, decimal_places=2)
    ADIV5YAVG = peewee.DecimalField(max_digits=8, decimal_places=2)
    AEBIT = peewee.DecimalField(max_digits=8, decimal_places=2)
    AEBTNORM = peewee.DecimalField(max_digits=8, decimal_places=2)
    AEPSNORM = peewee.DecimalField(max_digits=8, decimal_places=2)
    AEPSXCLXOR = peewee.DecimalField(max_digits=8, decimal_places=2)
    AFEEPSNTM = peewee.DecimalField(max_digits=8, decimal_places=2)
    AFPRD = peewee.DecimalField(max_digits=8, decimal_places=2)
    AFPSS = peewee.DecimalField(max_digits=8, decimal_places=2)
    ALSTD = peewee.DecimalField(max_digits=8, decimal_places=2)
    ALTCL = peewee.DecimalField(max_digits=8, decimal_places=2)
    ANIACNORM = peewee.DecimalField(max_digits=8, decimal_places=2)
    AOTLO = peewee.DecimalField(max_digits=8, decimal_places=2)
    APENORM = peewee.DecimalField(max_digits=8, decimal_places=2)
    APTMGNPCT = peewee.DecimalField(max_digits=8, decimal_places=2)
    AREVPS = peewee.DecimalField(max_digits=8, decimal_places=2)
    AROAPCT = peewee.DecimalField(max_digits=8, decimal_places=2)
    AROIPCT = peewee.DecimalField(max_digits=8, decimal_places=2)
    ASCEX = peewee.DecimalField(max_digits=8, decimal_places=2)
    ASFCF = peewee.DecimalField(max_digits=8, decimal_places=2)
    ASICF = peewee.DecimalField(max_digits=8, decimal_places=2)
    ASINN = peewee.DecimalField(max_digits=8, decimal_places=2)
    ASOPI = peewee.DecimalField(max_digits=8, decimal_places=2)
    BETA = peewee.DecimalField(max_digits=8, decimal_places=2)
    CURRENCY = peewee.DecimalField(max_digits=8, decimal_places=2)
    DIVGRPCT = peewee.DecimalField(max_digits=8, decimal_places=2)
    EPSCHNGYR = peewee.DecimalField(max_digits=8, decimal_places=2)
    EPSTRENDGR = peewee.DecimalField(max_digits=8, decimal_places=2)
    EV_Cur = peewee.DecimalField(max_digits=8, decimal_places=2)
    EV2EBITDA_Cur = peewee.DecimalField(max_digits=8, decimal_places=2)
    Frac52Wk = peewee.DecimalField(max_digits=8, decimal_places=2)
    LATESTADATE = peewee.DecimalField(max_digits=8, decimal_places=2)
    MKTCAP = peewee.DecimalField(max_digits=8, decimal_places=2)
    NetDebt_I = peewee.DecimalField(max_digits=8, decimal_places=2)
    NHIG = peewee.DecimalField(max_digits=8, decimal_places=2)
    NLOW = peewee.DecimalField(max_digits=8, decimal_places=2)
    NPRICE = peewee.DecimalField(max_digits=8, decimal_places=2)
    PEEXCLXOR = peewee.DecimalField(max_digits=8, decimal_places=2)
    PR13WKPCT = peewee.DecimalField(max_digits=8, decimal_places=2)
    PR1WKPCT = peewee.DecimalField(max_digits=8, decimal_places=2)
    PR2TANBK = peewee.DecimalField(max_digits=8, decimal_places=2)
    PR4WKPCT = peewee.DecimalField(max_digits=8, decimal_places=2)
    PR52WKPCT = peewee.DecimalField(max_digits=8, decimal_places=2)
    PRICE2BK = peewee.DecimalField(max_digits=8, decimal_places=2)
    PRYTDPCTR = peewee.DecimalField(max_digits=8, decimal_places=2)
    QATCA = peewee.DecimalField(max_digits=8, decimal_places=2)
    QBVPS = peewee.DecimalField(max_digits=8, decimal_places=2)
    QCASH = peewee.DecimalField(max_digits=8, decimal_places=2)
    QCSHPS = peewee.DecimalField(max_digits=8, decimal_places=2)
    QCURRATIO = peewee.DecimalField(max_digits=8, decimal_places=2)
    QEBIT = peewee.DecimalField(max_digits=8, decimal_places=2)
    QEBITDA = peewee.DecimalField(max_digits=8, decimal_places=2)
    QFPRD = peewee.DecimalField(max_digits=8, decimal_places=2)
    QFPSS = peewee.DecimalField(max_digits=8, decimal_places=2)
    QLSTD = peewee.DecimalField(max_digits=8, decimal_places=2)
    QLTCL = peewee.DecimalField(max_digits=8, decimal_places=2)
    QLTD2EQ = peewee.DecimalField(max_digits=8, decimal_places=2)
    QOTLO = peewee.DecimalField(max_digits=8, decimal_places=2)
    QPR2REV = peewee.DecimalField(max_digits=8, decimal_places=2)
    QPRCFPS = peewee.DecimalField(max_digits=8, decimal_places=2)
    QQUICKRATI = peewee.DecimalField(max_digits=8, decimal_places=2)
    QSCEX = peewee.DecimalField(max_digits=8, decimal_places=2)
    QSFCF = peewee.DecimalField(max_digits=8, decimal_places=2)
    QSICF = peewee.DecimalField(max_digits=8, decimal_places=2)
    QSINN = peewee.DecimalField(max_digits=8, decimal_places=2)
    QSOPI = peewee.DecimalField(max_digits=8, decimal_places=2)
    QTA = peewee.DecimalField(max_digits=8, decimal_places=2)
    QTANBVPS = peewee.DecimalField(max_digits=8, decimal_places=2)
    QTL = peewee.DecimalField(max_digits=8, decimal_places=2)
    QTOTCE = peewee.DecimalField(max_digits=8, decimal_places=2)
    QTOTD2EQ = peewee.DecimalField(max_digits=8, decimal_places=2)
    QTOTLTD = peewee.DecimalField(max_digits=8, decimal_places=2)
    REVCHNGYR = peewee.DecimalField(max_digits=8, decimal_places=2)
    REVTRENDGR = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMCFSHR = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMDIVSHR = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMEBITD = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMEBT = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMEPSCHG = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMEPSXCLX = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMFCF = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMFCFSHR = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMGROSMGN = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMINTCOV = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMINVTURN = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMNIAC = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMNIPEREM = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMNPMGN = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMOPMGN = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMPAYRAT = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMPR2REV = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMPRCFPS = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMPRFCFPS = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMPTMGN = peewee.DecimalField(max_digits=8, decimal_places=2)
    TTMREC = peewee.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        database = collector
        db_table = 'fundamentals'


def watcher(msg):
    print(msg)


def tickPriceHandler(msg):
    print(11111, msg)
    if msg.tickType == 47:
        fundamentals = str(msg).split('value=')[1].split(';')
        print(11111, msg)
        for fun in fundamentals:
            if len(fun) > 1:
                fun = fun.split('=')
                funDict[fun[0]] = fun[1]


def save_fundamentals(symbol):
    Fundamentals.insert_many(mainDict[symbol]).execute()


def makeContract(ticker):
    contract = Contract()
    contract.m_symbol = ticker
    contract.m_secType = 'STK'
    contract.m_exchange = 'SMART'
    contract.m_currency = 'USD'
    print(contract)
    return contract


def load_scraped_symbols():
    query = Scraped.select()
    return [(record.symbol, record.exchange) for record in query]


def collect():
    #for index, symbol in enumerate(scraped_symbols[:3]):  # for small tests
    for index, symbol in enumerate(scraped_symbols):
        print(11111111111111, index, symbol)
        ticker = symbol[0]
        exchange = symbol[1]
        funDict = {}
        cont = 0
        while funDict == {}:
            tws.connect()
            contractTuple = makeContract(ticker)
            sleep(5)
            print(222)
            tws.reqMktData(1, contractTuple, "233, 236, 258", False)
            print(222)
            sleep(5)
            tws.disconnect()
            print('Conecting: ', symbol)
            cont += 1
            if cont == persistence:
                print(symbol, 'fundamentals not found!')
                break

        funDict.update({'DATE': datetime.now(),
                        'EXCHANGE': exchange,
                        'TICKER': ticker})

        mainDict[symbol] = {}
        for tag in header:
            if tag in funDict:
                mainDict[symbol][tag] = funDict[tag]
            elif tag != 'id':
                mainDict[symbol][tag] = -99999.99

        print(funDict)
        print(exchange, ticker)
        save_fundamentals(symbol)
        print('Completed: ', index + 1, '/', len(scraped_symbols))


def check_time():
    next_collect = last_collect + timedelta(days=1)
    saturday = 5
    sunday = 6
    while (next_collect > datetime.now() and
           date.today() != saturday and
           date.today() != sunday
           ):
        print('waiting next collect:', next_collect)
        sleep(1000)


if __name__ == '__main__':
    #os.system('python3 scraper.py')
    if not Fundamentals.table_exists():
        Fundamentals.create_table()

    header = Fundamentals._meta.sorted_field_names

    hist = []           # historical list
    funDict = {}        # fundamental dictionary
    mainDict = {}       # main dictionary
    scraped_symbols = load_scraped_symbols()
    print(scraped_symbols)

    persistence = 5     # conections despite conections fail
    endtime = strftime('%Y%m%d %H:%M:%S')

    tws = ibConnection(port=7496, clientId=100)
    tws.register(tickPriceHandler, 'TickString')

    while True:
        last_collect = datetime.now()
        collect()
        check_time()
