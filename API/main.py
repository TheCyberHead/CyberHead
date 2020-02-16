from flask import Flask, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_cors import CORS, cross_origin
from database import DataSet

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
	print(data["identifier"])
	DataSet.create(identifier=data["identifier"], 
					reference_symbol=data["reference_symbol"], 
					description=data["description"], 
					source=data["source"])
	return request.json


if __name__ == '__main__':
	app.run(debug=True)