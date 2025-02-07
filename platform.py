import pygame, random
from utils import *
from settings import * 
from coin import Coin

class Platform(pygame.sprite.Sprite):
    colors = ['blue', 'green', 'red', 'yellow'] # list of possible colors for platforms

    def __init__(self, screen, id, x, y):
        super().__init__()
        # reference to screen
        self.screen = screen
        # platform attributes
        self.id = id
        self.color = self.set_color()
        self.type = self.set_type()
        self.image_path = resource_path(f'assets/platforms/{self.color}/{self.type}.png')
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))   
        self.speed = 120
        self.max_speed = 200
        self.coin = self.spawn_coin(self.rect.width)

    # info about platform for debugging
    def get_info(self):
        print(f"ID: {self.id} | Speed: {self.speed} | Color: {self.color} |Speed: {round(self.speed, 2)}, Type: {self.type}, X: {self.rect.x}, Y: {self.rect.y}")

    # respawn the platform if out of screen
    def respawn(self):
        self.color = self.set_color()
        self.type = self.set_type()
        self.image_path = resource_path(f'assets/platforms/{self.color}/{self.type}.png')
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width//2 - self.image.get_width() - 30) + random.randint(0, screen_width//2)
        self.rect.y = 980
        self.coin = self.spawn_coin(self.rect.width)

    # randomly pick platform type with a 70 chance being small
    def set_type(self):
        return random.choices(['small', 'medium'], weights=[70, 30])[0]

    # spawn coin on the platform
    def spawn_coin(self, width):
        num = random.randint(0, 100)
        # 40% chance of spawning a coin
        if num > 60:
            left = self.rect.topleft[0]
            right = self.rect.topright[0] - 50
            coin_x = random.randint(left, right)
            coin_y = self.rect.top - 50 
            coin = Coin(self.screen, coin_x, coin_y, self.speed)
            return coin

    # randomly pick and remove color from list, if empty refill
    def set_color(self):
        if len(Platform.colors) == 0:
            Platform.colors = ['blue', 'green', 'red', 'yellow']
        
        color = random.choice(Platform.colors)
        Platform.colors.remove(color)
        return color
    
    def reset_platform_speed(self):
        self.speed = 120

    def update(self, delta_time):
        # increase speed of platform to max speed
        if self.speed < self.max_speed:
            self.speed += 0.01

        # update and draw the coin if exist
        if self.coin:
            self.coin.update_speed(self.speed)
            self.coin.update(delta_time)
            self.coin.draw()

        # respawn the platform if out of screen
        if self.rect.bottom <= 50:
            self.respawn()

        # move the platform upwards
        self.rect.y -= self.speed * delta_time

        #self.get_info()

    def draw(self):
        self.screen.blit(self.image, self.rect)

