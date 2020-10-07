import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter location: ')

if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print("Retrieving", url)

xml = urllib.request.urlopen(url).read()
data = ET.fromstring(xml)
lst = data.findall('comments/comment')
print("Count: ", len(lst))

sum = 0
for i in lst:
	x = int(i.find('count').text)
	sum = sum + x
print("Sum: ", sum)
	
	