# screen sizes
screen_width = 960
screen_height = 720

# game status flags
_game_state = 'menu'
_first_game = True
_music = True
_sound = True

volume = {
    'menu': 0.3,
    'click': 0.6,
    '8-bit-game': 0.3,
    'land': 0.4,
    'collect': 0.4
}

def set_first_game(value):
    global _first_game
    _first_game = value

def set_game_state(value):
    global _game_state
    _game_state = value

def set_music(value):
    global _music
    _music = value

def set_sound(value):
    global _sound
    _sound = value

def get_first_game():
    return _first_game

def get_game_state():
    return _game_state

def get_music():
    return _music

def get_sound():
    return _sound

