import pygame

# screen sizes
screen_width = 960
screen_height = 720

# game status flags
_game_over = False 
_music = True 
_sound = True 
_playing = False 

# initialize font if pygame initialized
if pygame.init():
    small_font = pygame.font.Font('fonts/Minecraft.ttf', 25) 
    medium_font = pygame.font.Font('fonts/Minecraft.ttf', 30)
    big_font = pygame.font.Font('fonts/Minecraft.ttf', 70)

# paths to game assets (menu and sprite images)
menu_path = 'assets/menu/'
dino_path = 'assets/sheet/'

# function to load an image, scale it, and return it
def get_image(type, scale):
    if pygame.display.get_init(): 
        images = {
            'cloud1': pygame.image.load('assets/clouds/cloud1.png').convert_alpha(),
            'cloud2': pygame.image.load('assets/clouds/cloud2.png').convert_alpha(),
            'cloud3': pygame.image.load('assets/clouds/cloud3.png').convert_alpha(),
            'platform': pygame.image.load('assets/menu/platform.png').convert_alpha(),
            'hud_game': pygame.image.load('assets/menu/hud-game.png').convert_alpha(),
            'hud_controls': pygame.image.load('assets/menu/hud-controls.png').convert_alpha(),
            'dino': pygame.image.load('assets/menu/dino.png').convert_alpha()
        }
        image = images[type]
        return pygame.transform.scale_by(image, scale)

# function to get animation frames for different types of sprites
def get_frames(type):
    if pygame.display.get_init():
        frames = {
            'music': load_frames(0, 4, 16, 16, 4, pygame.image.load(f'{menu_path}spritesheet-music.png').convert_alpha()), 
            'sound': load_frames(0, 4, 16, 16, 4, pygame.image.load(f'{menu_path}spritesheet-sound.png').convert_alpha()), 
            'button': load_frames(0, 2, 48, 16, 4, pygame.image.load(f'{menu_path}spritesheet-button.png').convert_alpha()),
            'controls': load_frames(0, 6, 16, 16, 4, pygame.image.load(f'{menu_path}spritesheet-controls.png').convert_alpha())
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

# dictionary of music tracks loaded
music_list = {
    'menu': pygame.mixer.Sound('sounds/menu.mp3'),  
    '8-bit-game': pygame.mixer.Sound('sounds/8-bit-game.mp3'),
}

# dictionary of sound effects loaded
sound_list = {
    'click': pygame.mixer.Sound('sounds/click.mp3'), 
    'drop': pygame.mixer.Sound('sounds/drop.mp3'), 
    'collect': pygame.mixer.Sound('sounds/collect.mp3') 
}

# function to play the specified music if music is enabled
def play_music(name):
    if get_music(): 
        music_list[name].play(-1)

# function to play the specified sound effect if sound is enabled
def play_sound(name):
    if get_sound(): 
        sound_list[name].play()

# function to stop all currently playing music
def stop_music():
    for track in music_list.values():
        track.stop() 

# function to stop all currently playing sound effects
def stop_sound():
    for track in sound_list.values():
        track.stop()

# getter functions for game state flags
def get_sound():
    return _sound 

def get_music():
    return _music

def get_playing():
    return _playing

def get_game_over():
    return _game_over

# setter functions to update the game state flags
def set_sound(value):
    global _sound
    _sound = value

def set_music(value):
    global _music
    _music = value

def set_playing(value):
    global _playing
    _playing = value

def set_game_over(value):
    global _game_over
    _game_over = value
