import pygame 

def scale_image(img, scale):
    size = round(img.get_width() * scale), round(img.get_height() * scale)
    return pygame.transform.scale(img, size)

def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
    center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)