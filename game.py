import pygame, sys, random
from audiomanager import *
from settings import * 
from utils import *
from menu import Menu
from player import Player
from platform import Platform

class Game:
    def __init__(self):
        pygame.init()   
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('DinoFall')
        self.clock = pygame.time.Clock()
        self.delta_time = 0

        #* initialized menu, platforms and player
        self.menu = Menu(self.screen)
        self.platforms = self.create_platforms(7)
        self.player = Player(self.screen, self.platforms[2].rect.centerx, self.platforms[2].rect.top - 100, self.platforms[2].color)

    # create new platforms and reset player position
    def reset_game(self):
        self.platforms = self.create_platforms(7)
        self.player.reset_player(self.platforms[2].rect.centerx, self.platforms[2].rect.top - 100, self.platforms[2].color)
        play_music('8-bit-game')
        set_game_state('play')

    # create platforms and return as a list
    def create_platforms(self, num):
        list = []
        y = [140, 280, 420, 560, 700, 840, 980]
        for id in range(1, num + 1):
            x = random.randint(50, screen_width - 300)
            platform = Platform(self.screen, id, x, y.pop(0))
            list.append(platform)
        return list
    
    def draw_game_hud(self):
        # initialized UI elements
        self.hud_game = get_image('hud_game', 4)
        # initialized game text 
        self.score_text = medium_font.render(f"Score: {int(self.player.score / 10)}", True, ('white'))
        self.coins_text = medium_font.render(f"Coins: {(self.player.coins)}", True, ('white'))
        # display game HUD with text
        self.screen.blit(self.hud_game, (0, 0))
        self.screen.blit(self.score_text, (50, 20))
        self.screen.blit(self.coins_text, (screen_width - self.coins_text.get_width() - 50, 20))

    def draw_game_over(self):
        self.screen.fill(('#0099db'))
        draw_clouds(self.screen)

        # initialized UI elements
        self.controls_game = get_image('hud_controls', 5)
        self.controls_game_rect = self.controls_game.get_rect(center=(screen_width / 2, screen_height / 2))
        # inizialized text
        self.game_over_text = big_font.render(f"Game Over", True, ('white'))
        self.score_text = medium_font.render(f"Score: {int(self.player.score / 10)}", True, ('white'))
        self.max_score_text = medium_font.render(f"High score: {int(self.player.max_score / 10)}", True, ('white'))
        self.coins_text = medium_font.render(f"Coins: {(self.player.coins)}", True, ('white'))
        self.direction_text = medium_font.render("R - Restart / ESC - Menu", True, ('white'))
        
        # display game over UI
        self.screen.blit(self.controls_game, self.controls_game_rect)
        # display game over texts at different Y positions
        y = [220, 300, 350, 400, 500]
        for text in [self.game_over_text, self.score_text, self.max_score_text, self.coins_text, self.direction_text]:
            text_rect = text.get_rect(center=(screen_width / 2 - text.get_height() / 2, y.pop(0)))
            self.screen.blit(text, text_rect)

    def game(self, delta_time):
        self.screen.fill(('#0099db'))
        draw_clouds(self.screen)

        self.player.update(delta_time, self.platforms)
            
        for platform in self.platforms:
            platform.update(delta_time)
            platform.draw()

        self.player.draw()

        self.draw_game_hud()

    #* main game loop
    def run(self):
        running = True
        while running:
            delta_time = self.clock.tick(60) / 1000.0
            game_state = get_game_state()
            
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if game_state == 'menu':
                        self.menu.handle_menu_input(event)
                    if game_state == 'controls':
                        self.menu.handle_controls_input(event)
                    if game_state == 'gameover':
                        if event.key == pygame.K_r:
                            self.reset_game()
                        if event.key == pygame.K_ESCAPE:
                            set_game_state('menu')
                            if get_music(): play_music('menu')
                            

            # game logic based on state
            if game_state == 'play':
                self.game(delta_time)
            elif game_state == 'controls':
                self.menu.draw_controls()
            elif game_state == 'menu':
                self.menu.draw_menu()
            elif game_state == 'gameover':
                self.draw_game_over()
            elif game_state == 'exit':
                running = False


            pygame.display.update()

        pygame.quit()
        sys.exit()

Game().run()
