import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter a URL: ')

if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_815754.html'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# print(soup)
total = 0
lines = soup('span')
for line in lines:
	line = line.decode()
	x = re.findall('[0-9]+',line)
	x = int(x[0])
	total = total + x
print(total)