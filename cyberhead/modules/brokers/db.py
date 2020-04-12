import peewee
import os

db = peewee.MySQLDatabase(os.getenv('CH_DB_NAME'),
                          host=os.getenv('CH_DB_HOST'),
                          port=3306,
                          user=os.getenv('CH_DB_USER'),
                          password=os.getenv('CH_DB_PASSWORD'))

class Broker(peewee.Model):
	broker = peewee.CharField()
	# Coinbase / Alpaca
	api_key = peewee.CharField()
	api_secret = peewee.CharField()
	# Coinbase
	api_passphrase = peewee.CharField()
	#TDA
	refresh_token = peewee.CharField()
	current_token = peewee.CharField()
	class Meta:
	    database = db
	    db_table = 'broker'