#hold the escape key to quit
import time
import pygame
from sys import exit
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
X=1200
Y=800

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
 
# set the pygame window name
pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 120)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render('Hello Friendz', True, green, blue)
text2 = font.render('Hello Enemies', True, blue, green) 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
textRect2 = text2.get_rect()
 
# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)
textRect2.center = (X // 2, Y // 2)
 
# infinite loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # Set running to False to end the while loop.
                exit()
    # completely fill the surface object
    # with white color
    display_surface.fill(white)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text, textRect)
    
    # completely fill the surface object
    # with white color
    
    pygame.display.update()
    time.sleep(2.0)

    display_surface.fill(blue) 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text2, textRect2)
 
    # Draws the surface object to the screen.
    pygame.display.update()
    time.sleep(2.0)
