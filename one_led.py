import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)   # sets pin 18 as output

var = 1
while var == 1 :  # This constructs an infinite loop
    print ("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(2.5)   #two and half second delay
    print ("LED off")
    GPIO.output(18,GPIO.LOW)
    time.sleep(2)
