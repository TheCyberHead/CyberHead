import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

def download_historical(ticker: str, period: str, interval: str):
	data = pdr.get_data_yahoo(ticker, period=period, interval = interval)
	return data