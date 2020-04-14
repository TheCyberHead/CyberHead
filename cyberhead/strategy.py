from builder import CHStrategy
from backtesting.lib import crossover
from backtesting.test import GOOG
import numpy as np
import talib

def trade(strategy):
	ma1 = talib.SMA(strategy.timeseries.Close, 10)
	ma2 = talib.SMA(strategy.timeseries.Close, 20)
	print(ma1)

st01 = CHStrategy('alpaca', 100000, 0.5, GOOG, 5, trade)
st01.run()