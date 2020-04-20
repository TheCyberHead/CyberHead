from .generate.wrapper import CustomStrategy
from .generate.builder import CHStrategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG

def initialization(self):
    Close = self.data.Close
    self.ma1 = self.I(SMA, Close, 10)
    self.ma2 = self.I(SMA, Close, 20)

def iterator(self):
    if crossover(self.ma1, self.ma2):
        self.buy()
    elif crossover(self.ma2, self.ma1):
        self.sell()

def perform_backtest(dataset):
	return CHStrategy('Alpaca', 10000, .002, dataset, CustomStrategy, initialization, iterator, 'SMACrossAPPL').run()