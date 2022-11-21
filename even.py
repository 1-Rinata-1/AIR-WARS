import pygame, sys
from bullet import Bullet


def events(screen, plane, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                plane.mright = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                plane.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, plane)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                plane.mright = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                plane.mleft = False

def update(bg_color, screen, plane, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    plane.output()
    pygame.display.flip()

