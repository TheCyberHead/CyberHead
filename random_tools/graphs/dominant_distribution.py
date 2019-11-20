from colormaps import inferno

def getColor(series_set, n):
	data_set = series_set
	if len(data_set)%2 != 0:
		data_set.append(data_set[-1])

	data_dist = round(len(data_set)/4)
	dist_one = data_set[0:data_dist]
	dist_two = data_set[data_dist:data_dist*2]
	dist_three = data_set[data_dist*2:data_dist*3]
	dist_four = data_set[data_dist*3:data_dist*4]
	if n in dist_one:
		color = [0.001462, 0.000466, 0.013866]
	elif n in dist_two:
		color = [0.335217, 0.060060, 0.428524]
	elif n in dist_three:
		color = [0.729909, 0.212759, 0.333861]
	elif n in dist_four:
		color = [0.988362, 0.998364, 0.644924]
	else:
		color = [0.559624, 0.141346, 0.410078]
	return color