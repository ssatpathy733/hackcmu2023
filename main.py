import pygame
import sys
import os

pygame.init()
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("name of game!")
clock = pygame.time.Clock()

exploring = True
while exploring:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exploring = False

    pygame.display.flip()
pygame.quit()