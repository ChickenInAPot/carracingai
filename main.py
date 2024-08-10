import pygame, sys, time, math

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    


pygame.quit()
sys.exit()