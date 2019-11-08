import peewee
from config import db_host, db_user, db_password, db_name, db_port

collector = peewee.MySQLDatabase(db_name,
                          host=db_host,
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
    AATCA = peewee.DecimalField(max_digits=8, default=0)
    ACFSHR = peewee.DecimalField(max_digits=8, default=0)
    ADIV5YAVG = peewee.DecimalField(max_digits=8, default=0)
    AEBIT = peewee.DecimalField(max_digits=8, default=0)
    AEBTNORM = peewee.DecimalField(max_digits=8, default=0)
    AEPSNORM = peewee.DecimalField(max_digits=8, default=0)
    AEPSXCLXOR = peewee.DecimalField(max_digits=8, default=0)
    AFEEPSNTM = peewee.DecimalField(max_digits=8, default=0)
    AFPRD = peewee.DecimalField(max_digits=8, default=0)
    AFPSS = peewee.DecimalField(max_digits=8, default=0)
    ALSTD = peewee.DecimalField(max_digits=8, default=0)
    ALTCL = peewee.DecimalField(max_digits=8, default=0)
    ANIACNORM = peewee.DecimalField(max_digits=8, default=0)
    AOTLO = peewee.DecimalField(max_digits=8, default=0)
    APENORM = peewee.DecimalField(max_digits=8, default=0)
    APTMGNPCT = peewee.DecimalField(max_digits=8, default=0)
    AREVPS = peewee.DecimalField(max_digits=8, default=0)
    AROAPCT = peewee.DecimalField(max_digits=8, default=0)
    AROIPCT = peewee.DecimalField(max_digits=8, default=0)
    ASCEX = peewee.DecimalField(max_digits=8, default=0)
    ASFCF = peewee.DecimalField(max_digits=8, default=0)
    ASICF = peewee.DecimalField(max_digits=8, default=0)
    ASINN = peewee.DecimalField(max_digits=8, default=0)
    ASOPI = peewee.DecimalField(max_digits=8, default=0)
    BETA = peewee.DecimalField(max_digits=8, default=0)
    CURRENCY = peewee.DecimalField(max_digits=8, default=0)
    DIVGRPCT = peewee.DecimalField(max_digits=8, default=0)
    EPSCHNGYR = peewee.DecimalField(max_digits=8, default=0)
    EPSTRENDGR = peewee.DecimalField(max_digits=8, default=0)
    EV_Cur = peewee.DecimalField(max_digits=8, default=0)
    EV2EBITDA_Cur = peewee.DecimalField(max_digits=8, default=0)
    Frac52Wk = peewee.DecimalField(max_digits=8, default=0)
    LATESTADATE = peewee.DecimalField(max_digits=8, default=0)
    MKTCAP = peewee.DecimalField(max_digits=8, default=0)
    NetDebt_I = peewee.DecimalField(max_digits=8, default=0)
    NHIG = peewee.DecimalField(max_digits=8, default=0)
    NLOW = peewee.DecimalField(max_digits=8, default=0)
    NPRICE = peewee.DecimalField(max_digits=8, default=0)
    PEEXCLXOR = peewee.DecimalField(max_digits=8, default=0)
    PR13WKPCT = peewee.DecimalField(max_digits=8, default=0)
    PR1WKPCT = peewee.DecimalField(max_digits=8, default=0)
    PR2TANBK = peewee.DecimalField(max_digits=8, default=0)
    PR4WKPCT = peewee.DecimalField(max_digits=8, default=0)
    PR52WKPCT = peewee.DecimalField(max_digits=8, default=0)
    PRICE2BK = peewee.DecimalField(max_digits=8, default=0)
    PRYTDPCTR = peewee.DecimalField(max_digits=8, default=0)
    QATCA = peewee.DecimalField(max_digits=8, default=0)
    QBVPS = peewee.DecimalField(max_digits=8, default=0)
    QCASH = peewee.DecimalField(max_digits=8, default=0)
    QCSHPS = peewee.DecimalField(max_digits=8, default=0)
    QCURRATIO = peewee.DecimalField(max_digits=8, default=0)
    QEBIT = peewee.DecimalField(max_digits=8, default=0)
    QEBITDA = peewee.DecimalField(max_digits=8, default=0)
    QFPRD = peewee.DecimalField(max_digits=8, default=0)
    QFPSS = peewee.DecimalField(max_digits=8, default=0)
    QLSTD = peewee.DecimalField(max_digits=8, default=0)
    QLTCL = peewee.DecimalField(max_digits=8, default=0)
    QLTD2EQ = peewee.DecimalField(max_digits=8, default=0)
    QOTLO = peewee.DecimalField(max_digits=8, default=0)
    QPR2REV = peewee.DecimalField(max_digits=8, default=0)
    QPRCFPS = peewee.DecimalField(max_digits=8, default=0)
    QQUICKRATI = peewee.DecimalField(max_digits=8, default=0)
    QSCEX = peewee.DecimalField(max_digits=8, default=0)
    QSFCF = peewee.DecimalField(max_digits=8, default=0)
    QSICF = peewee.DecimalField(max_digits=8, default=0)
    QSINN = peewee.DecimalField(max_digits=8, default=0)
    QSOPI = peewee.DecimalField(max_digits=8, default=0)
    QTA = peewee.DecimalField(max_digits=8, default=0)
    QTANBVPS = peewee.DecimalField(max_digits=8, default=0)
    QTL = peewee.DecimalField(max_digits=8, default=0)
    QTOTCE = peewee.DecimalField(max_digits=8, default=0)
    QTOTD2EQ = peewee.DecimalField(max_digits=8, default=0)
    QTOTLTD = peewee.DecimalField(max_digits=8, default=0)
    REVCHNGYR = peewee.DecimalField(max_digits=8, default=0)
    REVTRENDGR = peewee.DecimalField(max_digits=8, default=0)
    TTMCFSHR = peewee.DecimalField(max_digits=8, default=0)
    TTMDIVSHR = peewee.DecimalField(max_digits=8, default=0)
    TTMEBITD = peewee.DecimalField(max_digits=8, default=0)
    TTMEBT = peewee.DecimalField(max_digits=8, default=0)
    TTMEPSCHG = peewee.DecimalField(max_digits=8, default=0)
    TTMEPSXCLX = peewee.DecimalField(max_digits=8, default=0)
    TTMFCF = peewee.DecimalField(max_digits=8, default=0)
    TTMFCFSHR = peewee.DecimalField(max_digits=8, default=0)
    TTMGROSMGN = peewee.DecimalField(max_digits=8, default=0)
    TTMINTCOV = peewee.DecimalField(max_digits=8, default=0)
    TTMINVTURN = peewee.DecimalField(max_digits=8, default=0)
    TTMNIAC = peewee.DecimalField(max_digits=8, default=0)
    TTMNIPEREM = peewee.DecimalField(max_digits=8, default=0)
    TTMNPMGN = peewee.DecimalField(max_digits=8, default=0)
    TTMOPMGN = peewee.DecimalField(max_digits=8, default=0)
    TTMPAYRAT = peewee.DecimalField(max_digits=8, default=0)
    TTMPR2REV = peewee.DecimalField(max_digits=8, default=0)
    TTMPRCFPS = peewee.DecimalField(max_digits=8, default=0)
    TTMPRFCFPS = peewee.DecimalField(max_digits=8, default=0)
    TTMPTMGN = peewee.DecimalField(max_digits=8, default=0)
    TTMREC = peewee.DecimalField(max_digits=8, default=0)

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
