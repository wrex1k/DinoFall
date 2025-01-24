import pygame
from settings import screen_width, screen_height

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(x, y, 48, 48)
        self.direction = 'right'
        self.speed = 4
        self.gravity = 3
        self.hp = 3

        self.change_dino('blue')
        self.current_animation = self.animations['idle_right']
        self.animation_frame = 0

    def change_dino(self, color):
        path = 'assets/sheets/'
        dinos = {
            'blue': pygame.image.load(f'{path}DinoSprites - doux.png').convert_alpha(),
            'red': pygame.image.load(f'{path}DinoSprites - mort.png').convert_alpha(),
            'yellow': pygame.image.load(f'{path}DinoSprites - tard.png').convert_alpha(),
            'green': pygame.image.load(f'{path}DinoSprites - vitatest.png').convert_alpha(),
        }
        self.image = dinos[color]

        self.animations = {
            'idle_right': self.load_animation(0, 3),
            'idle_left': self.load_animation(0, 3, flip=True),
            'walk_right': self.load_animation(3, 8),
            'walk_left': self.load_animation(3, 8, flip=True),
            'dead': self.load_animation(15, 17)
        }

    def draw_hitbox(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)

    def load_animation(self, start, stop, flip=False):
        frames = []
        for i in range(start, stop):
            frame = self.image.subsurface(pygame.Rect(i * 24, 0, 24, 24))
            if flip:
                frame = pygame.transform.flip(frame, True, False)
            frames.append(frame)
        return frames

    def update(self):
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = 'left'
            moving = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = 'right'
            moving = True

        #self.rect.y += self.gravity

        if moving:
            self.current_animation = self.animations[f'walk_{self.direction}']
        else:
            self.current_animation = self.animations[f'idle_{self.direction}']

        self.animation_frame += 0.1
        if self.animation_frame >= len(self.current_animation):
            self.animation_frame = 0

        self.image = self.current_animation[int(self.animation_frame)]

    def draw(self):
        self.screen.blit(pygame.transform.scale(self.image, (48*5, 48*5)), (self.rect.x, self.rect.y))