import time
from requests import get
import json

settings = {
    'api_key':'your_api_key',
    'zip_code':'94112',
    'country_code':'us',
    'temp_unit':'imperial'} #unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"

while True:
    final_url = BASE_URL.format(settings["api_key"],settings["zip_code"],settings["country_code"],settings["temp_unit"])
    weather_data = get(final_url).json()['weather'][0]['main']
    print(weather_data)
    time.sleep(20) #get new data every 20 seconds
