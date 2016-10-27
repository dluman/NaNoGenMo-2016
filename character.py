import yaml

	def writeStatus(status):
		with open('yaml/sphreak-char.yaml') as character:
			yaml.dump(data,character)
		pass

	def getStatus():
		with open('yaml/sphreak-char.yaml') as character:
			status = yaml.load(character)
		return status
