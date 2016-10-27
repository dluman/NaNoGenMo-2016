import distance, station, yaml

class Station:
	
	def __init__(self):
		station_obj = station.getStation()
		self.id = station_obj['Switch']
		self.name = station_obj['Name'].title()
		self.street = station_obj['Street']
		self.city = station_obj['City']
		self.zip = station_obj['ZIP']
		self.coords = station.getCoords(station_obj)

class Character:

	def __init__(self):
		char_obj = character.getStatus()
		self.name = "X"
		self.age = 0
		self.car.year = "1971"
		self.car.make = "Chevy"
		self.car.model = "Vega"
		self.car.mpg = 20
		self.car.tank = 11
		self.car.fuel = char_obj['Fuel']
		self.money = char_obj['Money']

start_station = Station()
finis_station = Station()

print "It's " + distance.calcDistance(start_station.coords,finis_station.coords) + " between " + start_station.name + " and " + finis_station.name + "."
