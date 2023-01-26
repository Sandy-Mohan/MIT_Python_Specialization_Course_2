import json
import urllib.request, urllib.error, urllib.parse

url = input('Enter URL:')
uO = urllib.request.urlopen(url)
data = uO.read().decode()
try:
    js = json.loads(data)
except:
    js = None

count = 0
for comments in js['comments']:
    count += int(comments['count'])

print(count)

