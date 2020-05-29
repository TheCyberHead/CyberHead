from flask import Flask, request, jsonify, send_from_directory
from playhouse.shortcuts import model_to_dict
from flask_cors import CORS, cross_origin
from modules.datasets.db import DataSet
from modules.strategies.db import BacktestPerform
from database import HeatMap
from tasker import perform_strategy, run_loader, fetch_dataset_yahoo, generate_heatmap
import os
import json
import base64
import uuid 

app = Flask(__name__)
CORS(app)

'''
/datasets => GET
Lists saved and synced datasets stored in database.
'''

@app.route('/datasets', methods=['GET'])
def list_datasets():
	datasets = DataSet.select()
	return jsonify({'datasets':[model_to_dict(dataset) for dataset in datasets]})

'''
/datasets/{id} => GET
@id = DataSet ID, can be found in the response of the /datasets endpoint
Get dataset
'''
@app.route('/datasets/<int:task_id>', methods=["GET"])
def get_dataset(task_id):
	pass


'''
/datasets => POST
@identifier = Any reference you'd like to store
@reference_symbol = Historical identifier, should not be the same as the stock symbol, because this identifier is intended to be used as a differentiator, i.e, for AMZN at 1 week historical yoy may use AMZN1W
@symbol = The underlying stock symbol to look for in the market.
@source = The data source where you would like to fetch the historical prices. Yahoo, Ameritrade, Alpaca.
Save a initiate a fetch of a historical pricing data.
'''
@app.route('/datasets', methods=['POST'])
def create_dataset():
	data = request.json
	data_set = DataSet.create(identifier=data["identifier"], 
					reference_symbol=data["reference_symbol"],
					symbol=data["ticker"],
					source=data["source"],
					frecuency=data["frecuency"])
	fetch_dataset_yahoo.delay(data["ticker"],"max", "1d",data_set.id)
	return request.json


'''
This method is used to perform the backtests of the strategies stored in the strategies module, this doesn't require any interaction on your side.
'''
@app.route('/perform_backtest', methods=['POST'])
def perform_backtest():
	data = request.json
	perform_async = perform_strategy.delay(data['strategy_name'])
	return {"execution_id": str(perform_async)}

'''
Return a list of all the available strategies in CyberHead.
'''
@app.route('/get_strategies', methods=["GET"])
def get_strategies():
	strategies_list = BacktestPerform.select(BacktestPerform.strategy_name).distinct().execute()
	return jsonify({'strategies':[model_to_dict(strategy) for strategy in strategies_list]})

'''
Return all the performing data of al strategies.
'''
@app.route('/portfolio_strategies', methods=["GET"])
def portfolio_strategies():
	strategies_list = BacktestPerform.select(BacktestPerform.strategy_name, BacktestPerform.strategy_return, BacktestPerform.equity_final, BacktestPerform.sharpe_ratio).distinct().execute()
	return jsonify({'strategies':[model_to_dict(strategy) for strategy in strategies_list]})

'''
Return all the performing data of a single strategy.
'''
@app.route('/get_strategy/<strategy>')
def get_strategy(strategy):
	strategy_data = BacktestPerform.select().where(BacktestPerform.strategy_name == strategy).order_by(BacktestPerform.id.desc()).limit(1)
	return jsonify({'strategy':[model_to_dict(strategy) for strategy in strategy_data]})

'''
Shows the plotting timeseries of a performed strategy, with all the trades made in the given timeframe.
'''
@app.route('/get_plot/<strategy>')
def get_plot(strategy):
	return send_from_directory('tmp', strategy)


@app.route('/get_heatmap/<heatmap>')
def get_heatmap(heatmap):
	return send_from_directory('tmp/images', heatmap)

'''
Get all strategies to be available on editor.
'''
@app.route('/get_strategies_edit', methods=["GET"])
def strategies_dir():
	strategies_edit = os.listdir("/Users/luispereira/Documents/CyberHead/cyberhead/modules/strategies")
	strategies_edit.remove('__pycache__')
	return {'strategies':strategies_edit}

'''
Edit an strategy and save the code.
'''
@app.route('/get_strategy_edit/<strategy_name>')
def strategy_get_edit(strategy_name):
	find_strategy = open(f'/Users/luispereira/Documents/CyberHead/cyberhead/modules/strategies/{strategy_name}', 'r')
	return {'strategy_code': find_strategy.read()}



@app.route('/heatmap', methods=["POST", "GET"])
def heatmap():
	print(request.method)
	if request.method == 'POST':
		title = request.json['heatmap']['title']
		file = request.json['heatmap']['file64'][21:]
		unique_id = uuid.uuid1()
		heatmap = HeatMap.create(title=title,
								file_tmp_path=f"{unique_id}.csv",
								file_encoded=file,
								image_encoded="NA"
					)
		with open(f"tmp/{unique_id}.csv", "wb") as f:
		    f.write(base64.b64decode(file))
		    f.close()
		generate_heatmap(unique_id, heatmap.id)
		return request.json
	elif request.method == 'GET':
		heatmaps = HeatMap.select()
		return jsonify({'heatmaps':[model_to_dict(heatmap) for heatmap in heatmaps]})

"""
This sections defines how Flask is listening, when deploying for a production instance you should set debug to False and set the host parameter to 0.0.0.0
"""
if __name__ == '__main__':
	#run_loader()
	app.run(debug=True, host='0.0.0.0')
