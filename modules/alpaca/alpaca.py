import alpaca_trade_api as tradeapi

class Alpaca:
	def __init__(self, api_key, api_secret):
		super(Alpaca, self).__init__()
		self.api = tradeapi.REST(api_key, api_secret, api_version='v2', base_url="https://paper-api.alpaca.markets")

	def get_account(self):
		return self.api.get_account()