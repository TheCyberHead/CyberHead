from colormaps import inferno

def generateHex(lenght):
	lenght = lenght + 1
	increments = round(250/lenght)
	red = [increments]
	green = [0]
	blue = [250]
	colors = []
	for x in range(0,lenght-1):
		red.append(round(red[-1]+increments))
		green.append(0)
		blue.append(blue[-1]-increments)
	for g in range(0, lenght-1):
		colors.append('#%02x%02x%02x' % (red[g], green[g], blue[g]))
	return colors

def getRGB(lenght):
	black = inferno[0:64]
	purple = inferno[64:128]
	red = inferno[128:192]
	yellow = inferno[192:256]
	if lenght > 256:
		gen = round((lenght-256)/4)
		if gen < 5:
			black.append(black[-1])
			purple.append(purple[-1])
			red.append(red[-1])
			yellow.append(yellow[-1])
			colors = black + purple + red + yellow
		else:
			black += black[-gen:]
			purple += purple[-gen:]
			yellow += yellow[-gen:]
			red += red[-gen:]
			colors = black + purple + red + yellow
	else:
		dist = round(lenght/4)
		colors = black[:dist] + purple[:dist] + red[:dist] + yellow[:dist]

	return colors
