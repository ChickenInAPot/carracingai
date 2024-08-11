import pygame, sys, time, math
from utils import  scale_image 

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

fps = 60
running = True

car = scale_image(pygame.image.load("/imgs/white-car.png"))


class car():
    def movement:

while running:
    pygame.time.Clock().tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    


pygame.quit()
sys.exit()