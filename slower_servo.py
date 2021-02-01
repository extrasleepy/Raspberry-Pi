import time
from adafruit_servokit import ServoKit
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
kit.servo[0].angle = 90   #set servos to "center" positions
kit.servo[1].angle = 90
kit.servo[2].angle = 90
kit.servo[3].angle = 90
time.sleep(2)

for i in range(90,60,-1):
      kit.servo[0].angle = i
      time.sleep(0.02)

while True:
   for i in range(60,130,1):
      kit.servo[0].angle = i
      time.sleep(0.02)
   time.sleep(2)
