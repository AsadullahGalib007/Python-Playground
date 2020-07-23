import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a URL: ')
if len(url) < 1: url = 'http://www.dr-chuck.com/'

html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# print(soup)

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
	print(tag.get('href', None))