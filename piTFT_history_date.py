import time
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

import json
import requests
from requests import get

url = 'http://history.muffinlabs.com/date'
 
# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
 
# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000
 
# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=240,
    height=240,
    x_offset=0,
    y_offset=80,
)
 
# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 180
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# First define some constants to allow easy resizing of shapes.
padding = 0
top = padding
bottom = height - padding
 
# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
 
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

while True:
    y=top
    x=0
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
     
    one_day = get(url).json()
    print (one_day['data']['Events'][-1]['year'],one_day['data']['Events'][-1]['text'])
    
    date = one_day['data']['Events'][-1]['year']
    message = one_day['data']['Events'][-1]['text']
    
    #print the date for 5 sec
    draw.text((x, y),date, font=font, fill=(255,255,255))
    
    # Display image.
    disp.image(image, rotation)
    time.sleep(30.0)
