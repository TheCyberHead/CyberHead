from os import environ
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
from backtesting import Backtest, Strategy
from backtesting._plotting import plot

class CHStrategy:
	def __init__(self, broker, test_cash, test_comission, dataset, unit_size):
		super(CHStrategy, self).__init__()
		self.broker = broker
		self.test_cash = test_cash
		self.test_comission = test_comission
		self.dataset = dataset
		self.unit_size = unit_size
		self.trades = []

	def data(self):
		pass

	def algorithm(self, fn):
		self.algorithm = fn

	def perform(self):
		print(self.dataset)

	def run(self):
		self.algorithm(self, self.buy, self.sell)

	def buy(self):
		pass

	def sell(self):
		pass