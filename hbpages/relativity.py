from hbpages.events import EventHandler
from hbpages.ui import UI, Menu
from button.button import Button
from handbook import HandbookMenu
width = 1500
height = 844
train_x = (width * 0.1)
train_y = (height * 0.35)

WHITE = (255,255,255)
BLACK = (0,0,0)

flag = True


# characters
character = pygame.image.load("hbpages/assets/train.png")

# return to handbook page


class Relativity:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        UI.init(self)
        self.clock = pygame.time.Clock()
        EventHandler()
        hb_img = pygame.image.load('button/hb_button.png').convert_alpha()
        self.hb_button = Button(0, 0, hb_img, 0.1)
        self.menu = Menu(self)


    def run(self):
        self.running = True
        while self.running:
            self.screen.fill(BLACK)
            EventHandler.run()
            for e in EventHandler.events:
                if e.type == pygame.QUIT:
                    self.running = False

            self.menu.run()

            pygame.display.update()
            self.clock.tick(60)

            def add_train_at_location(x, y):
                self.screen.blit(character, (x, y))

            add_train_at_location(train_x, train_y)
            if self.hb_button.draw(self.screen):
                print("haha i press button")
                # i want this to bring me back to handbook menu... sammy pls help ;;-;;

            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Relativity()
    game.run()
