import pygame
# naming system:
# from directory.fileName import className
from button.button import Button
from hbpages.relativity import relativity

pygame.init()

# set up screen
scr_width, scr_height = 1500, 844
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Explorer's Handbook")

# import images for buttons
# MAKE SURE FILE PATH NAMES ARE CORRECT
spec_rel_img = pygame.image.load('button/rel_button.png').convert_alpha()
quit_img = pygame.image.load('button/mainmen_button.png.png').convert_alpha()

# make buttons
spec_rel_button = Button(160, 250, spec_rel_img, 0.1)
quit_button = Button(400, 250, quit_img, 0.1)

# game variables
hb_open = False

# define fonts
font = pygame.font.SysFont("comicsans", 40)

# define colors
text_col = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True

while run:
    screen.fill((52, 78, 91))

    # special relativity
    if spec_rel_button.draw(screen):
        hb_page = relativity()
        hb_page.run()

    if quit_button.draw(screen):
        run = False
    # event handler

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hb_open = True
        if event.type == pygame.QUIT:
            run = False
    #

    pygame.display.update()

pygame.quit()

