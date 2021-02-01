import json
import requests
from requests import get

url = 'http://history.muffinlabs.com/date'
response = requests.get(url)
print(response)
