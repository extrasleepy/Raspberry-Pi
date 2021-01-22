import time
import requests

from PIL import Image

from unicornhatmini import UnicornHATMini
unicornhatmini = UnicornHATMini()

unicornhatmini.set_brightness(0.5)

temp_color=0

settings = {
    'api_key':'0e974dbb38ad3719228ac1854b212827',
    'zip_code':'94112',
    'country_code':'us',
    'temp_unit':'imperial'} #unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"


while True:
    final_url = BASE_URL.format(settings["api_key"],settings["zip_code"],settings["country_code"],settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    temperature = weather_data["main"]["temp"]  
    print(temperature)
    
    temp_color=int(temperature)
    if temperature >= 85:
        image = Image.new("RGB", (17, 7), (255, 0, 0))
    if temperature >= 55 and temperature <= 85:
        image = Image.new("RGB", (17, 7), (0, 255, 0))
    if temperature <= 55:
        image = Image.new("RGB", (17, 7), (0, 0, 255))

    unicornhatmini.set_image(image)
    unicornhatmini.show()
    time.sleep(60) #get new data every 60 seconds
