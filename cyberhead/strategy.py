from builder import CHStrategy
from backtesting.lib import crossover
from backtesting.test import GOOG
import numpy as np
import talib

def trade(strategy):
	print(strategy.timeseries)

st01 = CHStrategy('alpaca', 100000, 0.5, GOOG, 5, trade)
st01.run()