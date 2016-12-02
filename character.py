import datetime, yaml

def writeStatus(status):
	lasttrip = datetime.datetime.strptime(status.lasttrip,'%Y-%m-%d')
	#print lasttrip
	nexttrip = lasttrip + datetime.timedelta(days=1)
	#print nexttrip
	writedate = str(nexttrip.year) + "-" + str(nexttrip.month) + "-" + str(nexttrip.day)
	#print writedate
	char = {'Name':status.name,
		'Age':status.age,
		'CYear':status.caryear,
		'CMake':status.carmake,
		'CModel':status.carmodel,
		'CTank':status.cartank,
		'CMPG':status.carmpg,
		'Fuel':status.carfuel,
		'Money':status.money,
		'Home':status.home,
		'Last Trip':writedate}
	with open('yaml/sphreak-char.yaml','w') as character:
		yaml.dump(char,character,default_flow_style=False)

def getStatus():
	with open('yaml/sphreak-char.yaml','r') as character:
		status = yaml.load(character)
	return status

def useSupplies(money):
	#FROM http://flowingdata.com/2015/04/02/how-we-spend-our-money-a-breakdown/
	housing = .34
	transport = .16
	healthcare = .07
	food = .17
	discr = .05
	clothes = .01
	edu_loan = .02
	care = .02
	drinking = .01
	components = housing+transport+healthcare+food+discr+clothes+edu_loan+care+drinking
	money = money - (components*money)
	return money

def fillUp(money,fuel):
	cost = 1.20
	afford = money/cost
	if afford >= 11: fuel_needed = 11 - fuel
	if afford < 11: fuel_needed = money/cost
	fuel = fuel_needed
	money = money - (fuel_needed*cost)
	return money, fuel_needed, fuel

class Status:
	def __init__(self):	
		self.name = 'X'
        	self.age = 19
        	self.caryear = 1971
        	self.carmake = 'Chevy'
        	self.carmodel = 'Vega'
        	self.cartank = 11
        	self.carmpg = 20
        	self.carfuel = 11
        	self.money = 710.82
       		self.home = '(40.32486017994435,-74.24347435732415)'
       		self.lasttrip = '1985-10-31'

def restore():
	status = Status()
	writeStatus(status)
	
#Age: 17
#CMPG: 20
#CMake: Chevy
#CModel: Vega
#CTank: 11
#CYear: 1971
#Fuel: 11
#Home: (40.32486017994435,-74.24347435732415)
#Last Trip: 1985-11-1
#Money: 710.82
#Name: X
