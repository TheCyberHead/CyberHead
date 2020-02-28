import cbpro
from base64 import b64encode

class Coin:
	def __init__(self, API_KEY, API_SECRET, API_PASS, ENV_URL="https://pro.coinbase.com"):
		self.API_KEY = API_KEY
		self.API_SECRET = API_SECRET
		self.API_PASS = API_PASS
		self.ENV_URL = ENV_URL
		self.client = cbpro.AuthenticatedClient(self.API_KEY, self.API_SECRET, self.API_PASS, api_url=self.ENV_URL)

	def place_market(self, action, ticker, amount):
		order = self.client.place_market_order(
				product_id=ticker,
				side=action,
				funds=amount
			)
		return place_market

	def place_limit_order(self, action, ticker, entry_price, size):
		entry_order = self.client.place_limit_order(product_id=ticker, 
							side=action, 
							price=entry_price, 
							size=size)
		print(entry_order)
		return entry_order

	def get_accounts(self):
		return self.client.get_accounts()

	def orders(self):
		return self.client.get_orders()

	def fills(self):
		return self.client.get_fills()