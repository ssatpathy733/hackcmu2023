import pygame
import sys
import os
from button.button import Button
import SystemEntries
from SystemEntries import System
from SystemEntries import SystemStats
from SystemEntries import systems_dict
from SystemEntries import systems_stats_dict



pygame.init()
window_size = (1500 , 844)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("name of game!")
clock = pygame.time.Clock()
click_timer = 0

#button setup:
cont_img = pygame.image.load('button/cont_button.png').convert_alpha()
earth_img = pygame.image.load('button/earth_button.png').convert_alpha()
hb_img = pygame.image.load('button/hb_button.png').convert_alpha()
hd_img = pygame.image.load('button/hd_button.png').convert_alpha()
kep_img = pygame.image.load('button/kep_button.png').convert_alpha()
launch_img = pygame.image.load('button/launch_button.png').convert_alpha()
mainmen_img = pygame.image.load('button/mainmen_button.png').convert_alpha()
playag_img = pygame.image.load('button/playag_button.png').convert_alpha()
proxcent_img = pygame.image.load('button/proxcent_button.png').convert_alpha()
rel_img = pygame.image.load('button/rel_button.png').convert_alpha()
trap_img = pygame.image.load('button/trap_button.png').convert_alpha()
wolf_img = pygame.image.load('button/wolf_button.png').convert_alpha()


# make buttons
cont_button = Button(160, 250, cont_img, 0.1);
earth_button = Button(160, 250, earth_img, 0.1);
hb_button = Button(300, 250, hb_img, 0.1);
hd_button = Button(160, 250, hd_img, 0.1);
kep_button = Button(160, 250, kep_img, 0.1);
launch_button = Button(300, 500, launch_img, 0.3);
mainmen_button = Button(160, 250, mainmen_img, 0.1);
playag_button = Button(160, 250, playag_img, 0.1);
proxcent_button = Button(160, 250, proxcent_img, 0.1);
rel_button = Button(160, 250, rel_img, 0.1);
trap_button = Button(160, 250, trap_img, 0.1);
wolf_button = Button(160, 250, wolf_img, 0.1);


# define fonts
font = pygame.font.SysFont("comicsans", 40)

# define colors
text_col = (255, 255, 255)


curr_system = systems_dict["Earth"]
display_system = systems_dict["Earth"]
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
    window.fill((52, 78, 91))

    launch_button.draw(window, 300, 600)
    hb_button.draw(window, 350, 250)

def draw_launch_page(system):
    window.fill((52, 78, 91))

    earth_button.draw(window, 150, 600)
    hd_button.draw(window, 150, 500)
    kep_button.draw(window, 150, 400)
    proxcent_button.draw(window, 150, 300)
    trap_button.draw(window, 150, 200)
    wolf_button.draw(window, 150, 100)

def draw_choose_speed():
    window.fill((52, 78, 91))

    cont_button.draw(window, 1100, 650)

def draw_landing_page(system):
    window.fill((52, 78, 91))

    cont_button.draw(window, 1100, 650)

def draw_system_stats(system):
    window.fill((52, 78, 91))

    hb_button.draw(window, 100, 100)

def draw_relativity():
    window.fill((52, 78, 91))

    hb_button.draw(window, 100, 100)

def draw_handbook_page():
    window.fill((52, 78, 91))

    mainmen_button.draw(window, 100, 100)
    rel_button.draw(window, 500, 100)
    earth_button.draw(window, 200, 200)
    hd_button.draw(window, 400, 200)
    kep_button.draw(window, 600, 200)
    proxcent_button.draw(window, 800, 200)
    trap_button.draw(window, 1000, 200)
    wolf_button.draw(window, 1200, 200)

def draw_win_page():
    window.fill((52, 78, 91))
    playag_button.draw(window, 700, 100)


exploring = True
while exploring:
    print("game state: " + game_state)
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
            #leaving this here for debugging purposes...
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
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click_timer == 0:
            print("pressing something")
            click_timer = 50 #to prevent two buttons on different screens from being pressed in one click
    #actual button press commands!
            if hb_button.isClicked(pygame.mouse.get_pos()):
                print("clicked handbook")
                game_state = "handbook"

            if mainmen_button.isClicked(pygame.mouse.get_pos()):
                print("clicked main page")
                game_state = "main-page"

            if launch_button.isClicked(pygame.mouse.get_pos()):
                curr_system = systems_dict["Earth"]
                game_state = "launching"

            if playag_button.isClicked(pygame.mouse.get_pos()):
                game_state = "main-page"
                for key in systems_dict:
                    setattr(systems_dict[key], "found", False)

            if cont_button.isClicked(pygame.mouse.get_pos()):
                if game_state == "choose-speed":
                    game_state = "landing"
                elif game_state == "landing":
                    game_state = "launching"

            if earth_button.isClicked(pygame.mouse.get_pos()) and game_state == "launching":
                game_state = "choose-speed"
                curr_system = systems_dict["Earth"]

            if hd_button.isClicked(pygame.mouse.get_pos()) and game_state == "launching":
                game_state = "choose-speed"
                curr_system = systems_dict["HD 189733b"]

            if kep_button.isClicked(pygame.mouse.get_pos()) and game_state == "launching":
                game_state = "choose-speed"
                curr_system = systems_dict["Kepler-62"]

            if proxcent_button.isClicked(pygame.mouse.get_pos()) and game_state == "launching":
                game_state = "choose-speed"
                curr_system = systems_dict["Proxima Centauri"]

            if trap_button.isClicked(pygame.mouse.get_pos()) and game_state == "launching":
                game_state = "choose-speed"
                curr_system = systems_dict["TRAPPIST-1"]

            if wolf_button.isClicked(pygame.mouse.get_pos()) and game_state == "launching":
                game_state = "choose-speed"
                curr_system = systems_dict["Wolf 359"]

            


            if earth_button.isClicked(pygame.mouse.get_pos()) and game_state == "handbook":
                game_state = "system-stats"
                display_system = systems_dict["Earth"]

            if hd_button.isClicked(pygame.mouse.get_pos()) and game_state == "handbook":
                game_state = "system-stats"
                display_system = systems_dict["HD 189733b"]

            if kep_button.isClicked(pygame.mouse.get_pos()) and game_state == "handbook":
                game_state = "system-stats"
                display_system = systems_dict["Kepler-62"]

            if proxcent_button.isClicked(pygame.mouse.get_pos()) and game_state == "handbook":
                game_state = "system-stats"
                display_system = systems_dict["Proxima Centauri"]

            if trap_button.isClicked(pygame.mouse.get_pos()) and game_state == "handbook":
                game_state = "system-stats"
                display_system = systems_dict["TRAPPIST-1"]

            if wolf_button.isClicked(pygame.mouse.get_pos()) and game_state == "handbook":
                game_state = "system-stats"
                display_system = systems_dict["Wolf 359"]

    if all_found():
        game_state = "win"
        

    #game state screen changes
    if game_state == "main-page":
        draw_main_page()

    if game_state == "launching":
        draw_launch_page(curr_system)

    if game_state == "choose-speed":
        draw_choose_speed()

    if game_state == "landing":
        draw_landing_page(curr_system)
        setattr(curr_system, "found", True)

    if game_state == "system-stats":
        draw_system_stats(display_system)

    if game_state == "handbook":
        draw_handbook_page()
        
    if game_state == "win":
        draw_win_page()   

    pygame.display.flip()
    if click_timer > 0:
        click_timer -= 1
print(all_found())
pygame.quit()
