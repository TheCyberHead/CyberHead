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

	def data(self):
		pass

	def perform(self):
		print(self.dataset)

	def run(self):
		self.algorithm(self)

	def buy(self):
		pass

	def sell(self):
		self.trades.append(222)
		self.trades.append(222)
		self.trades.append(222)
		self.trades.append(222)

	def results(self):
		print(len(self.trades))

	def plot(self):
		pass