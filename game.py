import pygame, sys, random
from settings import *
from player import Player
from platform import Platform
from coin import Coin
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()   
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.delta_time = 0

        # initialize state
        self.state = 'menu'

        # initialized menu, player and platforms
        self.menu = Menu(self.screen)
        self.player = Player(self.screen, 200, 200)
        self.platforms = pygame.sprite.Group()
        self.create_platforms(7)  

        # UI elements
        self.hud_game = get_image('hud_game', 4)
        self.controls_game = get_image('hud_controls', 5)
        self.controls_game_rect = self.controls_game.get_rect(center=(screen_width / 2, screen_height / 2))

    # create platforms object and add to group
    def create_platforms(self, num):
        for id in range(0, num):
            platform = Platform(self.screen, self.player)      
            self.platforms.add(platform)

    def play(self, delta_time):
        # redrawing the screen with clouds
        self.screen.fill(('#0099db'))
        self.menu.draw_clouds()

        if not self.player.dead:
            # update and draw player and platforms
            self.player.update(delta_time, self.platforms)
            self.platforms.update(delta_time)
            self.platforms.draw(self.screen)
            self.player.draw()

            # draw game hud
            self.screen.blit(self.hud_game, (0, 0))
            self.score_text = medium_font.render(f"Score: {int(self.player.score / 10)}", True, ('white'))
            self.coins_text = medium_font.render(f"Coins: {(self.player.coins)}", True, ('white'))
            self.screen.blit(self.score_text, (50, 20))
            self.screen.blit(self.coins_text, (screen_width - self.coins_text.get_width() - 50, 20))
        else:
            # inizialized game over text
            self.game_over_text = big_font.render(f"Game Over", True, ('white'))
            self.score_text = medium_font.render(f"Score: {int(self.player.score / 10)}", True, ('white'))
            self.max_score_text = medium_font.render(f"High score: {int(self.player.max_score / 10)}", True, ('white'))
            self.coins_text = medium_font.render(f"Coins: {(self.player.coins)}", True, ('white'))
            self.direction_text = medium_font.render("R - Restart / ESC - Menu", True, ('white'))

            # draw game over hud
            self.screen.blit(self.controls_game, self.controls_game_rect)
            
            # display game over texts at different Y positions
            y = [220, 300, 350, 400, 500]
            for text in [self.game_over_text, self.score_text, self.max_score_text, self.coins_text, self.direction_text]:
                text_rect = text.get_rect(center=(screen_width / 2 - text.get_height() / 2, y.pop(0)))
                self.screen.blit(text, text_rect)

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
                    # handle menu inputs
                    if self.state == 'menu':
                        result = self.menu.handle_input(event)
                        if result == 'play':
                            self.state = 'play'
                        elif result == 'controls':
                            self.state = 'controls'
                        elif result == 'exit':
                            running = False

                    # show controls screen
                    if self.state == 'controls':
                        self.menu.draw_controls()
                        if event.key == pygame.K_ESCAPE:
                            self.state = 'menu'

                    # game events
                    if self.state == 'play':
                        # change dino
                        if event.key in (pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f):
                            colors = {pygame.K_a: 'blue', pygame.K_s: 'green', pygame.K_d: 'red', pygame.K_f: 'yellow'}
                            self.player.change_dino(colors[event.key])
                        # return to menu
                        if event.key == pygame.K_ESCAPE:
                            self.state = 'menu'
                            stop_music()
                            set_playing(False)
                        # restart game
                        if event.key == pygame.K_r:
                            if get_game_over():
                                if not get_playing(): play_music('8-bit-game') and set_playing(True)
                                self.player.restart_player()
                                self.state = 'play'

                    
            # game logic based on state
            if self.state == 'play':
                self.play(delta_time)
            elif self.state == 'controls':
                self.menu.draw_controls()
            elif self.state == 'menu':
                self.menu.draw_menu()
                if get_music() and not get_playing():
                    play_music('menu')
                    set_playing(True)

            pygame.display.update()

        pygame.quit()
        sys.exit()

Game().run()
