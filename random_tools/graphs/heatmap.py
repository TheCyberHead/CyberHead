import pandas as pd
from database import Fundamentals, collector
from decimal import Decimal
import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy as np
from random_tools.graphs.dominant_distribution import getColor
import os

def plotFundamental(fundamental,graphType):
	df = pd.read_csv('random_tools/graphs/CSV/data.csv')
	print('reading data')
	symbols = df.symbol.unique()
	periods = []
	graphOne = []
	for index,x in enumerate(symbols):
		print(f"{x} {index+1}/{len(symbols)}")
		findSymbol = df.loc[df['symbol'] == x]
		periods.append([findSymbol.iloc[0]['period'], x,findSymbol.iloc[0]['recover']])
		graphOne.append([x, list(findSymbol.recover), list(findSymbol.period)])
	
	if graphType in [2,3]:

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


		if graphType == 2:
			y_axis = periods_series
			plot_label = "Recovering Period"
		elif graphType == 3:
			y_axis = recover_percent_series
			plot_label = "Recover Percent"
		x_axis = fundamental_series

		N_bins = 100

		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.hist2d(x_axis, y_axis, bins=N_bins, normed=False, cmap='plasma')
		ax.set_label('Range')
		ax.set_title(f"Type : {graphType} / {fundamental}. Drops : -12%. Recover : 3%")
		ax.set_xlabel(f"{fundamental} / Data points : {len(fundamental_series)}")
		ax.set_ylabel(plot_label)
		fig.savefig(f'random_tools/graphs/fundamentals_visualization/Type-{graphType}-{fundamental}-Drops-12-Recover-3.png', bbox_inches='tight')
		pylab.close(fig)

	elif graphType == 1:
		stock_symbols = [x[0] for x in graphOne]
		series_values = {}
		query = collector.execute_sql("SELECT TICKER,{} from Fundamentals where TICKER in {}".format(fundamental,tuple(stock_symbols)))
		for i in query:
			series_values[i[0]] = i[1]
		for x in graphOne:
			try:
				if series_values[x[0]]:
					x.append(series_values[x[0]])
			except Exception as e:
				print(e)
		fundamental_colors = [x for x in series_values.values()]
		fundamental_colors.sort()

		for index,el in enumerate(graphOne):
			try:
				plt.plot(el[2], np.round(el[1], 2), color=getColor(fundamental_colors,el[3]), linewidth=0.5)
			except Exception as e:
				print(e)
				continue
		plt.title(f"Type : {graphType}. Drops : -12%. Recover : 3%")
		plt.xlabel('Period')
		plt.ylabel('Recover')
		plt.savefig(f'random_tools/graphs/fundamentals_visualization/type-1-drops-12-recover-3{fundamental}.png', dpi=400)

def generateMaps():
	fundamental_iter = ["AATCA","ACFSHR","ADIV5YAVG","AEBIT","AEBTNORM","AEPSNORM","AEPSXCLXOR","AFEEPSNTM","AFPRD","AFPSS","ALSTD","ALTCL","ANIACNORM","AOTLO","APENORM","APTMGNPCT","AREVPS","AROAPCT","AROIPCT","ASCEX","ASFCF","ASICF","ASINN","ASOPI","BETA","CURRENCY","DIVGRPCT","EPSCHNGYR","EPSTRENDGR","EV_Cur","EV2EBITDA_Cur","Frac52Wk","LATESTADATE","MKTCAP","NetDebt_I","NHIG","NLOW","NPRICE","PEEXCLXOR","PR13WKPCT","PR1WKPCT","PR2TANBK","PR4WKPCT","PR52WKPCT","PRICE2BK","PRYTDPCTR","QATCA","QBVPS","QCASH","QCSHPS","QCURRATIO","QEBIT","QEBITDA","QFPRD","QFPSS","QLSTD","QLTCL","QLTD2EQ","QOTLO","QPR2REV","QPRCFPS","QQUICKRATI","QSCEX","QSFCF","QSICF","QSINN","QSOPI","QTA","QTANBVPS","QTL","QTOTCE","QTOTD2EQ","QTOTLTD","REVCHNGYR","REVTRENDGR","TTMCFSHR","TTMDIVSHR","TTMEBITD","TTMEBT","TTMEPSCHG","TTMEPSXCLX","TTMFCF","TTMFCFSHR","TTMGROSMGN","TTMINTCOV","TTMINVTURN","TTMNIAC","TTMNIPEREM","TTMNPMGN","TTMOPMGN","TTMPAYRAT","TTMPR2REV","TTMPRCFPS","TTMPRFCFPS","TTMPTMGN","TTMREC"]
	for funda in fundamental_iter:
		plotFundamental(funda, 1)
		print(f'Generated Type 1 for {funda}')
		plotFundamental(funda, 2)
		print(f'Generated Type 2 for {funda}')
		plotFundamental(funda, 3)
		print(f'Generated Type 3 for {funda}')

