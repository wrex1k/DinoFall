import pygame, random
from utils import load_frames, resource_path
from audiomanager import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, speed):
        super().__init__()
        # reference to screen and player
        self.screen = screen
        
        # random coin position
        self.x = x
        self.y = y

        # coin attributes
        self.collected = False
        self.played = False
        self.speed = speed

        self.frames = [] # list of frames for coin animation
        self.load_animation() # load the animation frames

        # animation attributes
        self.frame_index = 0
        self.animation_speed = 0.1
        self.animation_time = 0

    # use coin spritesheet to load frames, set position and create mask
    def load_animation(self):
        path = resource_path('assets/coins/coin.png')
        sprite_sheet = pygame.image.load(path).convert_alpha()
        self.frames = load_frames(0, 8, 20, 20, 2, sprite_sheet)
        self.rect = self.frames[0].get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.frames[0])

    # updating speed to synchronize coin draw
    def update_speed(self, speed):
        self.speed = speed

    def update(self, delta_time):
        # move coin upwards
        self.rect.y -= self.speed * delta_time
        self.animation_time += delta_time

        # update coin animation
        if self.animation_time >= self.animation_speed:
            self.animation_time = 0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.frame_index = 0

        # update coin image to current frame
        self.image = self.frames[self.frame_index]

    def draw(self):
        # draw coin if not collected
        if not self.collected:
            self.screen.blit(self.image, self.rect)
