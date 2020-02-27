from database import DataSet, engine
from modules.datasets import yahoo
import numpy as np
import pandas

def fetchDataSet(ticker: str, period: str, interval: str, dataset_id: int):
	data = yahoo.download_historical(ticker, period, interval)
	data.to_csv('tmp/test.csv')
	read_export = pandas.read_csv('tmp/test.csv')
	read_export.drop('Adj Close',axis=1, inplace=True)
	read_export.columns = ['datetime', 'open_price', 'high_price', 'low_price', 'closing_price', 'volume']
	read_export['dataset_id'] = 12422
	read_export.to_sql('history', con=engine, if_exists='append', index = False)
	print(read_export)



if __name__ == '__main__':
	symbols = ['NFLX', 'AMZN', 'GS', 'MS', 'GOOG', 'FB', 'TSLA', 'WM', 'UBER', 'CRM', 'F', 'T', 'KO']
	for symbol in symbols:
		fetchDataSet(symbol, "max", "1d", 2212)