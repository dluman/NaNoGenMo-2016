import os, pdfrw, random

def getDoc(tech):
	files = []
	ls = [file for file in os.listdir('texts/')]
	for file in ls:
		if tech in file:
			files.append(file)
	return files

def getPage(file):
	filename = 'texts/'+file
	reader = pdfrw.PdfReader(filename)
	fileLength = len(reader.pages)
	randomPage = random.randrange(1,fileLength)
	return file, randomPage

def pullPage(filename,page,destfile):
	reader = pdfrw.PdfReader(filename)
	writer = pdfrw.PdfWriter()
	writer.addpage(reader.pages[page]).write(destfile+'.pdf')
	print "DONE"

file = random.choice(getDoc("DMS100"))
