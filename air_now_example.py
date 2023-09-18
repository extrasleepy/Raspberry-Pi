import json
import requests
from requests import get

url = 'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94114&distance=25&API_KEY=your_api_key'

air_today = get(url).json()  
print (air_today[0]['AQI'])
print (air_today[0]['Category']['Name'])
