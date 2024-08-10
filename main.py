import pygame, sys, time, math

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

fps = 60
running = True


class car():
    def movement


while running:
    pygame.time.Clock().tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    


pygame.quit()
sys.exit()