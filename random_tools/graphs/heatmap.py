import pandas as pd
from database import Fundamentals, collector
from decimal import Decimal
import matplotlib.pyplot as plt
from test import getRGB

def plotFundamental(fundamental,graphType):
	df = pd.read_csv('CSV/data.csv')
	symbols = df.symbol.unique()
	periods = []
	graphOne = []
	for x in symbols:
		findSymbol = df.loc[df['symbol'] == x]
		periods.append([findSymbol.iloc[0]['period'], x,findSymbol.iloc[0]['recover']])
		graphOne.append([x, list(findSymbol.recover), list(findSymbol.period)])
	
	query = collector.execute_sql("SELECT TICKER,{} from Fundamentals where TICKER in {}".format(fundamental,tuple(symbols)))
	if query:
		for i in query:
			for b in periods:
				if i[0] == b[1]:
					if i[1] != Decimal('-999.99999'):
						b.append(i[1])
					else:
						periods.remove(b)

	filterPeriods = list(filter(lambda x: len(x) > 3, periods))
	periods_series = [b[0] for b in filterPeriods]
	recover_percent_series = [round(float(b[2]),3) for b in filterPeriods]
	fundamental_series = [round(float(b[3]),3) for b in filterPeriods]
	if graphType in [2,3]:
		if graphType == 2:
			y_axis = periods_series
			plot_label = "Recovering Period"
		elif graphType == 3:
			y_axis = recover_percent_series
			plot_label = "Recover Percent"
		x_axis = fundamental_series

		N_bins = 100
		plt.hist2d(x_axis, y_axis, bins=N_bins, normed=False, cmap='plasma')
		cb = plt.colorbar()
		cb.set_label('Range')
		plt.title(f"{fundamental} Type : {graphType}. Drops : -3%. Recover : 1%")
		plt.xlabel(fundamental)
		plt.ylabel(plot_label)
		plt.show()
	elif graphType == 1:
		colors = getRGB(len(graphOne))
		for index,el in enumerate(graphOne):
			plt.plot(el[2], el[1], color=colors[index], linewidth=0.5)
		plt.title(f"Type : {graphType}. Drops : -3%. Recover : 1%")
		plt.xlabel('Period')
		plt.ylabel('Recover')
		plt.show()


'''
fundamental_iter = ["AATCA","ACFSHR","ADIV5YAVG","AEBIT","AEBTNORM","AEPSNORM","AEPSXCLXOR","AFEEPSNTM","AFPRD","AFPSS","ALSTD","ALTCL","ANIACNORM","AOTLO","APENORM","APTMGNPCT","AREVPS","AROAPCT","AROIPCT","ASCEX","ASFCF","ASICF","ASINN","ASOPI","BETA","CURRENCY","DIVGRPCT","EPSCHNGYR","EPSTRENDGR","EV_Cur","EV2EBITDA_Cur","Frac52Wk","LATESTADATE","MKTCAP","NetDebt_I","NHIG","NLOW","NPRICE","PEEXCLXOR","PR13WKPCT","PR1WKPCT","PR2TANBK","PR4WKPCT","PR52WKPCT","PRICE2BK","PRYTDPCTR","QATCA","QBVPS","QCASH","QCSHPS","QCURRATIO","QEBIT","QEBITDA","QFPRD","QFPSS","QLSTD","QLTCL","QLTD2EQ","QOTLO","QPR2REV","QPRCFPS","QQUICKRATI","QSCEX","QSFCF","QSICF","QSINN","QSOPI","QTA","QTANBVPS","QTL","QTOTCE","QTOTD2EQ","QTOTLTD","REVCHNGYR","REVTRENDGR","TTMCFSHR","TTMDIVSHR","TTMEBITD","TTMEBT","TTMEPSCHG","TTMEPSXCLX","TTMFCF","TTMFCFSHR","TTMGROSMGN","TTMINTCOV","TTMINVTURN","TTMNIAC","TTMNIPEREM","TTMNPMGN","TTMOPMGN","TTMPAYRAT","TTMPR2REV","TTMPRCFPS","TTMPRFCFPS","TTMPTMGN","TTMREC"]

for x in fundamental_iter[:6]:
	plotFundamental(x)'''

plotFundamental('EV2EBITDA_Cur', 1)
