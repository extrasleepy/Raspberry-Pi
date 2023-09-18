import blynklib
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

BLYNK_AUTH = 'your_auth_token'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

# register handler for virtual pin V4 write event
@blynk.handle_event('write V5')
def write_virtual_pin_handler(pin, value):
   print(WRITE_EVENT_PRINT_MSG.format(pin, value))
   print(value[0])
   kit.servo[0].angle = int(value[0])
   time.sleep(0)

@blynk.handle_event('write V6')
def write_virtual_pin_handler(pin, value):
   print(WRITE_EVENT_PRINT_MSG.format(pin, value))
   print(value[0])
   kit.servo[3].angle = int(value[0])
   time.sleep(0)
   
  
###########################################################
# infinite loop that waits for event
###########################################################
while True:
   blynk.run()
