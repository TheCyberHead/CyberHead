import requests

class Poloniex:
	def __init__(self, API_KEY, API_SECRET):
		super(Poloniex, self).__init__()
		self.API_KEY = API_KEY
		self.API_SECRET = API_SECRET
		self.private_url = 'https://poloniex.com/tradingApi'
		self.public_url = 'https://poloniex.com/public'
		self.headers = {
			'KEY': self.API_KEY,
			'SECRET': self.API_SECRET
		}

	def set_auth(self):
		pass

	def auth(self):
		print('Authenticating Poloniex')

	def check_auth(self):
		pass

	def buy_market(self, price, size, symbol):
		payload = {
            'command': 'buy',
            'currencyPair': symbol,
            'rate': price,
			'amound': size
		}
		req = requests.post(self.private_url, json=payload, headers=self.headers)
		if req.status_code == 201:
			return req.json()
		else:
			return False


	def sell_market(self, price, size, symbol):
		payload = {
			'command': 'sell',
			'currencyPair': symbol,
			'rate': price,
			'amound': size
		}
		req = requests.post(self.private_url, json=payload, headers=self.headers)
		if req.status_code == 201:
			return req.json()
		else:
			return False

	def get_account(self):
		payload = {
			'command': 'returnBalances'
		}
		req = requests.get(self.private_url, json=payload, headers=self.headers)
		if req.status_code == 200:
			return req.json()
		else:
			return False


	def orders(self):
		payload = {
			'command': 'returnTradeHistory'
		}
		req = requests.get(self.private_url, json=payload, headers=self.headers)
		if req.status_code == 200:
			return req.json()
		else:
			return False
