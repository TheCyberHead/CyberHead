from builder import CHStrategy
from backtesting.test import GOOG
import numpy as np
import talib

def trade(strategy):
	print(strategy.dataset.Close)
	strategy.sell()

st01 = CHStrategy('alpaca', 100000, 0.5, GOOG, 5, trade)
st01.run()
st01.results()