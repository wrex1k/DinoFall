import pygame
from settings import screen_width, screen_height

class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, color, type, x, y):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(f'assets/platforms/{color}/{type}.png').convert_alpha()
        self.scale = [3, 3] if type == 'small' else [6, 3] if type == 'medium' else None
        self.rect = pygame.Rect(x, y, 48*self.scale[0], 16.0*self.scale[1])
        self.speed = 100

    def update(self, delta_time):
        self.rect.y -= self.speed * delta_time

        if self.rect.bottom <= 0:
            self.rect.top = screen_height


    def draw_hitbox(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

    def draw(self):
        self.draw_hitbox()
        scaled_image = pygame.transform.scale(self.image, (48*self.scale[0], 16*self.scale[1]))
        self.screen.blit(scaled_image, self.rect) 
