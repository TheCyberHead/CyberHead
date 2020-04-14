from os import environ
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
from backtesting import Backtest, Strategy
from backtesting._plotting import plot

class CHStrategy:
	def __init__(self, broker, test_cash, test_comission, dataset, unit_size, algorithm):
		super(CHStrategy, self).__init__()
		self.broker = broker
		self.test_cash = test_cash
		self.test_comission = test_comission
		self.dataset = dataset
		self.unit_size = unit_size
		self.trades = []
		self.algorithm = algorithm
		self.timeseries = []

	def run(self):
		for did in range(len(self.dataset)):
			self.timeseries = self.dataset.loc[:self.dataset.iloc[did].name]
			self.algorithm(self)

	def buy(self):
		print('BUY')

	def sell(self):
		print('SELL')

	def results(self):
		print(len(self.trades))

	def plot(self):
		pass
