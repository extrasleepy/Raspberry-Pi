#top sneaker values, scrolling on unicorn hat mini
import json
import requests
import time
import sys
 
from colorsys import hsv_to_rgb
 
from PIL import Image, ImageDraw, ImageFont
from unicornhatmini import UnicornHATMini
from requests import get
# The text we want to display. You should probably keep this line and replace it below
# That way you'll have a guide as to what characters are supported!
url ="https://snkr-findr.herokuapp.com/sneakers"

text= "hello"
unicornhatmini = UnicornHATMini()

offset_x = 0
rotation = 0

if len(sys.argv) > 1:
    try:
        rotation = int(sys.argv[1])
    except ValueError:
        print("Usage: {} <rotation>".format(sys.argv[0]))
        sys.exit(1)
 
unicornhatmini.set_rotation(rotation)
display_width, display_height = unicornhatmini.get_shape()
 
print("{}x{}".format(display_width, display_height))
 
# Do not look at unicornhatmini with remaining eye
unicornhatmini.set_brightness(0.1)
 
# Load a nice 5x7 pixel font
# Granted it's actually 5x8 for some reason :| but that doesn't matter
font = ImageFont.truetype("5x7.ttf", 8)

def api_call(text):
    sneaker = get(url).json() 
    print (sneaker[0]['name'])
    print (sneaker[0]['lowest_price'])
    print (sneaker[1]['name'])
    print (sneaker[1]['lowest_price'])
    print (sneaker[2]['name'])
    print (sneaker[2]['lowest_price'])
    text=sneaker[0]['name']+" "+str(sneaker[0]['lowest_price'])
    return text

while True:

    # Measure the size of our text, we only really care about the width for the moment
    # but we could do line-by-line scroll if we used the height
    text_width, text_height = font.getsize(text)
     
    # Create a new PIL image big enough to fit the text
    image = Image.new('P', (text_width + display_width + display_width, display_height), 0)
    draw = ImageDraw.Draw(image)
    draw.text((display_width, -1), text, font=font, fill=255)
    
    for y in range(display_height):
        for x in range(display_width):
            hue = (time.time() / 10.0) + (x / float(display_width * 2))
            r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
            if image.getpixel((x + offset_x, y)) == 255:
                unicornhatmini.set_pixel(x, y, r, g, b)
            else:
                unicornhatmini.set_pixel(x, y, 0, 0, 0)
 
    offset_x += 1
    if offset_x + display_width > image.size[0]:
        offset_x = 0
        text = api_call(text)
       
    unicornhatmini.show()
    time.sleep(0.05)
