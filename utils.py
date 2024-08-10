import pygame 

def scale_image(img, scale):
    size = round(img.get_width() * scale), round(img.get_height() * scale)
    return pygame.transform.scale(img, size)

def rotate_center(win, image, top_left, angle):
    