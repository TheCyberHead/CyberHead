from os import environ
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
from backtesting import Backtest, Strategy
from backtesting._plotting import plot

class CHStrategy:
	def __init__(self, broker, cash, commission, dataset, strategy, initialization, iterator, strategy_name):
		super(CHStrategy, self).__init__()
		self.broker = broker
		self.dataset = dataset
		self.cash = cash
		self.strategy = strategy
		self.commission = commission
		self.initialization = initialization
		self.iterator = iterator
		self.strategy_name = strategy_name

	def run_old(self):
		for did in range(len(self.dataset)):
			self.timeseries = self.dataset.loc[:self.dataset.iloc[did].name]
			self.algorithm(self)

	def run(self):
		self.strategy.init = self.initialization
		self.strategy.next = self.iterator
		bt = Backtest(self.dataset, self.strategy, cash=self.cash, commission=self.commission)
		output = bt.run()
		bt.plot(open_browser=False, plot_width=700, filename=f'tmp/{self.strategy_name}')
		return output