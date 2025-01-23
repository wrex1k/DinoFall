import pygame, sys
from settings import screen_width, screen_height

class Game:
    def __init__(self):
        pygame.init()   

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("dino fall")

    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))

            pygame.display.update()

    pygame.quit()
    sys.exit()
