import time
from unicornhatmini import UnicornHATMini

uh = UnicornHATMini()
uh.set_brightness(0.5)
uh.set_rotation(0)

uh.set_pixel(0, 0, 255, 255, 0)   #set one pixel
uh.show()

time.sleep(3)

for x in range(17):                      #loop to set all pixels
    for y in range(7):
        uh.set_pixel(x, y, 0, 255, 255)
uh.show()

time.sleep(3)

uh.clear()           #clear all pixels
uh.show()