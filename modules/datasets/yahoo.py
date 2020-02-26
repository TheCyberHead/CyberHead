import yfinance as yf
from sqlalchemy import create_engine 
from pandas_datareader import data as pdr

yf.pdr_override()
engine = create_engine(f"mysql+pymysql://root:root@localhost/cyberhead").connect()

def download_historical(ticker: str, start_date: str, end_date: str, interval: str):
	data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date, interval = interval)
	data.to_csv('tmp/{}.csv'.format(ticker))


if __name__ == '__main__':
	download_historical('AMZN', "2018-03-01", "2020-02-08", "1h")