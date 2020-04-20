from celery import Celery
from backtesting.test import SMA, GOOG
from modules.strategies import SMACrossGOOG, SMACrossAPPL
from database import BacktestPerform
from recurrent import allTimeFetch, symbolHistorical

app = Celery('tasker', broker="amqp://localhost//")

dataset_map = {
	"SMACrossGOOG": symbolHistorical('AAPL1D'),
	"SMACrossAPPL": symbolHistorical('GOOG1D')
}

strategies_map = {
	"SMACrossGOOG": SMACrossGOOG.perform_backtest,
	"SMACrossAPPL": SMACrossAPPL.perform_backtest
}

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

@app.task
def fetch_dataset_yahoo(ticker: str, period: str, interval: str, dataset_id: int):
	allTimeFetch(ticker, period, interval, dataset_id)


@app.task
def sync_dataset(source: str, symbol: str):
	return source


def run_loader():
	for strategy in strategies_map.keys():
		perform_strategy.delay(strategy)

