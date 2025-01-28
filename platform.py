import pygame, random
from settings import screen_width, screen_height

class Platform(pygame.sprite.Sprite):
    zones = [140, 280, 420, 560, 700]

    def __init__(self, surface, group):
        super().__init__()
        self.surface = surface
        self.color = random.choice(['green'])
        self.type = 'small' if random.randint(1, 3) % 2 == 1 else 'medium'
        self.image = pygame.image.load(f'assets/platforms/{self.color}/{self.type}.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, (3, 3))
        self.x = random.randint(0, screen_width - self.image.get_width())
        self.y = self.set_y()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 80
        self.group = group

    def get_info(self):
        print(f"Color: {self.color}, Type: {self.type}, X: {self.x}, Y: {self.y}")

    def set_y(self):
        if len(Platform.zones) > 0:
            num = random.choice(Platform.zones)
            self.zones.remove(num)
        else:
            num = 700
        return num

    def create_platform(self):
        platform = Platform(self.surface, self.group)
        platform.get_info()
        self.group.add(platform)
    
    def update(self, delta_time):        
        self.rect.y -= self.speed * delta_time

        if self.rect.bottom <= 0:
            self.kill()
            self.create_platform()

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(self.image, self.rect)

