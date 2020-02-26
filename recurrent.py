from database import DataSet, engine
from modules.datasets import yahoo

data = yahoo.download_historical('AMZN', "2018-03-01", "2020-02-08", "1h")
data.to_csv('tmp/test.csv')