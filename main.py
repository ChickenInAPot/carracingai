import pygame, sys, time, math
from utils import  scale_image, blit_rotate_center

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("👨🏾‍🦲")


fps = 60
running = True

grass = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
track = scale_image(pygame.image.load("imgs/track.png"), 0.9)
car = scale_image(pygame.image.load("imgs/white-car.png"), 0.5)

startpos = (180,200)

class Car():
    def __init__(self, maxvel, rotvel):
        self.img = car
        self.max_vel = maxvel
        self.vel = 0
        self.rotation_vel = rotvel
        self.angle = 0
        self.x, self.y = startpos
        self.acceleration = 0.1
    def rotate(self, left = False, right = False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    def draw(self, screen):
        blit_rotate_center(screen, self.img, (self.x, self.y), self.angle)
    def move_forward(self):
        

    

def draw(screen, images, Car):
    for img, pos in images:
        screen.blit(img, pos)

    Car.draw(screen)
    pygame.display.update()

images = [(track, (0, 0)), (grass, (0, 0))]
test = Car(4,4)

while running:

    pygame.time.Clock().tick(fps)
    
    draw(screen, images, test)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    


pygame.quit()
sys.exit()