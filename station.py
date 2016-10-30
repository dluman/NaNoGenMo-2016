import plot, random, yaml

def getStation():
	with open('yaml/sphreak-station.yaml','r') as locations:
		stations = yaml.load(locations)
	return random.choice(stations)

def getCoords(station):
	return '('+str(station['Lat'])+','+str(station['Long'])+')'

def stationEvent(station):
	events = []
	items = []
	tech = station.tech
	return random.choice(events), random.choice(items), tech
