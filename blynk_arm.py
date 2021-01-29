"""
[WRITE VIRTUAL PIN EXAMPLE] ========================================================================

Environment prepare:
In your Blynk App project:
  - add "Slider" widget,
  - bind it to Virtual Pin V4,
  - set values range 0-255
  - add "LED" widget and assign Virtual Pin V4 to it
  - Run the App (green triangle in the upper right corner).
  - define your auth token for current example and run it


This started program will periodically call and execute event handler "write_virtual_pin_handler".
In app you can move slider that will cause LED brightness change and will send virtual write event
to current running example. Handler will print pin number and it's updated value.

Schema:
====================================================================================================
          +-----------+                        +--------------+                    +--------------+
          |           |                        |              |                    |              |
          | blynk lib |                        | blynk server |                    |  blynk app   |
          |           |                        |  virtual pin |                    |              |
          |           |                        |              |                    |              |
          +-----+-----+                        +------+-------+                    +-------+------+
                |                                     |                                    |
                |                                     |  write event from "Slider" widget  |
                |                                     |                                    |
                |                                     +<-----------------------------------+
                |                                     |                                    |
                |                                     |                                    |
                |                                     |                                    |
                |                                     |                                    |
 event handler  |   write event to hw from server     |                                    |
(user function) |                                     |                                    |
     +-----------<------------------------------------+                                    |
     |          |                                     |                                    |
     |          |                                     |                                    |
     +--------->+                                     |                                    |
                |                                     |                                    |
                |                                     |                                    |
                |                                     |                                    |
                +                                     +                                    +
====================================================================================================
Additional blynk info you can find by examining such resources:

    Downloads, docs, tutorials:     https://blynk.io
    Sketch generator:               http://examples.blynk.cc
    Blynk community:                http://community.blynk.cc
    Social networks:                http://www.fb.com/blynkapp
                                    http://twitter.com/blynk_app
====================================================================================================
"""

import blynklib
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)   # sets pin 18 as output

BLYNK_AUTH = 'aND7v7xp2nfE4RQ44G4TCg08xemYcDwh'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)


# register handler for virtual pin V4 write event
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    print (value)
    if value==['1']:
        arm_down()

# register handler for virtual pin V4 write event
@blynk.handle_event('write V5')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    print (value)
    if value==['1']:
        arm_up()

    
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

###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()
