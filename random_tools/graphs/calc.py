from database import Historical, Scraped
import pandas as pd 

def load_scraped_symbols():
    query = Scraped.select()
    return [record.symbol for record in query]

def drop(symbol: str, target: float, periods: int):
	try:
		stock = Historical.select(Historical.date_history,Historical.closing_price,Historical.id).where(Historical.ticker==symbol).limit(periods).order_by(Historical.date_history.desc()).execute()
		closing_prices = []
		dates = []
		for x in stock:
			closing_prices.append(x.closing_price)
			dates.append(x.date_history)
		closing_prices.reverse()
		dates.reverse()
		max_point = max(closing_prices)
		index_max = closing_prices.index(max_point)
		for price in closing_prices[index_max+1:]:
			drop_calc = round(price/max_point-1,3)
			if drop_calc <= target:
				drop_index = closing_prices.index(price)
				return [closing_prices, True, symbol, drop_calc, price, drop_index, dates, max_point, dates[drop_index]]
		return False
	except Exception as e:
		print('Error ', e)

def recover(drop_data: list, target: float, graphType: int):
	try:
		recoverRes = []
		drop_index = drop_data[5]
		drop_point = drop_data[0][drop_index]
		recover_dates = drop_data[6][drop_index+1:]
		recover_prices = drop_data[0][drop_index+1:]
		print(len(drop_data[0]))
		if graphType != 1:
			for price in recover_prices:
				recover_calc = round(price/drop_point-1,3)
				recover_index = recover_prices.index(price)
				recoverRes.append([drop_data[2], recover_dates[recover_index], drop_point, price, recover_calc])
				if recover_calc >= target:
					return recoverRes
		else:
			for price in recover_prices:
				recover_calc = round(price/drop_point-1,3)
				recover_index = recover_prices.index(price)
				recoverRes.append([drop_data[2], recover_dates[recover_index], drop_point, price, recover_calc])
		return recoverRes

	except Exception as e:
		print('Error ', e)

def generateCSV(symbol: str, dropTarget: float, recoverTarget: float, periods: int):
	try:
		result = []
		dropExec = drop(symbol, dropTarget, periods)
		if dropExec:
			dropList = ['DROP', dropExec[2], dropExec[8], dropExec[7], dropExec[4],dropExec[3]]
			result.append(dropList)
		recoverExec = recover(dropExec, recoverTarget, 1)
		if recoverExec:
			recoverList = recoverExec
			recoverList.reverse()
			recListLen = len(recoverList)
			for index,action in enumerate(recoverList):
				action[2] = recListLen-index
			df = pd.DataFrame(recoverList, columns =['symbol','time','period','price_close','recover']) 
			df.to_csv('CSV/data.csv', index=False, mode='a', header=False)
	except Exception as e:
		print('Error ', e)

for symbol in load_scraped_symbols():
	generateCSV(symbol, -0.12, 0.03, 300)