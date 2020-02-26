import yfinance as yf
from sqlalchemy import create_engine 
from pandas_datareader import data as pdr

yf.pdr_override()

def download_historical(ticker: str, start_date: str, end_date: str, interval: str):
	data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date, interval = interval)
	return data