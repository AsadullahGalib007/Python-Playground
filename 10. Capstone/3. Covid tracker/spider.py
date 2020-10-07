import urllib.request, urllib.parse, urllib.error
import json
import ssl
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Creating Database...................................................
conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Info')
cur.execute('''
CREATE TABLE Info(
		country TEXT,
		confirmed INTEGER,
		deaths INTEGER,
		recovered INTEGER,
		active INTEGER	
)''')



#API 1: https://covid2019-api.herokuapp.com/
#API 2: https://covid2019-api.azurewebsites.net/
url = input("Enter your own API else press ENTER: ")
if len(url)<1:
	url = 'https://covid2019-api.herokuapp.com/v2/current'

# Retriving & Inserting into Database......................................................
print('Retrieving from ', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
	js = json.loads(data)
except:
	js = None



for item in js['data']:
	lst = list()
	for i in item.values():
		lst.append(i)
	country = lst[0]
	confirmed = lst[1]
	deaths = lst[2]
	recovered = lst[3]
	active = lst[4]
	cur.execute('''INSERT INTO Info
					(country, confirmed, deaths, recovered, active)
					VALUES(?,?,?,?,?)''',
					(country, confirmed, deaths, recovered, active)
				)

conn.commit()

date = js['dt']
print('Updated at', date)