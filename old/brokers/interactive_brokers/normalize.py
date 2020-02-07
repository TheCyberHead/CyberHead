from database import Scraped, Historical

symbols = [(record.symbol) for record in Scraped.select()]

for ticker in symbols:
	records = Historical.select().where(Historical.ticker==ticker)
	print(ticker)
	print(len(records))