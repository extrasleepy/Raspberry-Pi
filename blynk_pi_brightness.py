import blynklib
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)   # sets pin 18 as output
pi_pwm = GPIO.PWM(18,1000)      #create PWM instance with frequency
pi_pwm.start(0)

BLYNK_AUTH = 'YOUR AUTH TOKEN'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

# register handler for virtual pin V4 write event
@blynk.handle_event('write V5')
def write_virtual_pin_handler(pin, value):
   print(WRITE_EVENT_PRINT_MSG.format(pin, value))
   print(value[0])
   pi_pwm.ChangeDutyCycle(int(value[0]))
  
###########################################################
# infinite loop that waits for event
###########################################################
while True:
   blynk.run()
