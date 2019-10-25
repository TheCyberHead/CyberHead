import gspread
from oauth2client.service_account import ServiceAccountCredentials
from collector import collect, makeContract
from fancy_marketdata import makeStkContract
from ib.ext.Contract import Contract
from ib.opt import ibConnection, message, Connection
from time import sleep, strftime

tickerStore = {}
ticks = []
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

def last_quote_handler(msg):
	if "finished" in msg.date:
		# generate the credentials with the google API (json file instead 'CREDS')
		creds = ServiceAccountCredentials.from_json_keyfile_name('CREDS',scope)
		client = gspread.authorize(creds)
		sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1Qvp5nHNZ9hhBZ-Z0l0IwXUxXd1_PcnjcSU8NJzNoToY/edit?usp=drive_web&ouid=108069423102413752253').sheet1
		sheet.update_acell('A1', 'Ticker')
		sheet.update_acell('B1', 'Bid')
		sheet.update_acell('C1', 'Ask')
		range_cell = 'A{}:C{}'.format(msg.reqId, msg.reqId)
		cell_list = sheet.range(range_cell)
		for index,cell in enumerate(cell_list):
		    cell.value = ticks[-1][index]
		sheet.update_cells(cell_list)
	else:
		ticks.append([tickerStore[msg.reqId],msg.open, msg.close])

def last_quote(tickerId: int, contract: tuple) -> None:
    con = ibConnection("134.209.160.105",port=7496, clientId=100)
    con.register(last_quote_handler, message.historicalData)
    con.connect()
    sleep(1)
    stkContract = makeStkContract(contract)
    con.reqMarketDataType(4)
    sleep(1)
    endtime = strftime('%Y%m%d %H:%M:%S')
    tickerStore[tickerId] = stkContract.m_symbol
    con.reqHistoricalData(tickerId,stkContract,endtime,"1 D","30 mins","BID_ASK",1,1)
    sleep(1)
    con.disconnect()
    sleep(1)



<<<<<<< HEAD
if __name__ == '__main___':
	tickers = ['AMZN', 'GOOG', 'FB', 'GS', 'JPM','NFLX', 'TSLA']
	for index,stock in enumerate(tickers):
		print(stock)
		last_quote(index+2, (stock, 'STK', 'SMART', 'USD', '', 0.0, ''))
=======
for index,stock in enumerate(tickers):
	print(stock)
	last_quote(index+2, (stock, 'STK', 'SMART', 'USD', '', 0.0, ''))
>>>>>>> 94be61114d229c195f0cbf73f4ff1d9e18d7ae2a
