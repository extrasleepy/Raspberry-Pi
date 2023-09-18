import time
import pygame
from requests import get
import json

pygame.init()
 
# define the RGB value
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
 
# assigning values to X and Y variable
X = 1024
Y = 768

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
#display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
 
# set the pygame window name
pygame.display.set_caption('Bart')
font = pygame.font.Font('freesansbold.ttf', 70)

api_key ="Your-API-Key" 
url='http://api.bart.gov/api/etd.aspx?cmd=etd&orig=balb&dir=n&key='+api_key+'&json=y'

while True:
 
    bart = get(url).json()
    
    #print in console
    print(bart['root']['station'][0]['name'], "Station")
    print("Next Train", bart['root']['station'][0]['etd'][0]['estimate'][0]['minutes'],"minutes")
    print("headed", bart['root']['station'][0]['etd'][0]['estimate'][0]['direction'],"to",bart['root']['station'][0]['etd'][0]['destination'])
    
    #create variables to print to screen
    bart_time = "Next Train " + str(bart['root']['station'][0]['etd'][0]['estimate'][0]['minutes'])+" minutes"
    bart_train = "headed " + bart['root']['station'][0]['etd'][0]['estimate'][0]['direction'] + " to " + bart['root']['station'][0]['etd'][0]['destination']
    
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(bart_time, True, white)
    text2 = font.render(bart_train, True, white)
    
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2.5)
    textRect2.center = (X // 2, Y // 2)
    
    #fill the screen with black
    display_surface.fill(black)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text, textRect)
    display_surface.blit(text2, textRect2)
    
    
    pygame.display.update()
    time.sleep(15.0)
