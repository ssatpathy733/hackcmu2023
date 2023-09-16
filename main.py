import pygame
import sys
import os

pygame.init()
window_size = (1200, 800)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("name of game!")
clock = pygame.time.Clock()
game_state = "main-page"
systems = ["system1", "system2", "system3", "system4", "system5", "earth"]

curr_system = "earth"

class SystemStats():
    def _init_(self, name, distance_km, mass_kg):
        self.name = name
        self.distance_km = distance_km
        self.mass_kg = mass_kg

class System():
    def _init_(self, name, linked_systems, found, system_stats):
        self.name = name
        self.linked_systems = linked_systems
        self.found = found
        self.system_stats = system_stats

#fill these in with actual graphics and relevant code 
def draw_main_page():
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(30, 30, 60, 60))

def draw_launch_page(system):
    pygame.draw.rect(window, (0, 255, 0), pygame.Rect(30, 30, 60, 60))

def draw_choose_speed():
    pygame.draw.rect(window, (0, 0, 255), pygame.Rect(30, 30, 60, 60))

def draw_landing_page(system):
    pygame.draw.rect(window, (200, 200, 0), pygame.Rect(30, 30, 60, 60))

def draw_system_stats(system):
    pygame.draw.rect(window, (0, 200, 200), pygame.Rect(30, 30, 60, 60))

def draw_handbook_page():
    pygame.draw.rect(window, (0, 200, 200), pygame.Rect(30, 30, 60, 60))

def draw_win_page():
    pygame.draw.rect(window, (200, 0, 200), pygame.Rect(30, 30, 60, 60))


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
            if event.key == pygame.K_l:
                game_state = "launching"
            if event.key == pygame.K_a:
                game_state = "landing"
            if event.key == pygame.K_c:
                game_state = "choose-speed"
            if event.key == pygame.K_h:
                game_state = "handbook"
            if event.key == pygame.K_w:
                game_state = "win"
            if event.key == pygame.K_m:
                game_state = "main-page"

    if game_state == "main-page":
        draw_main_page()

    if game_state == "launching":
        draw_launch_page(curr_system)

    if game_state == "choose-speed":
        draw_choose_speed()

    if game_state == "landing":
        draw_landing_page(curr_system)

    if game_state == "system-stats":
        draw_system_stats(curr_system)

    if game_state == "handbook":
        draw_handbook_page()
        
    if game_state == "win":
        draw_win_page()   

    pygame.display.flip()
pygame.quit()