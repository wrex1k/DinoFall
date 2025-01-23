import pygame, sys
from settings import screen_width, screen_height

class Game:
    def __init__(self):
        pygame.init()   

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("dino fall")

    def run(self):
        running = True
        self.clock.tick(60)
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill('blue')

            pygame.display.update()

        pygame.quit()
        sys.exit()

Game().run()
