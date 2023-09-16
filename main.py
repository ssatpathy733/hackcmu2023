import pygame
import sys
from events import EventHandler
from ui import UI, Menu

train = pygame.image.load("assets/train.png")

width = 1500
height = 844
train_x = (width * 0.1)
train_y = (height * 0.35)

WHITE = (255,255,255)
BLACK = (0,0,0)

flag = True


# characters
character = pygame.image.load("assets/train.png")

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        UI.init(self)
        self.clock = pygame.time.Clock()
        EventHandler()


        self.menu = Menu(self)
    def run(self):
        self.running = True
        while self.running:
            EventHandler.run()
            for e in EventHandler.events:
                if e.type == pygame.QUIT:
                    self.running = False

            self.menu.run()

            pygame.display.update()
            self.clock.tick(60)

            def add_train_at_location(x, y):
                self.screen.blit(character, (x, y))

            self.screen.fill(BLACK)
            add_train_at_location(train_x, train_y)
            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()


