import pygame, sys, random
from settings import screen_width, screen_height
from player import Player
from platform import Platform

class Game:
    def __init__(self):
        pygame.init()   

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.delta_time = 0

        self.player = Player(self.screen, 0, 0)
        self.platforms = pygame.sprite.Group()

        self.font = pygame.font.Font('assets/fonts/Minecraft.ttf', 30)
        self.text = self.font.render(f"test", True, (0, 0, 0))

        self.create_platforms(6)

    def create_platforms (self, num):
        for id in range(1, num):
            self.platforms.add(Platform(self.screen, self.platforms))

    def run(self):
        running = True
        while running:
            delta_time = self.clock.tick(60) / 1000.0
            pygame.display.set_caption(str(round(self.clock.get_fps(), 2)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_y, pygame.K_x, pygame.K_c, pygame.K_v):
                        colors = {pygame.K_y: 'yellow', pygame.K_x: 'red', pygame.K_c: 'blue', pygame.K_v: 'green'}
                        self.player.change_dino(colors[event.key])

            self.screen.fill((255, 255, 255))
           
            self.player.update(delta_time, self.platforms)
            self.platforms.update(delta_time)
            self.player.draw() 
            self.platforms.draw(self.screen)

            self.screen.blit(self.text, (0, 0))

            pygame.display.update()

        pygame.quit()
        sys.exit()

Game().run()
