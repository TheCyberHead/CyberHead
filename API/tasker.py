from celery import Celery
from strategies.strategy_one import run_backtest
app = Celery('tasker', broker="amqp://localhost//")

strategies = {
	"CrossGOOG": run_backtest
}

@app.task
def perform_strategy(name: str) -> list:
	# Generated backtest file not being loaded in the strategies folder.
	perform = strategies[name]()
	return perform

@app.task
def sync_dataset(source: str, symbol: str):
	pass
