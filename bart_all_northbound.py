#print the next train of each northbount type
import time
from requests import get
import json

api_key ="MW9S-E7SL-26DU-VV8V" 

url='http://api.bart.gov/api/etd.aspx?cmd=etd&orig=balb&dir=n&key='+api_key+'&json=y'

while True:
  bart = get(url).json()
  print (len(bart['root']['station'][0]['etd']))
  train_names = len(bart['root']['station'][0]['etd'])

  for i in range (train_names):
    print (bart['root']['station'][0]['etd'][i]['destination'],bart['root']['station'][0]['etd'][i]['estimate'][0]['minutes'])

  time.sleep(30)
