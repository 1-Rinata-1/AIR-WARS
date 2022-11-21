import pygame
from plane import Plane
import even
from bullet import Bullet
from pygame.sprite import Group

def start():
    pygame.init()
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("AIR WARS")
    bg_color = (127, 199, 255)
    plane = Plane(screen)
    bullets = Group()

    while True:
        even.events(screen, plane, bullets)
        plane.update_plane()
        bullets.update()
        even.update(bg_color, screen, plane, bullets)



start()
