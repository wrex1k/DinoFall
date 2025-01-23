import pygame, sys
from settings import screen_width, screen_height
from player import Player

class Game:
    def __init__(self):
        pygame.init()   
        pygame.display.set_caption("dino fall")

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        
        self.player = Player(self.screen, screen_width // 2 - 24, 0)
    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            self.screen.fill((0, 120, 220))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.player.update()
            self.player.draw()

            pygame.display.update()

        pygame.quit()
        sys.exit()

Game().run()
