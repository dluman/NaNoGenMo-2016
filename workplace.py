import codecs, language, random, re

bans = ['black','spic','nigger','negro','bitch','cunt','whore','ho']

complaints = []

with codecs.open('texts/WORK.txt','r') as file:
	content = file.read()

content = content.strip()

sentences = (sentence.strip() for sentence in re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\!|\.|\?)\s',content))

for sentence in sentences:
	complaints.append(sentence.replace("\n"," ").replace("\r"," ").replace("\xad"," ").replace("\xb7"," ").replace("  "," "))

def getWorkDay(date):
	pass

def getWorkGripe(length):
	paragraph = []
	similar = 0.0
	possibility = ""
	for i in range(length):
		if i > 0:
			while len(paragraph) < length:
				similar = 0.0
				possibility = random.choice(complaints)
				#print possibility
				try: similar = language.similarity(paragraph[i-1],possibility,False)
				except: pass
				#print paragraph[0], similar
				if similar >= .43: 
					for ban in bans:
						if ban not in possibility:
							pass
						else:
							continue
					paragraph.append(possibility)
				#print similar,len(paragraph)
		elif i == 0: paragraph.append(random.choice(complaints))
	return ' '.join(paragraph)
	

