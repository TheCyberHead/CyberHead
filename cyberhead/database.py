from sqlalchemy import create_engine
import peewee
import os

engine = create_engine(f"mysql+pymysql://{os.getenv('CH_DB_USER')}:{os.getenv('CH_DB_PASSWORD')}@{os.getenv('CH_DB_HOST')}:3306/{os.getenv('CH_DB_NAME')}").connect()

'''
modules = filter(lambda x: x != '__init__.py', os.listdir("modules"))
for module in modules:
	try:
		os.listdir(f"modules/{module}").index('db.py')
		exec(f"from modules.{module}.db import *")
	except Exception as e:
		print(f'Database file not found in module {module}')
try:
	print('--------')
	databases = list(globals())
	split_db = databases[databases.index('db')+1:]
	for database in split_db:
		exec(f"{database}.create_table()")
		print(database)
except Exception as e:
	print(f"Database Integration Error. {e}")

'''

db = peewee.MySQLDatabase(os.getenv('CH_DB_NAME'),
                          host=os.getenv('CH_DB_HOST'),
                          port=3306,
                          user=os.getenv('CH_DB_USER'),
                          password=os.getenv('CH_DB_PASSWORD'))

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