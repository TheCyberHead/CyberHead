from builder import CHStrategy
from backtesting.test import GOOG
import numpy as np
import talib

def trade(fn, buy, sell):
	return fn.dataset.Close

st01 = CHStrategy('alpaca',100000,0.5, GOOG, 5)
st01.algorithm(trade)
st01.run()