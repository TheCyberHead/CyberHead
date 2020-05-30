from celery import Celery
from backtesting.test import SMA, GOOG
from modules.strategies import SMACrossGOOG, SMACrossAPPL
from database import BacktestPerform, HeatMap
from recurrent import allTimeFetch, symbolHistorical
import matplotlib as mpl
mpl.use('Agg')
import seaborn as sns
import matplotlib.pyplot as plt
import uuid
import csv

'''
Celery Initialization
If your broker instance is located out of localhost replace replace it below, or set the propper URL if you're lookign to use Redis.
'''
app = Celery('tasker', broker="amqp://rabbit//")


'''
Define the first initialization of datasets on startup.
'''

dataset_map = {
	"SMACrossGOOG": symbolHistorical('GOOG1D'),
	"SMACrossAPPL": symbolHistorical('AAPL1D')
}

'''
Define the available strategies enabled to be reach by the 
'''

strategies_map = {
	"SMACrossGOOG": SMACrossGOOG.perform_backtest,
	"SMACrossAPPL": SMACrossAPPL.perform_backtest
}

'''
This task enqueue the execution of strategy, since this is an CPU intensive task it should not be executed in a single thread.
'''
@app.task
def perform_strategy(name: str) -> list:
	perform = strategies_map[name](dataset_map[name])
	plot_path = f"{name}.html"
	BacktestPerform.create(
		start=perform["Start"],
		end=perform["End"],
		duration=perform["Duration"],
		exposure=perform["Exposure [%]"],
		equity_final=perform["Equity Final [$]"],
		equity_peak=perform["Equity Peak [$]"],
		strategy_return=perform["Return [%]"],
		buy_hold_return=perform["Buy & Hold Return [%]"],
		max_drawdown=perform["Max. Drawdown [%]"],
		avg_drawdown=perform["Avg. Drawdown [%]"],
		max_drawdown_duration=perform["Max. Drawdown Duration"],
		avg_drawdown_duration=perform["Avg. Drawdown Duration"],
		trades=perform["# Trades"],
		win_rate=perform["Win Rate [%]"],
		best_trade=perform["Best Trade [%]"],
		worst_trade=perform["Worst Trade [%]"],
		avg_trade=perform["Avg. Trade [%]"],
		max_trade_duration=perform["Max. Trade Duration"],
		avg_trade_duration=perform["Avg. Trade Duration"],
		expectancy=perform["Expectancy [%]"],
		sqn=perform["SQN"],
		sharpe_ratio=perform["Sharpe Ratio"],
		sortino_ratio=perform["Sortino Ratio"],
		calmar_ratio=perform["Calmar Ratio"],
		strategy_name=name,
		plot_path=plot_path
		)
	return name


'''
Get historical pricing data from Yahoo (Queue)
'''
@app.task
def fetch_dataset_yahoo(ticker: str, period: str, interval: str, dataset_id: int):
	allTimeFetch(ticker, period, interval, dataset_id)


'''
Sync dataset with the latest updates
'''
@app.task
def sync_dataset(source: str, symbol: str):
	return source

'''
The loader is the first entry point that will be executed once you run the application.
'''
def run_loader():
	for strategy in strategies_map.keys():
		perform_strategy.delay(strategy)

def generate_heatmap(file_path, heatmap_id):
	with open(f'tmp/{file_path}.csv', newline='') as f:
	    reader = csv.reader(f)
	    data = list(reader)
	    f.close()
	headers, csv_data = data[0],data[1:]
	csv_data = [[int(x[0]), int(x[1])] for x in csv_data]
	unique_id = uuid.uuid1()
	ax = sns.heatmap(csv_data, cmap='YlGnBu')
	ax.figure.savefig(f'tmp/images/{unique_id}.png')
	plt.close()
	q = HeatMap.update(image_encoded=f'tmp/images/{unique_id}.png').where(HeatMap.id==heatmap_id)
	q.execute()

