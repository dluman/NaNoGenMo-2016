import datetime, yaml

def writeStatus(status):
	lasttrip = datetime.datetime.strptime(status.lasttrip,'%Y-%M-%d')
	nexttrip = "1985-11-"+str((lasttrip.day+1))
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
		'Last Trip':nexttrip}
	with open('yaml/sphreak-char.yaml','w') as character:
		yaml.dump(char,character,default_flow_style=False)

def getStatus():
	with open('yaml/sphreak-char.yaml','r') as character:
		status = yaml.load(character)
	return status
