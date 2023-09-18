import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)   # sets pin 18 as output

try:
    while True :  # This constructs an infinite loop
        print ("LED on")
        GPIO.output(18,GPIO.HIGH)
        time.sleep(2.5)   #two and half second delay
        print ("LED off")
        GPIO.output(18,GPIO.LOW)
        time.sleep(2)

except KeyboardInterrupt:  #end program if control+c pressed
    GPIO.cleanup()   #reset all the pins you've used
