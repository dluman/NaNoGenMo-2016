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
	return filename, randomPage

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
