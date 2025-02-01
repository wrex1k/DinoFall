import pygame, random

class Coin(pygame.sprite.Sprite):
    def __init__(self, screen, topleft, topright, speed):
        super().__init__()
        self.screen = screen
        self.scale = 2
        self.spritesheet = pygame.image.load('assets/coins/coin.png').convert_alpha()
        self.x = random.randint(topleft[0], topright[0])
        self.y = topleft[1] - 50
        self.collect = False
        self.speed = speed

        self.frames = []
        self.load_animation()

        self.frame_index = 0
        self.animation_speed = 0.1
        self.animation_time = 0

    def load_animation(self):
        for i in range(8):
            frame_rect = pygame.Rect(i * 20, 0, 20, 20)
            frame = self.spritesheet.subsurface(frame_rect)
            frame = pygame.transform.scale_by(frame, (self.scale, self.scale))
            self.rect = frame.get_rect(topleft=(self.x, self.y))
            self.mask = pygame.mask.from_surface(frame)
            self.frames.append(frame)

    def update(self, delta_time):
        self.rect.y -= self.speed * delta_time
        self.animation_time += delta_time

        if self.animation_time >= self.animation_speed:
            self.animation_time = 0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.frame_index = 0

        self.image = self.frames[self.frame_index]

    def draw(self):
        if not self.collect:
            self.screen.blit(self.image, self.rect)
