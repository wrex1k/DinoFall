import pygame
from utils import *
from audiomanager import *

class Item(pygame.sprite.Sprite):
    def __init__(self, screen, type, x, y, speed):
        super().__init__()
        # reference to screen
        self.screen = screen

        # item attributes
        self.type = type
        self.collected = False
        self.played = False
        self.speed = speed
        self.x = x
        self.y = y

        self.frames = [] # list of frames for item animation
        self.load_animations(self.type) # load the animation frames

        # animation attributes
        self.frame_index = 0
        self.animation_speed = 0.1
        self.animation_time = 0

    # use item spritesheet to load frames, set position and create mask
    def load_animations(self, type):
        self.frames = get_frames(type)
        self.rect = self.frames[0].get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.frames[0])

    # updating speed to synchronize item draw
    def update_speed(self, speed):
        self.speed = speed

    def update(self, delta_time):
        # move item upwards
        self.rect.y -= self.speed * delta_time
        self.animation_time += delta_time

        # update item animation
        if self.animation_time >= self.animation_speed:
            self.animation_time = 0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.frame_index = 0

        # update item image to current frame
        self.image = self.frames[self.frame_index]

    def draw(self):
        # draw item if not collected
        if not self.collected:
            self.screen.blit(self.image, self.rect)
