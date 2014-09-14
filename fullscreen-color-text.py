import pygame
import random
from time import sleep

myText=["BALLS","RATS","RUNTS","TOADS","BLOOD","CASH","PILLS","CATS","BUMS","LIGHTS","STRIP","CREME","MOLD","DRIP"]
running=True
pygame.init()
pygame.mouse.set_visible(0)
screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((random.random()*255, random.random()*255, random.random()*255))

while running:
    
    blue = random.random()*255
    green = random.random()*255
    red = random.random()*255
    
    if red>244:
        red = 244
    if blue>244:
        blue = 244
    if green>244:
        green = 244
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((red, green, blue))

    if pygame.font:
        font = pygame.font.Font(None, 750)
        text = font.render(myText[random.randint(0,len(myText))], 1, (red+10, green+10, blue+10))
        textpos = text.get_rect(centerx=(screen.get_width()/2),centery=(screen.get_height()/2))
        background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    sleep(random.randint(0,20))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False
paygame.quit()
