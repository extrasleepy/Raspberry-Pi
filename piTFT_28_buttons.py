import time
import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print('start')

# activate the pygame library
pygame.init()
 
# define the RGB values
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
yellow = (255,255,0)
 
# assigning values to X and Y variable (determines size of window)
X = 1280
Y = 900

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Button Test')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 120)
 
# which text is drawn and what color
text = font.render('Button 17', True, green, blue)
text2 = font.render('Button 22', True, blue, green)
text3 = font.render('Button 23', True, green, blue)
text4 = font.render('Button 27', True, black, yellow) 
# create a rectangular object for the text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)

# infinite loop
while True:
    
    input_state17 = GPIO.input(17)
    input_state22 = GPIO.input(22)
    input_state23 = GPIO.input(23)
    input_state27 = GPIO.input(27)
    
    if input_state17 == False:
        display_surface.fill(blue) 
        display_surface.blit(text, textRect)
   
    if input_state22 == False:
        display_surface.fill(green) 
        display_surface.blit(text2, textRect)
    
    if input_state23 == False:
        display_surface.fill(black) 
        display_surface.blit(text3, textRect)

    if input_state27 == False:
        display_surface.fill(white) 
        display_surface.blit(text4, textRect)
        
    pygame.display.update()
    time.sleep(0.1)
