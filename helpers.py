from database import DataSet, History

def getHistorical(ticker_identifier: str):
	data_set = DataSet.select().where(DataSet.reference_symbol == ticker_identifier)
	historical = History.select().where(History.dataset_id == data_set).execute()
	return historical

def getLastRecordHistorical(ticker_identifier: str) -> list:
	data_set = DataSet.select().where(DataSet.reference_symbol == ticker_identifier)
	historical = History.select().where(History.dataset_id == data_set).limit(1).order_by(History.id.desc()).get()
	return [historical.datetime, historical.open_price, historical.closing_price, historical.volume]

def getIntervalHistorical(ticker_identifier: str, start: str, end: str):
	pass


if __name__ == '__main__':
	print(getLastRecordHistorical('MSFT1D'))