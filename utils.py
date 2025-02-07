import pygame, os
from settings import * 

def resource_path(relative_path):
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

font_path = resource_path("fonts/Minecraft.ttf")

# initialize font if pygame initialized
pygame.init()
try:
    small_font = pygame.font.Font(font_path, 25)
    medium_font = pygame.font.Font(font_path, 30)
    big_font = pygame.font.Font(font_path, 70)
except FileNotFoundError:
    print(f"Chyba: Font '{font_path}' nebol nájdený!")

# paths to game assets (menu and sprite images)
menu_path = 'assets/menu/'
dino_path = 'assets/sheet/'

# function to load an image, scale it, and return it
def get_image(type, scale):
    if pygame.display.get_init(): 
        images = {
            'cloud1': pygame.image.load(resource_path('assets/clouds/cloud1.png')).convert_alpha(),
            'cloud2': pygame.image.load(resource_path('assets/clouds/cloud2.png')).convert_alpha(),
            'cloud3': pygame.image.load(resource_path('assets/clouds/cloud3.png')).convert_alpha(),
            'platform': pygame.image.load(resource_path('assets/menu/platform.png')).convert_alpha(),
            'hud_game': pygame.image.load(resource_path('assets/menu/hud-game.png')).convert_alpha(),
            'hud_controls': pygame.image.load(resource_path('assets/menu/hud-controls.png')).convert_alpha(),
            'dino': pygame.image.load(resource_path('assets/menu/dino.png')).convert_alpha()
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
            'controls': load_frames(0, 6, 16, 16, 4, pygame.image.load(resource_path(f'{menu_path}spritesheet-controls.png')).convert_alpha())
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
