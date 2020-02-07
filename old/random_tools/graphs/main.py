import numpy as np
import numpy.random
import matplotlib.pyplot as plt
from database import Scraped, Historical, Fundamentals, collector
from datetime import datetime, timedelta
from decimal import Decimal

def min_max(ticker: str, timeframe: int)-> None:
	try:
		d = datetime.today() - timedelta(days=timeframe)
		combine = datetime.combine(d.date(), datetime.min.time())
		stock = Historical.select().where(Historical.ticker==ticker, Historical.date_history>=combine).execute()
		avg = []
		for x in stock:
			avg.append(x.closing_price)
		drop = round((min(avg)/max(avg)-1)*100,2)
		if avg.index(min(avg)) > avg.index(max(avg)) and drop <= -6:
			#print(f'{ticker} {drop}%')
			return drop
	except Exception as e:
		print("Error {}".format(ticker))

def getSymbols():
	stocks = Scraped.select().execute()
	return [(stock.id, stock.symbol) for stock in stocks]

def filterFall():
	try:
		dropSymbols = []
		for stock in getSymbols():
			drop = min_max(stock[1],60)
			if drop:
				if drop <= -6:
					print(stock)
					dropSymbols.append(stock[1])
		return dropSymbols
	except Exception as e:
		print(e)

def plotFundamental(fundamental):
	listSy = ['ABMD', 'AMD', 'CDNS', 'CERN', 'CME', 'FANG', 'DISCA', 'DISCK', 'FB', 'FISV', 'FTNT', 'FOXA', 'FOX', 'GILD', 'MAR', 'MYL', 'NWSA', 'NWS', 'PYPL', 'ULTA', 'VRSK', 'VIAB', 'WLTW', 'WYNN', 'XLNX', 'ADS', 'MO', 'AMCR', 'AXP', 'AMT', 'AWK', 'ANTM', 'APA', 'AZO', 'BAX', 'BDX', 'HRB', 'BSX', 'BR', 'CCL', 'CBS', 'CNC', 'SCHW', 'CVX', 'CHD', 'CLX', 'CL', 'CAG', 'CXO', 'STZ', 'COO', 'CTVA', 'CCI', 'DRI', 'DAL', 'DVN', 'DFS', 'DD', 'DXC', 'ETN', 'ECL', 'EIX', 'EOG', 'EFX', 'EL', 'EVRG', 'EXC', 'EXR', 'XOM', 'FDX', 'FIS', 'FLT', 'FMC', 'F', 'FCX', 'GD', 'GM', 'GPN', 'HCA', 'HSY', 'HES', 'HRL', 'HPQ', 'HUM', 'HII', 'IEX', 'IR', 'ICE', 'IQV', 'LB', 'LHX', 'LH', 'LDOS', 'LLY', 'LMT', 'MAC', 'MRO', 'MCD', 'MRK', 'MCO', 'MSI', 'MSCI', 'NEM', 'NI', 'NBL', 'NCLH', 'OXY', 'OMC', 'PKI', 'PG', 'PGR', 'PSA', 'RMD', 'ROP', 'RCL', 'CRM', 'SLB', 'SEE', 'SPGI', 'SYK', 'TEL', 'FTI', 'TFX', 'TWTR', 'TDG', 'TRV', 'TSN', 'UNP', 'VTR', 'V', 'WAB', 'DIS', 'WM', 'WEC', 'WMB', 'XYL', 'YUM', 'ZBH']
	query = collector.execute_sql("SELECT {} from Fundamentals where TICKER in {}".format(fundamental,tuple(listSy)))
	fundamental_list = []
	for x in query:
		fundamental_list.append(x[0])
	ss = np.array(fundamental_list, dtype=float)
	print(fundamental)
	print(len(ss))
	N_numbers = 500
	N_bins = 50
	np.random.seed(0)
	x = ss
	y = ss
	plt.hist2d(x, y, bins=N_bins, normed=False, cmap='plasma')
	cb = plt.colorbar()
	cb.set_label('Range')
	plt.title(fundamental)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.show()
	# error en generacion
	#plt.savefig('graphs/{}.png'.format(fundamental))

fnd = ["AATCA","ACFSHR","ADIV5YAVG","AEBIT","AEBTNORM","AEPSNORM","AEPSXCLXOR","AFEEPSNTM","AFPRD","AFPSS","ALSTD","ALTCL","ANIACNORM","AOTLO","APENORM","APTMGNPCT","AREVPS","AROAPCT","AROIPCT","ASCEX","ASFCF","ASICF","ASINN","ASOPI","BETA","CURRENCY","DIVGRPCT","EPSCHNGYR","EPSTRENDGR","EV_Cur","EV2EBITDA_Cur","Frac52Wk","LATESTADATE","MKTCAP","NetDebt_I","NHIG","NLOW","NPRICE","PEEXCLXOR","PR13WKPCT","PR1WKPCT","PR2TANBK","PR4WKPCT","PR52WKPCT","PRICE2BK","PRYTDPCTR","QATCA","QBVPS","QCASH","QCSHPS","QCURRATIO","QEBIT","QEBITDA","QFPRD","QFPSS","QLSTD","QLTCL","QLTD2EQ","QOTLO","QPR2REV","QPRCFPS","QQUICKRATI","QSCEX","QSFCF","QSICF","QSINN","QSOPI","QTA","QTANBVPS","QTL","QTOTCE","QTOTD2EQ","QTOTLTD","REVCHNGYR","REVTRENDGR","TTMCFSHR","TTMDIVSHR","TTMEBITD","TTMEBT","TTMEPSCHG","TTMEPSXCLX","TTMFCF","TTMFCFSHR","TTMGROSMGN","TTMINTCOV","TTMINVTURN","TTMNIAC","TTMNIPEREM","TTMNPMGN","TTMOPMGN","TTMPAYRAT","TTMPR2REV","TTMPRCFPS","TTMPRFCFPS","TTMPTMGN","TTMREC"]
for x in fnd:
	plotFundamental(x)