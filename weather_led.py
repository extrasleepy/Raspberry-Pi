import time
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)   # sets pin 18 as output
GPIO.setup(17,GPIO.OUT)   # sets pin 18 as output

settings = {
    'api_key':'Your API Key',
    'zip_code':'94112',
    'country_code':'us',
    'temp_unit':'imperial'} #unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid={0}&zip={1},{2}&units={3}"
while True:
    final_url = BASE_URL.format(settings["api_key"],settings["zip_code"],settings["country_code"],settings["temp_unit"])
    weather_data = requests.get(final_url).json()
    temperature = weather_data["main"]["temp"]  
    print(temperature)

    if(temperature<=57):
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(17,GPIO.LOW)
    else:
        GPIO.output(18,GPIO.LOW)
        GPIO.output(17,GPIO.HIGH)
    
    time.sleep(120) #get new data every 120 seconds
