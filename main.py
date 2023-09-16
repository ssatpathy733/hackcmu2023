import pygame
import sys
import os

pygame.init()
window_size = (1200, 800)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("name of game!")
clock = pygame.time.Clock()
game_state = "landing-page"

class SystemStats:
    def __init__(self, name, distance_km, mass_kg):
        self.name = name
        self.distance_km = distance_km
        self.mass_kg = mass_kg

class System:
    def __init__(self, name, linked_systems, found, system_stats):
        self.name = name
        self.linked_systems = linked_systems
        self.found = found
        self.system_stats = system_stats

systems_stats_dict = {
    "Proxima Centauri": SystemStats("Proxima Centauri", 1000, 1000),
    "Wolf 359": SystemStats("Wolf 359", 1000, 1000),
    "System 3": SystemStats("System 3", 1000, 1000),
    "System 4": SystemStats("System 4", 1000, 1000),
    "System 5": SystemStats("System 5", 1000, 1000),
    "Earth": SystemStats("Earth", 1000, 1000)
}

systems_dict = {
    "Proxima Centauri": System("Proxima Centauri", [], False, systems_stats_dict["Proxima Centauri"]), 
    "Wolf 359": System("Wolf 359", [], False, systems_stats_dict["Wolf 359"]), 
    "System 3": System("System 3", [], False, systems_stats_dict["System 3"]), 
    "System 4": System("System 4", [], False, systems_stats_dict["System 4"]), 
    "System 5": System("System 5", [], False, systems_stats_dict["System 5"]), 
    "Earth": System("Earth", [], False, systems_stats_dict["Earth"])

}

curr_system = systems_dict["Earth"]
def all_found():
    for key in systems_dict:
        if (getattr(systems_dict[key], "found") == False):
            return False
    return True
        



#fill these in with actual graphics and relevant code
def draw_landing_page(system):
    # variables to create:
    # circle colour
    # outer circle ring colour
    myfont = pygame.font.SysFont("monospace", 30)
    #pygame.draw.rect(window, (200, 200, 0), pygame.Rect(30, 30, 60, 60))
    pygame.draw.circle(window, (171, 214, 212), (200, 350), 400, 0)
    pygame.draw.circle(window, (191, 224, 222), (200, 350), 400, 10)
    label = myfont.render(f"Welcome to {system}!", 1, (255, 255, 255))
    label_rect = label.get_rect(center=(1300, 800))
    window.blit(label, label_rect)


exploring = True
while exploring:
    clock.tick(60);

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exploring = False
        if event.type == pygame.KEYDOWN:

            #these will need to be changed to button presses in game once we get buttons done - everything should be via changing game-state tho!
            if event.key == pygame.K_q:
                exploring = False
                pygame.quit()
            if event.key == pygame.K_a:
                game_state = "landing"
            # if event.key == pygame.K_c:
            #     game_state = "choose-speed"
            # if event.key == pygame.K_h:
            #     game_state = "handbook"
            # if event.key == pygame.K_w:
            #     game_state = "win"
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


    if all_found():
        game_state = "win"
    pygame.display.flip()
pygame.quit()
