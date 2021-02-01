from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=17, trigger=4)

while True:
    rounded=round(sensor.distance,2)
    print(rounded)
    sleep(1)
