import pygame
from settings import *
from menu import Menu

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

menu = Menu(screen)

run = True
while run:
    
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    menu.update()

    pygame.display.update()

pygame.quit()