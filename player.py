import pygame
from settings import screen_width, screen_height

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.scale = 3
        self.rect = pygame.Rect(x, y, 24*self.scale, 24*self.scale-10)
        self.direction = 'right'
        self.speed = 200
        self.velocity_y = 3
        self.gravity = 2
        self.hp = 3

        self.dinos = ['blue', 'red', 'yellow', 'green']
        self.current_color = 'blue'
        self.load_animations(self.current_color)

        self.current_animation = self.animations['idle_right']
        self.animation_frame = 0

        self.image = self.current_animation[0]
        self.mask = pygame.mask.from_surface(self.image)

    def get_info(self):
        print(f"x: {self.rect.x} | y: {self.rect.y} | G: {self.gravity} | velocity_y: {self.velocity_y} | on_platform: {self.on_platform}")

    def load_animations(self, color):
        path = f'assets/sheets/DinoSprites - {color}.png'
        spritesheet = pygame.image.load(path).convert_alpha()

        self.animations = {
            'idle_right': self.load_animation(spritesheet, 0, 3),
            'idle_left': self.load_animation(spritesheet, 0, 3, flip=True),
            'walk_right': self.load_animation(spritesheet, 4, 8),
            'walk_left': self.load_animation(spritesheet, 4, 8, flip=True),
            'dead': self.load_animation(spritesheet, 15, 17),
        }

    def load_animation(self, spritesheet, start, stop, flip=False):
        frames = []
        for i in range(start, stop):
            frame = spritesheet.subsurface(pygame.Rect(i * 24, 0, 24, 24))
            if flip:
                frame = pygame.transform.flip(frame, True, False)
            frame = pygame.transform.scale_by(frame, (self.scale, self.scale))
            frames.append(frame)
        return frames

    def change_dino(self, color):
        if color != self.current_color:
            self.current_color = color
            self.load_animations(color)
            self.current_animation = self.animations['idle_right']

    def update(self, delta_time, platforms):
        keys = pygame.key.get_pressed()
        moving = False
        self.on_platform = False
        old_x = self.rect.x  

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed * delta_time
            self.direction = 'left'
            moving = True
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed * delta_time
            self.direction = 'right'
            moving = True

        if not self.on_platform:
            self.velocity_y += self.gravity * delta_time
            self.rect.y += self.velocity_y
            
        for platform in platforms:
            if pygame.sprite.collide_mask(self, platform):
                if self.rect.bottom <= platform.rect.top + 10:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_platform = True
                    self.rect.y -= platform.speed * delta_time
                    break
                else:
                    self.rect.x = old_x
            else:
                self.velocity_y = 3

        if self.rect.top >= self.screen.get_height(): 
            self.rect.bottom = 0

        if moving:
            self.current_animation = self.animations[f'walk_{self.direction}']
        else:
            self.current_animation = self.animations[f'idle_{self.direction}']

        self.animation_frame += 5 * delta_time
        if self.animation_frame >= len(self.current_animation):
            self.animation_frame = 0

        self.image = self.current_animation[int(self.animation_frame)]

        self.get_info()

    def draw(self):
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
        self.screen.blit(self.image, self.rect)
