import os, pylatex

if not os.path.isfile('test.pdf'):
	os.mknod('test.pdf')

doc = pylatex.Document()

def createEntry(date,text):
	with doc.create(pylatex.Section(date,numbering=None)):
		doc.append(text)
	doc.generate_pdf('temp',clean_tex=False)
	return('temp.pdf')

def createTitle():
	doc.preamble.append(pylatex.Command('title','Superphreak'))
	doc.preamble.append(pylatex.Command('author','Douglas Luman'))
	doc.preamble.append(pylatex.Command('date','2016'))
	doc.append(pylatex.utils.NoEscape(r'\maketitle'))
	
	doc.generate_pdf('title',clean_tex=False)
