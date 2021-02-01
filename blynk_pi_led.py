import blynklib
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)   # sets pin 18 as output

BLYNK_AUTH = 'YOUR AUTH TOKEN'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"


# register handler for virtual pin V4 write event
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    print (value)
    if value==['1']:
        GPIO.output(18,GPIO.HIGH)
        time.sleep(2.5)   #two and half second delay
    else:
        GPIO.output(18,GPIO.LOW)
        time.sleep(2.5)   #two and half second delay
    

###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()
