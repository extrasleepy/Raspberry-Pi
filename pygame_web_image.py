import io
import pygame as pg
try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen

# initialize pygame
pg.init()

# on a webpage right click on the image you want and use Copy image URL
image_url ="https://animalhype.com/wp-content/uploads/2020/06/Red-Panda-Names.jpg"

image_str = urlopen(image_url).read()
# create a file object (stream)
image_file = io.BytesIO(image_str)

# (r, g, b) color tuple, values 0 to 255
white = (255, 255, 255)

# create a 1200x1000 white screen
screen = pg.display.set_mode((1200,1000),  pg.RESIZABLE )
screen.fill(white)

# load the image from a file or stream
image = pg.image.load(image_file)

# draw image, position the image ulc at x=20, y=20
screen.blit(image, (20, 20))

# nothing gets displayed until one updates the screen
pg.display.flip()

# start event loop and wait until
# the user clicks on the window corner x to exit
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
