from database import DataSet, engine
from modules.datasets import yahoo
import numpy as np
import pandas

def allTimeFetch(ticker: str, period: str, interval: str, dataset_id: int):
	#xfetchDataSet(symbol, "max", "1d", 2212)
	data = yahoo.download_historical(ticker, period, interval)
	data.to_csv('tmp/{}.csv'.format(ticker))
	read_export = pandas.read_csv('tmp/{}.csv'.format(ticker))
	read_export.drop('Adj Close',axis=1, inplace=True)
	read_export.columns = ['datetime', 'open_price', 'high_price', 'low_price', 'closing_price', 'volume']
	read_export['dataset_id'] = dataset_id
	read_export.to_sql('history', con=engine, if_exists='append', index = False)