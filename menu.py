import pygame
from settings import * 
from utils import *
from audiomanager import * 

class Menu:
    def __init__(self, screen):
        # reference to screen
        self.screen = screen

        if get_music(): play_music('menu')

        # menu attributes
        self.scale = 4
        self.menu_elements = 5
        self.selected_index = 0

        # initialized menu texts
        self.title_text = big_font.render('DinoFall', True, ('white'))
        self.controls_text = big_font.render('Controls', True, ('white'))
        self.arrows_text = medium_font.render('Move', True, ('white'))
        self.color_text = medium_font.render('Color Change', True, ('white'))
        self.exit_text = small_font.render('Exit with ESC', True, ('white'))
        
        # load images menu and controls for UI
        self.platform = get_image('platform', 4)
        self.dino = get_image('dino', 3)
        self.hud_controls = get_image('hud_controls', 4)
        self.hud_controls_rect = self.hud_controls.get_rect(center=(screen_width / 2, screen_height / 2))
        
        # load different button frame images
        self.button_frames = get_frames('button')
        self.music_frames = get_frames('music')
        self.sound_frames = get_frames('sound')
        self.controls_frames = get_frames('controls')

        # dictionary of button states (normal, selected, music, sound)
        self.button_images = {
            'normal': self.button_frames[0],
            'selected': self.button_frames[1],
            'music_on': self.music_frames[0],
            'music_on_selected': self.music_frames[1],
            'music_off': self.music_frames[2],
            'music_off_selected': self.music_frames[3],
            'sound_on': self.sound_frames[0],
            'sound_on_selected': self.sound_frames[1],
            'sound_off': self.sound_frames[2],
            'sound_off_selected': self.sound_frames[3],
            'a.blue': self.controls_frames[0],
            's.green': self.controls_frames[1],
            'd.red': self.controls_frames[2],
            'f.yellow': self.controls_frames[3],
            'left_arrow': self.controls_frames[4],
            'right_arrow': self.controls_frames[5]
        }
        
    def draw_controls(self):
        # draw background
        draw_clouds(self.screen)

        # draw controls hud
        self.screen.blit(self.hud_controls, self.hud_controls_rect) 

        # draw control buttons (arrows and keys)
        x, y = 500, 250
        for control in ['left_arrow', 'right_arrow']:
            button = self.button_images[control]
            self.screen.blit(button, (x, y))
            x += 80

        x, y = 450, 350
        for control in ['a.blue', 's.green', 'd.red', 'f.yellow']:
            button = self.button_images[control]
            button_width = button.get_width()  
            control = control.split('.')
            text = small_font.render(control[1], True, ('white'))
            text_width = text.get_width() 
            self.screen.blit(button, (x, y))
            self.screen.blit(text, (x + (button_width - text_width) // 2, y + 70))
            x += 80

        # draw texts for controls
        self.screen.blit(self.controls_text, (screen_width / 2 - self.controls_text.get_width() / 2, 70))
        self.screen.blit(self.arrows_text, (400, 270))
        self.screen.blit(self.color_text, (220, 370))
        self.screen.blit(self.exit_text, (screen_width / 2 - self.exit_text.get_width() / 2, 480))
            

    def draw_menu(self):
        # draw background
        draw_clouds(self.screen)
        
        # draw title and images
        self.screen.blit(self.title_text, (screen_width / 2 - self.title_text.get_width() / 1.6, 70))
        self.screen.blit(self.platform, (screen_width / 2 - self.platform.get_width() / 2, 200))
        self.screen.blit(self.dino, (600, 200 - self.dino.get_height()))

        # draw menu buttons (Play, Controls, Exit)
        self.menu_button('Play', 310, 0)
        self.menu_button('Controls', 390, 1)
        self.menu_button('Exit', 470, 2)
        self.music_button(520, 3)
        self.sound_button(520, 4)
    
    # draw sound buttons if selected draw different one
    def sound_button(self, y, index):
        if get_sound():
            button = self.button_images["sound_on_selected"] if index == self.selected_index else self.button_images["sound_on"]
        else:
            button = self.button_images["sound_off_selected"] if index == self.selected_index else self.button_images["sound_off"]
        self.screen.blit(button, (self.screen.get_width() / 2 + button.get_width()/2, y)) 

    # draw music buttons if selected draw different one
    def music_button(self, y, index):
        if get_music():
            button = self.button_images["music_on_selected"] if index == self.selected_index else self.button_images["music_on"]
        else:
            button = self.button_images["music_off_selected"] if index == self.selected_index else self.button_images["music_off"]
        self.screen.blit(button, (self.screen.get_width() / 2 - (button.get_width() /2 * 3), y))

    # draw buttons in menu if selected draw different one
    def menu_button(self, text, y, index):
        button = self.button_images["selected"] if index == self.selected_index else self.button_images["normal"]
        button_rect = button.get_rect(center=(screen_width / 2, y))
        text_surf = medium_font.render(text, True, ('white'))
        text_rect = text_surf.get_rect(center=(screen_width / 2, y))
        self.screen.blit(button, button_rect)
        self.screen.blit(text_surf, text_rect)

    # menu event handler (key events to navigation)
    def handle_menu_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # menu navigation up
                self.selected_index = (self.selected_index - 1) % self.menu_elements
                if get_sound(): play_sound('click')
            if event.key == pygame.K_DOWN: # menu navigation down
                self.selected_index = (self.selected_index + 1) % self.menu_elements
                if get_sound(): play_sound('click')
            
            if event.key == pygame.K_RETURN:
                if self.selected_index == 0:
                    if get_first_game() == False:
                        set_game_state('gameover')
                        if get_sound(): stop_music()
                    else: 
                        set_game_state('play')
                        if get_sound(): play_music('8-bit-game')
                if self.selected_index == 1: # controls
                    set_game_state('controls')
                if self.selected_index == 2: # exit
                    set_game_state('exit')
                if self.selected_index == 3: # music
                    set_music(not get_music())
                    unpause_music() if get_music() else pause_music()
                if self.selected_index == 4: # sound
                    set_sound(not get_sound())

    # controls event handler       
    def handle_controls_input(self, event):
            if event.key == pygame.K_ESCAPE:
                set_game_state('menu')