import json
import urllib.request, urllib.error, urllib.parse
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')
param = dict()
param['address'] = address
param['key'] = api_key
url = serviceurl + urllib.parse.urlencode(param)
print(url)

try:
    uh = urllib.request.urlopen(url)
except:
    print('Failure')

data = uh.read().decode()
try:
    js = json.loads(data)
except:
    js = None

print(js['results'][0]['place_id'])
