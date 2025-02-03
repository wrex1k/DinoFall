import pygame, random
from settings import *
from coin import Coin

class Platform(pygame.sprite.Sprite):
    zones = [140, 280, 420, 560, 700, 840, 980] # default y positions for the platforms
    colors = ['blue', 'green', 'red', 'yellow'] # list of possible colors for platforms

    def __init__(self, screen, player):
        super().__init__()
        # reference to screen and player
        self.player = player
        self.screen = screen

        # platform attributes
        self.speed = 120
        self.max_speed = 140
        self.set_atributes()

    # info about platform for debugging
    def get_info(self):
        print(f"Speed: {self.speed} | Color: {self.color}, Palette: {Platform.colors}, Speed: {self.speed}, Type: {self.type}, X: {self.x}, Y: {self.y}")

    # set atributes of the platform / respawn
    def set_atributes(self):
        self.color = self.random_color()
        self.type = random.choices(['small', 'medium'], weights=[1, 0.45])[0]
        self.image_path = f'assets/platforms/{self.color}/{self.type}.png'
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        self.mask = pygame.mask.from_surface(self.image)
        self.x = self.set_pos('x')
        self.y = self.set_pos('y')
        self.rect = self.image.get_rect(topleft=(self.x, self.y))   
        self.coin = self.spawn_coin(self.speed) 

    # spawn coin on the platform
    def spawn_coin(self, speed):
        num = random.randint(0, 100)
        # 40% chance of spawning a coin
        if num > 60:
            coin = Coin(self.screen, self.player, self.rect.topleft, self.rect.topright, speed)
            return coin

    # randomly pick and remove color from list, if empty refill
    def random_color(self):
        if len(Platform.colors) > 0:
            color = random.choice(Platform.colors)
            Platform.colors.remove(color)
        else:
            Platform.colors = ['blue', 'green', 'red', 'yellow']
            color = random.choice(Platform.colors)
        return color

    # set pos of the platform, default values if list not empty
    def set_pos(self, axis):
        if axis == 'x':
            num = random.randint(0, screen_width - self.image.get_width() - 30)
        elif axis == 'y':
            if len(Platform.zones) > 0:
                num = random.choice(Platform.zones)
                Platform.zones.remove(num)
            else:
                num = screen_width
        return num

    def update(self, delta_time):
        # if game over reset platform speed
        if get_game_over():
            self.speed = 120

        # increase speed of platform to max speed
        if self.speed < self.max_speed:
            self.speed += 0.01

        # update and draw the coin if exist
        if self.coin:
            self.coin.update(delta_time)
            self.coin.draw()

        # respawn the platform if out of screen
        if self.rect.bottom <= 50:
            self.set_atributes()

        # move the platform upwards
        self.rect.y -= self.speed * delta_time

        self.get_info()

    def draw(self):
        self.screen.blit(self.image, self.rect)

