import pygame
from utils import resource_path
from settings import *

pygame.mixer.init()

# dictionary of sound_effects
sound_effects = {
    'click': pygame.mixer.Sound(resource_path('sounds/click.mp3')),
    'land': pygame.mixer.Sound(resource_path('sounds/land.mp3')),
    'collect-coin': pygame.mixer.Sound(resource_path('sounds/collect-coin.mp3')),
    'collect-powerup': pygame.mixer.Sound(resource_path('sounds/collect-powerup.mp3'))
}

# dictionary of music_tracks
music_tracks = {
    'menu': resource_path('sounds/menu.mp3'),
    '8-bit-game': resource_path('sounds/8-bit-game.mp3')
}

# set volume from settings for every sound effects
for name, sound in sound_effects.items():
    sound.set_volume(volume.get(name, 0.5))

# play sound if sound is enabled
def play_sound(name):
    if get_sound() and name in sound_effects:
        sound_effects[name].play()

# play music if music is enabled, set volume from settings, loop as default
def play_music(name, loop=-1):
    if get_music() and name in music_tracks:
        pygame.mixer.music.load(music_tracks[name])
        pygame.mixer.music.set_volume(volume.get(name, 0.5))
        pygame.mixer.music.play(loop)

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def set_music_volume(vol):
    pygame.mixer.music.set_volume(vol)
