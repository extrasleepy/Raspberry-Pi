import os   #add this so you can make directories
from datetime import datetime
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)

now = (datetime.now())
tstamp = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}_{0:%M}_{0:%S}".format(now)
path = '/home/pi/Documents/'+ str(tstamp)  #path generated
os.mkdir(path)   #make the folder
os.chdir(path)    #go into folder

camera.capture('image'+str(tstamp)+'.jpg')
print ('image printed')
