from sqlalchemy import create_engine
import peewee
import os


engine = create_engine(f"mysql+pymysql://root:cyberpass@localhost:3306/cyberdb").connect()

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

class DataSet(peewee.Model):
	identifier = peewee.CharField()
	reference_symbol = peewee.CharField()
	symbol = peewee.CharField()
	source = peewee.CharField()
	frecuency = peewee.CharField()
	first_fetch = peewee.BooleanField(default=False)
	class Meta:
	    database = db
	    db_table = 'dataset'

class History(peewee.Model):
	dataset_id = peewee.ForeignKeyField(DataSet)
	datetime = peewee.DateTimeField()
	open_price = peewee.FloatField()
	high_price = peewee.FloatField()
	low_price = peewee.FloatField()
	closing_price = peewee.FloatField()
	volume = peewee.IntegerField()
	class Meta:
	    database = db
	    db_table = 'history'

class BacktestPerform(peewee.Model):
	start = peewee.CharField()
	end = peewee.CharField()
	duration = peewee.CharField()
	exposure = peewee.CharField()
	equity_final = peewee.CharField()
	equity_peak = peewee.CharField()
	strategy_return = peewee.CharField()
	buy_hold_return = peewee.CharField()
	max_drawdown = peewee.CharField()
	avg_drawdown = peewee.CharField()
	max_drawdown_duration = peewee.CharField()
	avg_drawdown_duration = peewee.CharField()
	trades = peewee.CharField()
	win_rate = peewee.CharField()
	best_trade = peewee.CharField()
	worst_trade = peewee.CharField()
	avg_trade = peewee.CharField()
	max_trade_duration = peewee.CharField()
	avg_trade_duration = peewee.CharField()
	expectancy = peewee.CharField()
	sqn = peewee.CharField()
	sharpe_ratio = peewee.CharField()
	sortino_ratio = peewee.CharField()
	calmar_ratio = peewee.CharField()
	strategy_name = peewee.CharField()
	plot_path = peewee.CharField()
	class Meta:
	    database = db
	    db_table = 'backtest_perform'

if __name__ == '__main__':
	if not DataSet.table_exists():
		DataSet.create_table()
		print('Data Sets table created.')
	if not History.table_exists():
		History.create_table()
		print('History table created.')

	if not BacktestPerform.table_exists():
		BacktestPerform.create_table()
		print('Backtest Perform created.')

	if not Broker.table_exists():
		Broker.create_table()
		print('Broker table created.')
