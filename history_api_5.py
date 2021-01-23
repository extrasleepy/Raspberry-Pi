import json
import time
import requests
from requests import get

url = 'http://history.muffinlabs.com/date'


while True:
  one_day = get(url).json()
  print (one_day['data']['Events'][-1]['year'],one_day['data']['Events'][-1]['text'])
  time.sleep(30)
