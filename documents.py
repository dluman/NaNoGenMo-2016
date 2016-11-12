import os, pdfrw, random

if not os.path.isfile('texts/use.log'):
	os.mknod('texts/use.log')

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
			f.write(filename+str(randomPage))
		return filename, randomPage
	else:
		getPage(file)

def mergePages(files,pages):
	writer = pdfrw.PdfWriter()
	try: 
		novel_reader = pdfrw.PdfReader("output/novel.pdf")
		writer.addpages(novel_reader.pages)
	except: 
		try: os.mknod("output/novel.pdf")
		except: pass
	count = len(files)
	for i in range(0,count):
		choice = random.randrange(count)
		reader = pdfrw.PdfReader(files[choice])
		writer.addpage(reader.pages[pages[choice]])
		count = count - 1
		files.pop(choice)
		pages.pop(choice)
	writer.write('output/novel.pdf')

def checkUse(file,page):
	with open('texts/use.log') as f:
		records = f.read()
	for record in records:
		if file+str(page) in record:
			return True
		else:
			return False

def shufflePages():
	reader = pdfrw.PdfReader('output/novel.pdf')
	writer = pdfrw.PdfWriter()
	random.shuffle(reader.pages)
	for page in reader.pages: writer.addpage(page)
	writer.write('output/novel.pdf')
