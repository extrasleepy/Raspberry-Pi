import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print('start')

try:
    while True:
        input_state = GPIO.input(19)
        if input_state == False:
            print('Button Pressed')
            time.sleep(0.2)

except KeyboardInterrupt:  #end program if control+c pressed
    GPIO.cleanup()   #reset all the pins you've used
