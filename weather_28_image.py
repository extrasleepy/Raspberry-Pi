import io
import time
import pygame as pg
from requests import get
from urllib.request import urlopen

pg.init()

url = "http://api.openweathermap.org/data/2.5/weather?q=94112,us&APPID=your_key_here&units=imperial"

# (r, g, b) color tuple, values 0 to 255
white = (255, 255, 255)
black = (0,0,0)

screen = pg.display.set_mode((1200,1000),  pg.RESIZABLE )
screen.fill(black)
font = pg.font.Font('freesansbold.ttf', 120)
X = 1024
Y = 768
display_surface = pg.display.set_mode((X, Y))

while True:
    weather_type = get(url).json()['weather'][0]['main']
    print(weather_type)
    weather_temp = get(url).json()['main']['temp']
    print(weather_temp)
    weather_data = get(url).json()['weather'][0]['icon']
    image_url = "http://openweathermap.org/img/wn/"+ weather_data+"@2x.png"

    image_str = urlopen(image_url).read()
    image_file = io.BytesIO(image_str)

    # load the image from a file or stream
    image = pg.image.load(image_file)
    im_width, im_height = image.get_width(), image.get_height()  # get size
    image = pg.transform.scale(image, (im_width*3, im_height*3))
    # draw image, position the image
    screen.blit(image, (500, 0))


    text = font.render(weather_type, True, black, white)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    
    text2 = font.render(str(weather_temp), True, white, black)
    textRect2 = text2.get_rect()
    textRect2.center = (X // 2, Y // 3)

    display_surface.blit(text, textRect)
    display_surface.blit(text2, textRect2)

    # nothing gets displayed until one updates the screen
    pg.display.flip()
    
    time.sleep(30)
