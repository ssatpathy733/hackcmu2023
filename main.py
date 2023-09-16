import pygame
import sys
import os
from button.button import Button

pygame.init()
window_size = (1200, 800)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("name of game!")
clock = pygame.time.Clock()

#button setup:
spec_rel_img = pygame.image.load('button/spec_rel_button.png').convert_alpha()
main_menu_img = pygame.image.load('button/main menu.png').convert_alpha()

# make buttons
spec_rel_button = Button(160, 250, spec_rel_img, 0.1)
main_menu_button = Button(400, 250, main_menu_img, 0.1)


# define fonts
font = pygame.font.SysFont("comicsans", 40)

# define colors
text_col = (255, 255, 255)



class SystemStats:
    def __init__(self, name, distance_km, num_planets, entry):
        self.name = name
        self.distance_km = distance_km
        self.num_planets = num_planets
        self.entry = entry

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
game_state = "main-page"

def all_found():
    for key in systems_dict:
        if (getattr(systems_dict[key], "found") == False):
            return False
    return True


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))


#fill these in with actual graphics and relevant code 
def draw_main_page():
    print("drawing main page!")
    main_menu_button.draw(window);
    spec_rel_button.draw(window);

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
    window.fill((52, 78, 91))
    clock.tick(60);

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exploring = False
        if event.type == pygame.KEYDOWN:

            #these will need to be changed to button presses in game once we get buttons done - everything should be via changing game-state tho!
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

    #actual button press commands!
    if spec_rel_button.isClicked():
        print("spec rel clicked!")
        game_state = "handbook"

    if main_menu_button.isClicked():
        print("main menu clicked!")
        game_state = "main-page"

    #game state screen changes
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