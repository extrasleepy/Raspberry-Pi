import time
from adafruit_servokit import ServoKit
from requests import get
import json

settings = {
    'api_key':'your_api_key',
    'zip_code':'94112',
    'country_code':'us',
    'temp_unit':'imperial'} #unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)


def arm_down():
    kit.servo[3].angle =180   #handclosed
    kit.servo[2].angle = 0
    kit.servo[1].angle = 180
    kit.servo[0].angle = 90
    time.sleep(10)

def arm_up():
    kit.servo[3].angle =180   #handclosed
    kit.servo[2].angle = 0    
    kit.servo[1].angle = 90  #move arm vertically
    kit.servo[0].angle = 90
    time.sleep(10)

while True: 
    final_url = BASE_URL.format(settings["api_key"],settings["zip_code"],settings["country_code"],settings["temp_unit"])
    weather_data = get(final_url).json()['weather'][0]['main']
    print(weather_data)
    if (weather_data=="Rain"):
      print("yes")
      arm_up()
    else:
      arm_down()
    time.sleep(30)
