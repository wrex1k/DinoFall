import pygame, os
from settings import * 

def resource_path(relative_path):
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

font_path = resource_path("fonts/Minecraft.ttf")

# initialize font
pygame.font.init()
small_font = pygame.font.Font(font_path, 25)
medium_font = pygame.font.Font(font_path, 30)
big_font = pygame.font.Font(font_path, 70)

# paths to game assets
menu_path = 'assets/menu/'
platform_path = 'assets/platforms/'
items_path = 'assets/items/'

# function to load an image, scale it, and return it
def get_image(type, scale):
    if pygame.display.get_init(): 
        images = {
            'cloud1': pygame.image.load(resource_path('assets/clouds/cloud1.png')).convert_alpha(),
            'cloud2': pygame.image.load(resource_path('assets/clouds/cloud2.png')).convert_alpha(),
            'cloud3': pygame.image.load(resource_path('assets/clouds/cloud3.png')).convert_alpha(),
            'platform': pygame.image.load(resource_path(f'{menu_path}platform.png')).convert_alpha(),
            'hud_game': pygame.image.load(resource_path(f'{menu_path}hud-game.png')).convert_alpha(),
            'hud_controls': pygame.image.load(resource_path(f'{menu_path}hud-controls.png')).convert_alpha(),
            'dino': pygame.image.load(resource_path(f'{menu_path}dino.png')).convert_alpha(),
            'blue_small': pygame.image.load(resource_path(f'{platform_path}blue/small.png')).convert_alpha(),
            'blue_medium': pygame.image.load(resource_path(f'{platform_path}blue/medium.png')).convert_alpha(),
            'green_small': pygame.image.load(resource_path(f'{platform_path}green/small.png')).convert_alpha(),
            'green_medium': pygame.image.load(resource_path(f'{platform_path}green/medium.png')).convert_alpha(),
            'red_small': pygame.image.load(resource_path(f'{platform_path}red/small.png')).convert_alpha(),
            'red_medium': pygame.image.load(resource_path(f'{platform_path}red/medium.png')).convert_alpha(),
            'yellow_small': pygame.image.load(resource_path(f'{platform_path}yellow/small.png')).convert_alpha(),
            'yellow_medium': pygame.image.load(resource_path(f'{platform_path}yellow/medium.png')).convert_alpha(),
            'icon': pygame.image.load(resource_path('assets/icon.png')).convert_alpha()
        }
        image = images[type]
        return pygame.transform.scale_by(image, scale)

# function to get animation frames for different types of sprites
def get_frames(type):
    if pygame.display.get_init():
        frames = {
            'music': load_frames(0, 4, 16, 16, 4, pygame.image.load(resource_path(f'{menu_path}spritesheet-music.png')).convert_alpha()), 
            'sound': load_frames(0, 4, 16, 16, 4, pygame.image.load(resource_path(f'{menu_path}spritesheet-sound.png')).convert_alpha()), 
            'button': load_frames(0, 2, 48, 16, 4, pygame.image.load(resource_path(f'{menu_path}spritesheet-button.png')).convert_alpha()),
            'controls': load_frames(0, 6, 16, 16, 4, pygame.image.load(resource_path(f'{menu_path}spritesheet-controls.png')).convert_alpha()),
            'coin': load_frames(0, 8, 20, 20, 2, pygame.image.load(resource_path(f'{items_path}spritesheet-coin.png')).convert_alpha()),
            'powerup': load_frames(0, 8, 20, 20, 2, pygame.image.load(resource_path(f'{items_path}spritesheet-powerup.png')).convert_alpha())
        }
    return frames[type]

# function to load frames from spritesheet
def load_frames(start, stop, width, height, scale, spritesheet, flip=False):
    frames = [] 
    for i in range(start, stop): 
        frame = spritesheet.subsurface(pygame.Rect(i * width, 0, width, height))
        if flip: 
            frame = pygame.transform.flip(frame, True, False)
        frame = pygame.transform.scale_by(frame, scale)  
        frames.append(frame)
    
    return frames

def draw_clouds(screen):
    screen.fill(('#0099db'))
    cloud1 = get_image('cloud1', 4)
    cloud2 = get_image('cloud2', 4)
    cloud3 = get_image('cloud3', 4)
    screen.blit(cloud1, (0, 120))
    screen.blit(cloud2, (700, 300))
    screen.blit(cloud3, (0, 600))
