from modules.datasets import yahoo
from database import engine
#from modules.datasets.db import DataSet
from database import DataSet, History
import numpy as np
import pandas 
import os

def allTimeFetch(ticker: str, period: str, interval: str, dataset_id: int):
	#xfetchDataSet(symbol, "max", "1d", 2212)
	data = yahoo.download_historical(ticker, period, interval)
	data.to_csv('tmp/{}.csv'.format(ticker))
	read_export = pandas.read_csv('tmp/{}.csv'.format(ticker))
	read_export.drop('Adj Close',axis=1, inplace=True)
	read_export.columns = ['datetime', 'open_price', 'high_price', 'low_price', 'closing_price', 'volume']
	read_export['dataset_id'] = dataset_id
	read_export.to_sql('history', con=engine, if_exists='append', index = False)
	return ticker

def symbolHistorical(reference_symbol: str):
	dataset_id = DataSet.select().where(DataSet.reference_symbol == reference_symbol).get()
	history_timeseries = History.select().where(History.dataset_id == dataset_id).execute()
	index_timeseries = [x.datetime for x in history_timeseries]
	open_prices = [x.open_price for x in history_timeseries]
	high_prices = [x.high_price for x in history_timeseries]
	low_prices = [x.low_price for x in history_timeseries]
	closing_prices = [x.closing_price for x in history_timeseries]
	volume = [x.volume for x in history_timeseries]
	dataframe = pandas.DataFrame(data=open_prices, columns=['Open'], index=index_timeseries)
	dataframe['High'] = high_prices
	dataframe['Low'] =  low_prices
	dataframe['Close'] = closing_prices
	dataframe['Volume'] = volume
	return dataframe


'''
open_price = peewee.FloatField()
high_price = peewee.FloatField()
low_price = peewee.FloatField()
closing_price = peewee.FloatField()
volume = peewee.IntegerField()
'''
#Open    High     Low   Close    Volume

def lastRecordYahoo(ticker: str, last_interval: str):
	pass

if __name__ == '__main__':
	symbolHistorical('AMZN1D')