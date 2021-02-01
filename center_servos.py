import time
from adafruit_servokit import ServoKit
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
kit.servo[0].angle = 90
kit.servo[1].angle = 90
kit.servo[2].angle = 90
kit.servo[3].angle = 90
time.sleep(2)

while True: 
    kit.servo[0].angle = 70
    time.sleep(5)
    kit.servo[0].angle = 120
    time.sleep(5)
