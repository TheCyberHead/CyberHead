from database import DataSet, History


'''
Get historical data stored in local database.
'''
def getHistorical(ticker_identifier: str):
	data_set = DataSet.select().where(DataSet.reference_symbol == ticker_identifier)
	historical = History.select().where(History.dataset_id == data_set).execute()
	return historical


'''
Get las record of a give stock stored in local database.
'''
def getLastRecordHistorical(ticker_identifier: str) -> list:
	data_set = DataSet.select().where(DataSet.reference_symbol == ticker_identifier)
	historical = History.select().where(History.dataset_id == data_set).limit(1).order_by(History.id.desc()).get()
	return [historical.datetime, historical.open_price, historical.closing_price, historical.volume]

def getIntervalHistorical(ticker_identifier: str, start: str, end: str):
	pass