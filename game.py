import pygame, sys, random
from settings import *
from player import Player
from platform import Platform
from coin import Coin
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()   

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.delta_time = 0

        self.state = 'menu'
        self.menu = Menu(self.screen)

        self.platforms = pygame.sprite.Group()
        self.player = Player(self.screen, 200, 200)

        self.create_platforms(8)  
       
        self.small_font = pygame.font.Font('fonts/Minecraft.ttf', 25)
        self.medium_font = pygame.font.Font('fonts/Minecraft.ttf', 30)
        self.big_font = pygame.font.Font('fonts/Minecraft.ttf', 70)

        self.hud = pygame.transform.scale_by(pygame.image.load('assets/hud.png').convert_alpha(), 4)
       
    # create 7 platforms
    def create_platforms (self, num):
        for id in range(1, num):
            self.platforms.add(Platform(id, self.screen, self.player))

    # play
    def play(self, delta_time):
        self.screen.fill(('#0099db'))

        self.player.update(delta_time, self.platforms)
        self.platforms.update(delta_time)

        self.player.draw() 
    
        self.platforms.draw(self.screen)

        self.screen.blit(self.hud, (0, 0))

        self.score_text = self.medium_font.render(f"Score: {round(self.player.score / 100)}", True, ('white'))
        self.coins_text = self.medium_font.render(f"Coins: {self.player.coins}", True, ('white'))
        self.screen.blit(self.score_text, (50, 20))
        self.screen.blit(self.coins_text, (screen_width - self.coins_text.get_width() - 50, 20))

    # main game loop
    def run(self):
        running = True
        while running:
            delta_time = self.clock.tick(60) / 1000.0
            pygame.display.set_caption(str(round(self.clock.get_fps(), 2)))

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if self.state == 'menu':
                        result = self.menu.handle_input(event)
                        if result == 'play':
                            self.state = 'play'
                        elif result == 'exit':
                            running = False
                    
                    # game events
                    if self.state == 'play':
                        # change dino
                        if event.key in (pygame.K_y, pygame.K_x, pygame.K_c, pygame.K_v):
                            colors = {pygame.K_y: 'blue', pygame.K_x: 'green', pygame.K_c: 'red', pygame.K_v: 'yellow'}
                            self.player.change_dino(colors[event.key])
                    
            # game logic
            if self.state == 'play':
                self.play(delta_time)
            elif self.state == 'menu':
                self.menu.draw()

            pygame.display.update()

        pygame.quit()
        sys.exit()

Game().run()
