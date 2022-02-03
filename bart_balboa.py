import time
from requests import get
import json

api_key ="Your API Key here" 

url='http://api.bart.gov/api/etd.aspx?cmd=etd&orig=balb&dir=n&key='+api_key+'&json=y'

while True:
  bart = get(url).json()
  print(bart['root']['station'][0]['name'], "Station")

  print("Next Train", bart['root']['station'][0]['etd'][0]['estimate'][0]['minutes'],"minutes")

  print("headed", bart['root']['station'][0]['etd'][0]['estimate'][0]['direction'],"to",bart['root']['station'][0]['etd'][0]['destination'])

  time.sleep(30)
