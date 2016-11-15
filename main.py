import character, distance, documents, os, pdfrw, random, station, weather, workplace, write, yaml

global fuel,money,home,trip,prev_station,time

class Station:
	
	def __init__(self):
		station_obj = station.getStation()
		self.id = station_obj['Switch']
		self.name = station_obj['Name'].title()
		self.street = station_obj['Street']
		self.city = station_obj['City']
		self.zip = station_obj['ZIP']
		self.coords = station.getCoords(station_obj)
		self.tech = station_obj['Tech']		

class Character:

	def __init__(self):
		char_obj = character.getStatus()
		self.name = char_obj['Name']
		self.age = char_obj['Age']
		self.caryear = char_obj['CYear']
		self.carmake = char_obj['CMake']
		self.carmodel = char_obj['CModel']
		self.cartank = int(char_obj['CTank'])
		self.carmpg = int(char_obj['CMPG'])
		self.carfuel = int(char_obj['Fuel'])
		self.money = int(char_obj['Money'])
		self.home = char_obj['Home']
		self.lasttrip = char_obj['Last Trip']

def takeTrip(start_point,end_point,fuel,mpg,trip,speed,time):
	if trip == 1:
		mileage = distance.calcDistance(start_point,end_point.coords)
		fromhome = 0
	if trip > 1:
		mileage = distance.calcDistance(start_point.coords,end_point.coords)
		fromhome = distance.calcDistance(home,end_point.coords)
	fuel = fuel - (float(mileage)/mpg) - (float(fromhome)/mpg)
	time = time - (float(mileage)/speed) - (float(fromhome)/speed)
	if fuel < 0:
		reason = "fuel"
		return (fuel + (float(mileage)/mpg) + (float(fromhome)/mpg),0,time + (float(mileage)/speed) + (float(fromhome)/speed),reason)
	elif time < 0:
		reason = "time"
		return (fuel + (float(mileage)/mpg) + (float(fromhome)/mpg),0,time + (float(mileage)/speed) + (float(fromhome)/speed),reason)
	trip += 1
	return fuel, trip, time, "none"

if __name__ == "__main__":
	
	#Reset character to default
	character.restore()
	
	#Initialize character
	novel_narr = Character()
	fuel = novel_narr.carfuel
	money = novel_narr.money
	speed = 42.50
	trip = 1
	paydays = [15,29]
	
	#Start nightly trip
	visits = []
	tech = []
	home = novel_narr.home
	start_station = Station()
	
	#Set up the day
	weather = weather.getForecast(novel_narr.lasttrip)
	day = weather.date.split("-")[2]
	if len(day) < 2:
		day = "0"+day

	#Events based on the day
	if int(day) in paydays: money = novel_char.money + wage
	if int(day) == 1: money = character.useSupplies(money)

	#Checking supplies
	if fuel <= 1: money, fuel_needed, fuel = character.fillUp(money,fuel)
	
	#Set the amount of time for the trip
	duration = time = random.randint(2,6)

	#Loop while resources (time, fuel) are still available
	while trip != 0:
		if trip == 1:
			fuel, trip, time, reason = takeTrip(home,start_station,fuel,novel_narr.carmpg,trip,speed,time)
			visits.append(start_station)
			tech.append(start_station.tech)
		elif trip > 1:
			start_station = prev_station
			next_station = Station()
			if start_station.name == next_station.name or next_station.name in visits: continue
			visits.append(next_station)
			tech.append(next_station.tech)
			fuel, trip, time, reason = takeTrip(start_station,next_station,fuel,novel_narr.carmpg,trip,speed,time)
			if trip == 0:
				visits.pop(len(visits)-1)
				tech.pop(len(tech)-1)
		else:
			novel_narr.carfuel = fuel
			novel_narr.money = money
			character.writeStatus(novel_narr)
			break
		prev_station = start_station
	novel_narr.carfuel = fuel
	novel_narr.money = money
	
	#Save character status
	character.writeStatus(novel_narr)
	
	#Generate character development monologue
	monologue = random.randrange(12)
	text = workplace.getWorkGripe(monologue) + "\\"
	
	#Report trip status
	text = text + " Tonight, I went out for %s hours." % (str(int(time)))
	text = text + " It was %s degrees, was rained %s inches." % (weather.low,weather.precipitation)
	for station in visits:
		text = text + " At %s I found %s manuals." % (station.name,station.tech)
	text = text + " But, I had to stop because I was out of %s." % (reason)
	try: write.createEntry(str(weather.date),text)
	except: pass
	
	#Write daily entry
	documents.entryPage()
	
	#Collect documents written & found
	for station in visits:
		found_files = []
		found_pages = []
		tech_finds = random.randrange(2,5)
		gen_finds = random.randrange(2,5)
		for i in xrange(1,tech_finds):
			doc = documents.getDoc(station.tech)
			file, page = documents.getPage(doc)
			used = documents.checkUse(file,page)
			if not used:		
				#documents.mergePages(file,page)
				found_files.append(file)
				found_pages.append(page)
		for i in xrange(1,gen_finds):
			doc = documents.getDoc("NEWS - "+day)
			file,page = documents.getPage(doc)
			used = documents.checkUse(file,page)
			if not used:
				#documents.mergePages(file,page)
				found_files.append(file)
				found_pages.append(page)
		documents.mergePages(found_files,found_pages)
		#documents.shufflePages()
	
	#Clean up temporary files
	os.remove('temp.pdf')
