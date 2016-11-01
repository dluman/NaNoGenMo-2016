import os, pdfrw, random

def getDoc(tech):
	files = []
	ls = [file for file in os.listdir('texts/')]
	for file in ls:
		if tech in file:
			files.append(file)
	return random.choice(files)

def getPage(file):
	filename = 'texts/'+file
	reader = pdfrw.PdfReader(filename)
	fileLength = len(reader.pages)
	randomPage = random.randrange(0,fileLength)
 	used = checkUse(filename,randomPage)
	if not used:
		with open('texts/use.log','aw') as f:
			f.write(filename+randomPage)
		return filename, randomPage
	else:
		getPage(file)

def mergePages(file,page):
	reader = pdfrw.PdfReader(file)
	writer = pdfrw.PdfWriter()
	try: 
		novel_reader = pdfrw.PdfReader("output/novel.pdf")
		writer.addpages(novel_reader.pages)
	except: 
		try: os.mknod("output/novel.pdf")
		except: pass
	writer.addpage(reader.pages[page])
	writer.write('output/novel.pdf')

def checkUse(file,page)
	with open('texts/use.log') as f:
		records = f.read()
	for record in records:
		if file+page in record:
			return true
		else:
			return false
