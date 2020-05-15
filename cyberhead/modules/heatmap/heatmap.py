import numpy as np
import seaborn as sns
import uuid

def generate_heatmap(arr: list):
	unique_id = uuid.uuid1()
	ax = sns.heatmap(arr, cmap='YlGnBu')
	ax.figure.savefig('testingsea.png')