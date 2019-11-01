from database import Scraped
import csv


def load_symbol_set(file_name):
	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			else:
				checkRecord = Scraped.select().where(Scraped.symbol==row[1])
				if not checkRecord.exists():
					Scraped.create(symbol=row[1].upper(),exchange=row[0],currency='USD',market='SMART',symbol_type='STK')
					print(row)
					line_count += 1
				else:
					print('Exists')


load_symbol_set('sp500.csv')