import peewee
import os

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