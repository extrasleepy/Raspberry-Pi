import json
import requests
from requests import get

url = 'http://history.muffinlabs.com/date'
response = requests.get(url)
rawData = response.content
print(rawData)
