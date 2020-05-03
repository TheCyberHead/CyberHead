import alpaca_trade_api as tradeapi

class Alpaca:
	def __init__(self, api_key, api_secret):
		super(Alpaca, self).__init__()
		self.api = tradeapi.REST(api_key, api_secret, api_version='v2', base_url="https://paper-api.alpaca.markets")

	def auth(self):
		print('Authenticating Alpaca')

	def get_account(self):
		return self.api.get_account()

	def buy(self):
		return self.api.buy_market()

	def buy(self):
		return self.api.sell_market()

	def get_postions(self):
		return self.api.get_postions()