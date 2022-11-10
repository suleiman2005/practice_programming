import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 255, 255)
PURPLE = (255, 0, 255)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle(screen, RED, event.pos, 10)
            elif event.button == 2:
                circle(screen, GREEN, event.pos, 10)
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, 10)
            elif event.button == 4:
                circle(screen, LIGHT_BLUE, event.pos, 10)
            elif event.button == 5:
                circle(screen, PURPLE, event.pos, 10)
            pygame.display.update()


pygame.quit()

