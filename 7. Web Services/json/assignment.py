import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1: 
    url = 'http://py4e-data.dr-chuck.net/comments_815757.json'
    

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

count = len(js['comments'])
print('Count:', count)

sum = 0

for x in js['comments']:
    for i in x.values():
        if isinstance(i, int):
            sum = sum + i

print('Sum:', sum)


