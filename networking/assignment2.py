import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

count = 0
pos = 0

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Decklan.html'
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

def request(url):
	global html
	global soup
	html = urllib.request.urlopen(url, context = ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

def task():
	global pos
	tags = soup('a')
	for tag in tags:
		link = tag.get('href', None)
		pos = pos + 1
		if pos == 18:
			print('Retrieving: ' + link)
			pos = 0
			return link

def extraction(link):
	name = re.findall('_by_([A-Za-z]*)',link)
	print(name[0])


print('Retrieving: ' + url)
request(url)
url = task()
while count < 6:
	request(url)
	url = task()
	count = count + 1

extraction(url)