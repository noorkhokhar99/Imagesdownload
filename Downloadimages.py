#....@ NoorKhokhar.....
#python Downloadimages.py
import sys
import urllib


# setup toolbar
toolbar_width = 75
percent = 0

sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
hello = 'N'

for x in range(601):
	hello == 0	
	if len(str(hello)) == 1:

		helll = ('00')
		helll +=str(x)
		#print helll
    #Place file extention
		page = ("https://www.google.com/search?ei=1m7NWePfFYaGmQG51q7IBg&hl=en&q={}")
		page+=str(helll)
		page+=str(".png")
		filee = ("page")
		filee+=str(helll)
		filee+=str(".png")		
		urllib.urlretrieve(page, filee)
		
		
	
	if len(str(hello)) == 2:
		two = ('0')
		two +=str(x)
		#print hello
		page = ("HERE HERE HERE")
		page+=str(two)
		page+=str(".jpg")
		filee = ("page")
		filee+=str(two)
		filee+=str(".jpg")		
		urllib.urlretrieve(page, filee)
		urllib.urlretrieve(page, filee)
		
		
	if len(str(hello)) == 3:
		three = ('')
		three +=str(x)
		#print three
		page = ("HERE HERE HERE")
		page+=str(three)
		page+=str(".jpg")
		filee = ("page")
		filee+=str(three)
		filee+=str(".jpg")		
		urllib.urlretrieve(page, filee)
		
		
sys.stdout.write("\n")

