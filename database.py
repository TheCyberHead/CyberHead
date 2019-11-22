import peewee
from config import db_host, db_user, db_password, db_name, db_port

collector = peewee.MySQLDatabase(db_name,
                          host='34.226.57.196',
                          port=db_port,
                          user=db_user,
                          password=db_password)

class Historical(peewee.Model):
    ticker = peewee.CharField()
    date_history = peewee.DateTimeField()
    open_price = peewee.FloatField()
    high = peewee.FloatField()
    low = peewee.FloatField()
    closing_price = peewee.FloatField()
    hasGaps = peewee.BooleanField()
    class Meta:
        database = collector
        db_table = 'historical'


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
    AATCA = peewee.FloatField()
    ACFSHR = peewee.FloatField()
    ADIV5YAVG = peewee.FloatField()
    AEBIT = peewee.FloatField()
    AEBTNORM = peewee.FloatField()
    AEPSNORM = peewee.FloatField()
    AEPSXCLXOR = peewee.FloatField()
    AFEEPSNTM = peewee.FloatField()
    AFPRD = peewee.FloatField()
    AFPSS = peewee.FloatField()
    ALSTD = peewee.FloatField()
    ALTCL = peewee.FloatField()
    ANIACNORM = peewee.FloatField()
    AOTLO = peewee.FloatField()
    APENORM = peewee.FloatField()
    APTMGNPCT = peewee.FloatField()
    AREVPS = peewee.FloatField()
    AROAPCT = peewee.FloatField()
    AROIPCT = peewee.FloatField()
    ASCEX = peewee.FloatField()
    ASFCF = peewee.FloatField()
    ASICF = peewee.FloatField()
    ASINN = peewee.FloatField()
    ASOPI = peewee.FloatField()
    BETA = peewee.FloatField()
    CURRENCY = peewee.FloatField()
    DIVGRPCT = peewee.FloatField()
    EPSCHNGYR = peewee.FloatField()
    EPSTRENDGR = peewee.FloatField()
    EV_Cur = peewee.FloatField()
    EV2EBITDA_Cur = peewee.FloatField()
    Frac52Wk = peewee.FloatField()
    LATESTADATE = peewee.FloatField()
    MKTCAP = peewee.FloatField()
    NetDebt_I = peewee.FloatField()
    NHIG = peewee.FloatField()
    NLOW = peewee.FloatField()
    NPRICE = peewee.FloatField()
    PEEXCLXOR = peewee.FloatField()
    PR13WKPCT = peewee.FloatField()
    PR1WKPCT = peewee.FloatField()
    PR2TANBK = peewee.FloatField()
    PR4WKPCT = peewee.FloatField()
    PR52WKPCT = peewee.FloatField()
    PRICE2BK = peewee.FloatField()
    PRYTDPCTR = peewee.FloatField()
    QATCA = peewee.FloatField()
    QBVPS = peewee.FloatField()
    QCASH = peewee.FloatField()
    QCSHPS = peewee.FloatField()
    QCURRATIO = peewee.FloatField()
    QEBIT = peewee.FloatField()
    QEBITDA = peewee.FloatField()
    QFPRD = peewee.FloatField()
    QFPSS = peewee.FloatField()
    QLSTD = peewee.FloatField()
    QLTCL = peewee.FloatField()
    QLTD2EQ = peewee.FloatField()
    QOTLO = peewee.FloatField()
    QPR2REV = peewee.FloatField()
    QPRCFPS = peewee.FloatField()
    QQUICKRATI = peewee.FloatField()
    QSCEX = peewee.FloatField()
    QSFCF = peewee.FloatField()
    QSICF = peewee.FloatField()
    QSINN = peewee.FloatField()
    QSOPI = peewee.FloatField()
    QTA = peewee.FloatField()
    QTANBVPS = peewee.FloatField()
    QTL = peewee.FloatField()
    QTOTCE = peewee.FloatField()
    QTOTD2EQ = peewee.FloatField()
    QTOTLTD = peewee.FloatField()
    REVCHNGYR = peewee.FloatField()
    REVTRENDGR = peewee.FloatField()
    TTMCFSHR = peewee.FloatField()
    TTMDIVSHR = peewee.FloatField()
    TTMEBITD = peewee.FloatField()
    TTMEBT = peewee.FloatField()
    TTMEPSCHG = peewee.FloatField()
    TTMEPSXCLX = peewee.FloatField()
    TTMFCF = peewee.FloatField()
    TTMFCFSHR = peewee.FloatField()
    TTMGROSMGN = peewee.FloatField()
    TTMINTCOV = peewee.FloatField()
    TTMINVTURN = peewee.FloatField()
    TTMNIAC = peewee.FloatField()
    TTMNIPEREM = peewee.FloatField()
    TTMNPMGN = peewee.FloatField()
    TTMOPMGN = peewee.FloatField()
    TTMPAYRAT = peewee.FloatField()
    TTMPR2REV = peewee.FloatField()
    TTMPRCFPS = peewee.FloatField()
    TTMPRFCFPS = peewee.FloatField()
    TTMPTMGN = peewee.FloatField()
    TTMREC = peewee.FloatField()

    class Meta:
        database = collector
        db_table = 'fundamentals'



if __name__ == '__main__':
    if not Fundamentals.table_exists():
        Fundamentals.create_table()
    if not Scraped.table_exists():
        Scraped.create_table()
    if not Historical.table_exists():
        Historical.create_table()
