# import pygame module in this program
import pygame
import time
import textwrap
from requests import get
import json
#add your api key into this URL
url = "https://www.boredapi.com/api/activity"

 
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
X = 1280
Y = 900

wrapper = textwrap.TextWrapper(width=30)
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
font = pygame.font.Font('freesansbold.ttf', 70)

 
# infinite loop
while True:
    display_surface.fill(white)
    bored = get(url).json()['activity']
    print(bored)
    wrapped_text = wrapper.wrap(text=bored)
    
    for i in range(len(wrapped_text)):
        text = font.render(str(wrapped_text[i]), True, black, white)
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 3 +(i*100))
        display_surface.blit(text, textRect)
        pygame.display.update()
    
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text, textRect)
    # Draws the surface object to the screen.
    pygame.display.update()
    time.sleep(30) #get new data every 30 seconds
