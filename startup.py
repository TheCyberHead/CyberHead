from cyberhead.database import DataSet
from cyberhead.modules.datasets import yahoo
from sqlalchemy import create_engine
import numpy as np
import pandas
import os

engine = create_engine(f"mysql+pymysql://{os.getenv('CH_DB_USER')}:{os.getenv('CH_DB_PASSWORD')}@{os.getenv('CH_DB_HOST')}:3306/{os.getenv('CH_DB_NAME')}").connect()

def allTimeFetch(ticker: str, period: str, interval: str, dataset_id: int):
	data = yahoo.download_historical(ticker, period, interval)
	data.to_csv('cyberhead/tmp/{}.csv'.format(ticker))
	read_export = pandas.read_csv('cyberhead/tmp/{}.csv'.format(ticker))
	read_export.drop('Adj Close',axis=1, inplace=True)
	read_export.columns = ['datetime', 'open_price', 'high_price', 'low_price', 'closing_price', 'volume']
	read_export['dataset_id'] = dataset_id
	read_export.to_sql('history', con=engine, if_exists='append', index = False)
	return ticker


timeseries_ohlc = [
	{
		"identifier": "Google 1D",
		"reference_symbol":"GOOG1D",
		"ticker": "GOOG",
		"source": "Yahoo",
		"frecuency":"1D"
	},
	{
		"identifier": "Apple 1D",
		"reference_symbol":"AAPL1D",
		"ticker": "AAPL",
		"source": "Yahoo",
		"frecuency":"1D"
	}
]

for data in timeseries_ohlc:
	data_set = DataSet.create(identifier=data["identifier"], 
					reference_symbol=data["reference_symbol"],
					symbol=data["ticker"],
					source=data["source"],
					frecuency=data["frecuency"])
	allTimeFetch(data["ticker"],"max", "1d",data_set.id)
	print(f'{data["reference_symbol"]} loaded.')