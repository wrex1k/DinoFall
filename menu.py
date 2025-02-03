import pygame
from settings import *

class Menu:
    def __init__(self, screen):
        # reference to screen
        self.screen = screen

        # menu attributes
        self.scale = 4
        self.menu_elements = 5
        self.selected_index = 0

        # initialized menu texts
        self.title_text = big_font.render('Dino Fall', True, ('white'))
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

    # draw clouds on screen
    def draw_clouds(self):
        self.screen.fill(('#0099db'))
        cloud1 = get_image('cloud1', self.scale)
        cloud2 = get_image('cloud2', self.scale)
        cloud3 = get_image('cloud3', self.scale)
        self.screen.blit(cloud1, (0, 120))
        self.screen.blit(cloud2, (700, 300))
        self.screen.blit(cloud3, (0, 600))
        
    def draw_controls(self):
        # draw background
        self.draw_clouds()

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
            control = control.split('.')
            text = small_font.render(control[1], True, ('white'))
            self.screen.blit(button, (x, y))
            self.screen.blit(text, (x, y + 70))
            x += 80

        # draw texts for controls
        self.screen.blit(self.controls_text, (screen_width / 2 - self.controls_text.get_width() / 2, 50))
        self.screen.blit(self.arrows_text, (400, 270))
        self.screen.blit(self.color_text, (220, 370))
        self.screen.blit(self.exit_text, (screen_width / 2 - self.exit_text.get_width() / 2, 480))
            

    def draw_menu(self):
        # draw background
        self.draw_clouds()
        
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
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % self.menu_elements
                if get_sound(): play_sound('click')
            if event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % self.menu_elements
                if get_sound(): play_sound('click')
            if event.key == pygame.K_RETURN:
                if self.selected_index == 0:
                    stop_music()
                    if get_music(): 
                        play_music('8-bit-game')
                    return 'play'
                if self.selected_index == 1:
                    return 'controls'
                if self.selected_index == 2:
                    return 'exit'
                if self.selected_index == 3:
                    set_music(not get_music())
                    play_music('8-bit-menu') if get_music() else stop_music()
                if self.selected_index == 4:
                    set_sound(not get_sound())