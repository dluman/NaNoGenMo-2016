import random, yaml

def getStation():
	with open('yaml/sphreak-station.yaml','r') as locations:
		stations = yaml.load(locations)
	return random.choice(stations)

def getCoords(station):
	return '('+str(station['Lat'])+','+str(station['Long'])+')'
