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
	#character.restore()
	
	#Initialize character
	novel_narr = Character()
	fuel = novel_narr.carfuel
	money = novel_narr.money
	speed = 42.50
	trip = 1
	paydays = [15,29]
	wage = 710.82
	
	#Start nightly trip
	visits = []
	tech = []
	home = novel_narr.home
	start_station = Station()
	
	#Set up the day
	report = weather.getForecast(novel_narr.lasttrip)
	day = str(report.date).split("-")[2]
	if len(day) < 2:
		day = "0"+day

	#Events based on the day
	if int(day) in paydays: money = novel_narr.money + wage
	if int(day) == 1: money = character.useSupplies(money)

	#Checking supplies
	if fuel <= 1: money, fuel_needed, fuel = character.fillUp(money,fuel)
	
	#Set the amount of time for the trip
	duration = time = random.randint(2,6)

	#Loop while resources (time, fuel) are still available
	while trip != 0 and fuel > 1:
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
	monologue = random.randrange(3,10)
	text = workplace.getWorkGripe(monologue) + " "
	
	#Report trip status
	#text = text + " Tonight, I went out for %s hours." % (str(int(time)))
	#text = text + " It was %s degrees, was rained %s inches." % (weather.low,weather.precipitation)
	#for station in visits:
	#	text = text + " At %s I found %s manuals." % (station.name,station.tech)
	#text = text + " But, I had to stop because I was out of %s." % (reason)
	if report.low < 32: 
		text = text + " Tonight was freezing; %s is cold! It was supposed to be %s today!" % (report.low,report.high)
	elif report.low > 32 and report.low < 50:
		text = text + " Nice November night. %s seems about right for this time of year." % (report.low)
	else:
		text = text + " %s is too warm for November." % (report.low)
	if fuel < 1:
		days = 0
		if int(day) < 15:
			days = 15 - int(day)
		elif int(day) > 15:
			days = 29 - int(day)
		if days == 1:
			plural = ""
		else:
			plural = "s"
		text = text + " But, not having money for gas to go anywhere sucks. %s day%s until pay day is too many days." % (str(days),plural)
	if float(report.precipitation) > 0:
		text = text + " Too bad it's raining outside. Seems to have rained %s inches." % (str(report.precipitation))
		if fuel > 1:
			text = text + " Got some documents though they may be a little wet."
	else:
		text = text + " At least it didn't rain."	
	try: write.createEntry(str(report.date),text)
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
	
	os.rename('output/novel.pdf','output/novel-'+day+'.pdf')
