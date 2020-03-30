import os
from alpaca.alpaca import Alpaca
from coinbase.coinbase import Coinbase
from poloniex.poloniex import Poloniex

brokers = {
	'alpaca': Alpaca(os.getenv('CH_ALPACA_KEY'),os.getenv('CH_ALPACA_SECRET')),
	'coinbase': Coinbase(os.getenv('CH_COINBASE_SECRET'),os.getenv('CH_COINBASE_KEY'),os.getenv('CH_COINBASE_PASSPHRASE')),
	'poloniex': Poloniex(os.getenv('CH_POLONIEX_SECRET'),os.getenv('CH_POLONIEX_KEY'))
}


class Broker:
	def __init__(self, broker):
		super(Broker, self).__init__()
		self.broker = broker

	def set_auth(self, API_KEY, API_SECRET, API_PASSPHRASE):
		pass

	def auth(self):
		return brokers[self.broker].auth()

	def place_order(self, side, price, size, symbol):
		return brokers[self.broker].place_order(side, price, size, symbol)

	def buy_market(self, price, size, symbol):
		return brokers[self.broker].buy_market(price, size, symbol)

	def sell_market(self, price, size, symbol):
		return brokers[self.broker].sell_market(price, size, symbol)

	def get_account(self):
		return brokers[self.broker].get_account()

	def get_accounts(self):
		return brokers[self.broker].get_account()

	def orders(self):
		pass

	def historical(self):
		pass

if __name__ == '__main__':
	Broker('coinbase').auth()