from os import environ
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG

from cyberhead.modules.strategies.strat import Strat

friendly_title = "SMACrossAPPL"

class SMACrossAPPL(Strat):
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
    bt = Backtest(GOOG, SMACrossAPPL, cash=10000, commission=.002)
    output = bt.run()
    bt.plot(open_browser=False, plot_width=700, filename=environ.get('CH_PATH') + '/temp/SMACrossAPPL')
    return output

#################################################
from cyberhead.modules.strategies.strat import strat
from cyberhead.modules.datasets import GOOG
from backtesting.lib import crossover


SMACrossAPPL = strat
ma1 = GOOG.ma1
ma2 = GOOG.ma2

SMACrossAPPL.broker = 'alpaca'
        if crossover(ma1, ma2):
            SMACrossAPPL.buy()
        elif crossover(ma2, ma1):
            SMACrossAPPL.sell()

SMACrossAPPL.init()
