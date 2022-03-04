# import pygame module in this program
import pygame
import time
from requests import get
import json
#add your api key into this URL
url = "http://api.openweathermap.org/data/2.5/weather?q=94112,us&APPID=YOUR_API_KEY&units=imperial"

 
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
 
# assigning values to X and Y variable
X = 1200
Y = 900
 
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
#display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
 
# set the pygame window name
pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 120)

 
# infinite loop
while True:
    weather_type = get(url).json()['weather'][0]['main']
    print(weather_type)
    weather_temp = get(url).json()['main']['temp']
    print(weather_temp)
    # completely fill the surface object
    # with white color
    display_surface.fill(black)
    text = font.render(weather_type, True, black, white)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    
    text2 = font.render(str(weather_temp), True, white, black)
    textRect2 = text2.get_rect()
    textRect2.center = (X // 2, Y // 3)
    
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text, textRect)
    display_surface.blit(text2, textRect2)
    # Draws the surface object to the screen.
    pygame.display.update()
    time.sleep(20) #get new data every 20 seconds
