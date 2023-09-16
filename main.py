import pygame
import sys
import os

pygame.init()
window_size = (1200, 800)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("name of game!")
clock = pygame.time.Clock()
game_state = "main-page"

def draw_main_page():
    pygame.draw.rect(window, (255, 9, 9), pygame.Rect(30, 30, 60, 60))


exploring = True
while exploring:
    clock.tick(60);

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exploring = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exploring = False
                pygame.quit()

    if game_state == "main-page":
        draw_main_page()
    if game_state == "launching":
        pass
    if game_state == "choose-speed":
        pass
    if game_state == "landing":
        pass
    if game_state == "handbook":
        pass
    if game_state == "win":
        pass   

    pygame.display.flip()
pygame.quit()