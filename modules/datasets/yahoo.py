import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

def download_historical(ticker: str, period: str, interval: str):
	data = pdr.get_data_yahoo(ticker, period=period, interval = interval)
	return data


def last_record(ticker: str, frecuency: str, last_date: str):
	pass