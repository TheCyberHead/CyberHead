import yfinance as yf

def download_historical(tickers, start_date, end_date, interval):
	joined_tickers = ' '.join(tickers)
	intervals = ["1m","2m","5m","15m","30m","60m","90m","1h","1d","5d","1wk","1mo","3mo"]
	data = yf.download(joined_tickers, start=start_date, end=end_date, group_by = 'ticker', interval = interval)
	print(data)


if __name__ == '__main__':
	download_historical(['AMZN'], "2020-01-01", "2020-01-08", "1d")