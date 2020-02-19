from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG

class CrossGOOG(Strategy):
    def init(self):
        Close = self.data.Close
        self.ma1 = self.I(SMA, Close, 10)
        self.ma2 = self.I(SMA, Close, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


def run_backtest():
	bt = Backtest(GOOG, CrossGOOG, cash=10000, commission=.002)
	output = bt.run()
	bt.plot(open_browser=False, plot_width=700)
	return output