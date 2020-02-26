from flask import Flask, request, jsonify, send_from_directory
from playhouse.shortcuts import model_to_dict
from flask_cors import CORS, cross_origin
from database import DataSet, BacktestPerform
from tasker import perform_strategy, run_loader

app = Flask(__name__)
CORS(app)

@app.route('/datasets', methods=['GET'])
def list_datasets():
	datasets = DataSet.select()
	return jsonify({'datasets':[model_to_dict(dataset) for dataset in datasets]})

@app.route('/datasets/<int:task_id>', methods=["GET"])
def get_dataset(task_id):
	pass

@app.route('/datasets', methods=['POST'])
def create_dataset():
	data = request.json
	DataSet.create(identifier=data["identifier"], 
					reference_symbol=data["reference_symbol"],
					symbol=data["ticker"],
					source=data["source"],
					frecuency=data["frecuency"])
	return request.json


@app.route('/perform_backtest', methods=['POST'])
def perform_backtest():
	data = request.json
	perform_async = perform_strategy.delay(data['strategy_name'])
	return {"execution_id": str(perform_async)}

@app.route('/backtest_status/<queue_reference>', methods=["GET"])
def backtest_status(queue_reference):
	pass

@app.route('/get_strategies', methods=["GET"])
def get_strategies():
	strategies_list = BacktestPerform.select(BacktestPerform.strategy_name).distinct().execute()
	return jsonify({'strategies':[model_to_dict(strategy) for strategy in strategies_list]})

@app.route('/portfolio_strategies', methods=["GET"])
def portfolio_strategies():
	strategies_list = BacktestPerform.select(BacktestPerform.strategy_name, BacktestPerform.strategy_return, BacktestPerform.equity_final, BacktestPerform.sharpe_ratio).distinct().execute()
	return jsonify({'strategies':[model_to_dict(strategy) for strategy in strategies_list]})

@app.route('/get_strategy/<strategy>')
def get_strategy(strategy):
	strategy_data = BacktestPerform.select().where(BacktestPerform.strategy_name == strategy).order_by(BacktestPerform.id.desc()).limit(1)
	return jsonify({'strategy':[model_to_dict(strategy) for strategy in strategy_data]})

@app.route('/get_plot/<strategy>')
def get_plot(strategy):
	return send_from_directory('tmp', strategy)


if __name__ == '__main__':
	run_loader()
	app.run(debug=True)