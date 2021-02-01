import time
from requests import get
import json

url='http://webservices.nextbus.com/service/publicJSONFeed?command=predictions&a=sf-muni&stopId=13859&routetag=1-california'
muni = get(url).json()['predictions']
data = json.dumps(muni, sort_keys=True, indent=4)
#print(data)

while True:
   muni = get(url).json()['predictions']
   print(muni['direction']['prediction'][0]['minutes'])
   time.sleep(30)
