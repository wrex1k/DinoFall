import pygame, random
from settings import screen_width, screen_height
from coin import Coin

class Platform(pygame.sprite.Sprite):
    zones = [140, 280, 420, 560, 700, 840] # default y positions for the platforms
    colors = ['blue', 'green', 'red', 'yellow']

    def __init__(self, id, screen, player):
        super().__init__()
        self.player = player
        self.id = id
        self.screen = screen
        self.speed = 100
        self.set_atributes()

    # info about platform
    def get_info(self):
        print(f"id: {self.id}, Color: {self.color}, Palette: {Platform.colors}, Speed: {self.speed}, Type: {self.type}, X: {self.x}, Y: {self.y}")
    
    # set atributes of the platform / respawn
    def set_atributes(self):
        self.color = self.random_color()
        self.type = random.choices(['small', 'medium'], weights=[1, 0.4])[0]
        self.image_path = f'assets/platforms/{self.color}/{self.type}.png'
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 3)
        self.mask = pygame.mask.from_surface(self.image)
        self.x = self.set_pos('x')
        self.y = self.set_pos('y')
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.coin = self.spawn_coin()

    # spawn coin on the platform
    def spawn_coin(self):
        num = random.randint(0, 100)
        if num > 50 and self.type == 'medium':
            coin = Coin(self.screen, self.rect.topleft, self.rect.topright, self.speed)
            return coin

    # set platform color
    def random_color(self):
        if len(Platform.colors) > 0:
            color = random.choice(Platform.colors)
            Platform.colors.remove(color)
        else:
            Platform.colors = ['blue', 'green', 'red', 'yellow']
            color = random.choice(Platform.colors)
        return color

    # set pos of the platform 
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

    # update
    def update(self, delta_time):
        if self.coin:
            if self.coin.rect.colliderect(self.player.rect) and not self.coin.collect:
                self.player.coins += 1
                self.coin.collect = True
            self.coin.update(delta_time)
            self.coin.draw()
        if self.rect.bottom <= 0:
            self.set_atributes()

        self.rect.y -= self.speed * delta_time



    def draw(self):
    # draw
        self.screen.blit(self.image, self.rect)

