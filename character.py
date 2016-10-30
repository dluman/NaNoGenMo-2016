import yaml

def writeStatus(status):
	char = {}
	with open('yaml/sphreak-char.yaml','w') as character:
		for key,val in status:
			char[key] = val
		yaml.dump(char,character)

def getStatus():
	with open('yaml/sphreak-char.yaml','r') as character:
		status = yaml.load(character)
	return status[0]
