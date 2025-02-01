import pygame
from settings import screen_width, screen_height

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.scale = 3
        self.rect = pygame.Rect(x, y, 24*self.scale, 24*self.scale-10)
        self.direction = 'right'
        self.speed = 220
        self.velocity_y = 0
        self.gravity = 1.5
        self.score = 1
        self.coins = 0

        self.dinos = ['blue', 'red', 'yellow', 'green']
        self.current_color = 'blue'

        self.all_animations = {color: self.load_animations(color) for color in self.dinos}

        self.animations = self.all_animations[self.current_color]
        self.current_animation = self.animations['idle_right']
        self.animation_frame = 0

        self.image = self.current_animation[0]
        self.mask = pygame.mask.from_surface(self.image)

    def get_info(self):
        print(f"x: {self.rect.x} | y: {self.rect.y} | G: {self.gravity} | velocity_y: {self.velocity_y} | on_platform: {self.on_platform} | Correct color: {self.correct_color} | speed: {self.speed}")

    # load all animations for each direction at once by color
    def load_animations(self, color):
        path = f'assets/sheets/DinoSprites - {color}.png'
        spritesheet = pygame.image.load(path).convert_alpha()

        return {
            'idle_right': self.load_frames(spritesheet, 0, 3),
            'idle_left': self.load_frames(spritesheet, 0, 3, flip=True),
            'walk_right': self.load_frames(spritesheet, 4, 8),
            'walk_left': self.load_frames(spritesheet, 4, 8, flip=True),
            'dead': self.load_frames(spritesheet, 15, 17),
        }

    # load frames from spritesheet in right size than scale it, if animation left, flip frame
    def load_frames(self, spritesheet, start, stop, flip=False):
        frames = []
        for i in range(start, stop):
            frame = spritesheet.subsurface(pygame.Rect(i * 24, 0, 24, 24))
            if flip:
                frame = pygame.transform.flip(frame, True, False)
            frame = pygame.transform.scale_by(frame, (self.scale, self.scale))
            frames.append(frame)
        return frames

    # change color, animation of dino, set default animation
    def change_dino(self, color):
        if color in self.all_animations:
            self.current_color = color
            self.animations = self.all_animations[color]  
            self.current_animation = self.all_animations[color]['idle_right']

    def update(self, delta_time, platforms):
        self.on_platform = False
        old_x = self.rect.x  
        moving = False

        # update score
        self.score += 1

        # input handler
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed * delta_time
            self.direction = 'left'
            moving = True
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed * delta_time
            self.direction = 'right'
            moving = True

        # collision detection by mask and apply gravity 
        for platform in platforms:
            if pygame.sprite.collide_mask(self, platform):
                
                # speed handler
                self.speed = 220 if platform.color == self.current_color else 100
                
                # collision detection
                if self.rect.bottom <= platform.rect.top + 10:
                    self.rect.bottom = platform.rect.top 
                    self.velocity_y = 0
                    self.on_platform = True
                    break
                else:
                    self.rect.y -= self.speed * delta_time
                    self.rect.x = old_x

            if not self.on_platform:
                self.velocity_y += self.gravity * delta_time
                
        # apply gravity
        self.rect.y += self.velocity_y

        # velocity limit 5
        if not self.on_platform:
            self.velocity_y = min(self.velocity_y, 5)

        # reset y position
        if self.rect.bottom >= screen_height:
            self.rect.bottom = 0

        if moving:
            self.current_animation = self.animations[f'walk_{self.direction}']
        else:
            self.current_animation = self.animations[f'idle_{self.direction}']

        self.animation_frame += 5 * delta_time
        if self.animation_frame >= len(self.current_animation):
            self.animation_frame = 0

        self.image = self.current_animation[int(self.animation_frame)]

        #self.get_info()

    def draw(self):
        self.screen.blit(self.image, self.rect)
