#run a DC motor using the motor bonnet

import time
from adafruit_motorkit import MotorKit
kit = MotorKit()
while True: 
   kit.motor1.throttle = 1.0
   time.sleep(5.0)
   kit.motor1.throttle = 0
   time.sleep(5.0)
