from bs4 import BeautifulSoup
import urllib2
import pandoc

url = "http://mailchi.mp/ca15c2e6ebb0/71"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)
simple_html = ''

divs = soup.find_all(style="text-align: center;")
for div in divs:
	try:
		print div.contents[3]
	except:
		continue
