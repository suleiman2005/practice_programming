import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

rect(screen, (255, 255, 255), (0, 0, 500, 500))
circle(screen, (255, 255, 0), (250, 250), 100)
circle(screen, (0, 0, 0), (250, 250), 100, 1)
rect(screen, (0, 0, 0), (200, 300, 100, 20))
circle(screen, (255, 0, 0), (210, 220), 20)
circle(screen, (0, 0, 0), (210, 220), 20, 1)
circle(screen, (0, 0, 0), (210, 220), 10)
circle(screen, (255, 0, 0), (290, 220), 15)
circle(screen, (0, 0, 0), (290, 220), 15, 1)
circle(screen, (0, 0, 0), (290, 220), 10)
polygon(screen, (0, 0, 0), [(147, 168), (232, 211), (238, 199), (153, 156)])
polygon(screen, (0, 0, 0), [(351, 168), (273, 216), (269, 208), (347, 160)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()

