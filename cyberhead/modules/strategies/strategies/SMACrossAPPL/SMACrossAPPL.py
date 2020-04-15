from os import environ
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG


class SMACrossAPPL(Strategy):
    def init(self):
        '''
        Close = self.data.Close
        self.ma1 = self.I(SMA, Close, 10)
        self.ma2 = self.I(SMA, Close, 20)'''
        pass

    def next(self):
        '''
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()'''
        #print(len(self.ma1))
        pass


def run_backtest():
    bt = Backtest(GOOG, SMACrossAPPL, cash=10000, commission=.002)
    output = bt.run()
    bt.plot(open_browser=True, plot_width=700, filename='SMACrossAPPL')
    return output


if __name__ == '__main__':
    run_backtest()