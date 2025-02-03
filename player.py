import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        # reference to screen
        self.screen = screen
        # player attributes
        self.scale = 3
        self.rect = pygame.Rect(x, y, 24*self.scale, 24*self.scale-10)
        self.direction = 'right'
        self.speed = 220
        self.velocity_y = 0
        self.gravity = 1.5
        self.score = 0
        self.max_score = 0
        self.coins = 0
        self.dead = False
        self.was_on_platform = False

        # list of available dinos and default color
        self.dinos = ['blue', 'red', 'yellow', 'green']
        self.current_color = 'green'

        # loading all avaible animations for the dino colors in dictionary
        self.all_animations = {color: self.load_animations(color) for color in self.dinos}

        # set animations for the current color
        self.animations = self.all_animations[self.current_color]
        self.current_animation = self.animations['idle_right']
        self.animation_frame = 0

        # initialize image of player and mask
        self.image = self.current_animation[0]
        self.mask = pygame.mask.from_surface(self.image)

    # info about player for debugging
    def get_info(self):
        print(f"dead: {self.dead} | x: {self.rect.x} | y: {self.rect.y} | G: {self.gravity} | velocity_y: {self.velocity_y} | on_platform: {self.on_platform} | speed: {self.speed}")

    # load animations for a dino based on given color
    def load_animations(self, color):
        path = f'assets/sheets/DinoSprites - {color}.png'
        spritesheet = pygame.image.load(path).convert_alpha()

        return {
            'idle_right': load_frames(start=0, stop=3, width=24, height=24, scale=3, spritesheet=spritesheet),
            'idle_left': load_frames(start=0, stop=3, width=24, height=24, scale=3, spritesheet=spritesheet, flip=True),
            'walk_right': load_frames(start=4, stop=8, width=24, height=24, scale=3, spritesheet=spritesheet),
            'walk_left': load_frames(start=4, stop=8, width=24, height=24, scale=3, spritesheet=spritesheet, flip=True),
        }

    # change dino color based on given color
    def change_dino(self, color):
        if color in self.all_animations:
            self.current_color = color
            self.animations = self.all_animations[color]  
            self.current_animation = self.all_animations[color]['idle_right']

    # check if the player is dead
    def check_if_dead(self):
        if self.rect.top < 50 or self.rect.bottom >= screen_height:
            stop_music()
            set_playing(False)
            set_game_over(True)
            self.dead = True
            self.speed = 0
            self.velocity_y = 0
            self.gravity = 0
            if self.score > self.max_score:
                self.max_score = self.score

    # restart the player by resetting attributes to the initial state
    def restart_player(self):
        set_game_over(False)
        self.dead = False
        self.speed = 220
        self.score = 0
        self.coins = 0
        self.velocity_y = 0
        self.gravity = 1.5
        self.rect.x = 100
        self.rect.y = 200

    def update(self, delta_time, platforms):
        # reset platform interaction and moving status
        self.on_platform = False
        moving = False
        # store old x position to collision check
        old_x = self.rect.x  

        if not self.dead:
            # score calculation based on coin collected
            self.score += 1 if self.coins == 0 else 1 * self.coins

            keys = pygame.key.get_pressed()
            # handle left and right movement
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed * delta_time
                self.direction = 'left'
                moving = True
            if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
                self.rect.x += self.speed * delta_time
                self.direction = 'right'
                moving = True

            # check for collisions with platforms
            for platform in platforms:
                if pygame.sprite.collide_mask(self, platform):   

                    # set speed based on corected colors
                    self.speed = 220 if platform.color == self.current_color else 100
                    
                    # change dino color to match platform color
                    #self.change_dino(platform.color)   
    
                    # handle player landing on the platform
                    if self.rect.bottom <= platform.rect.top + 10:
                        self.rect.bottom = platform.rect.top 
                        self.velocity_y = 0
                        self.on_platform = True
                        
                        # if the dino just landed, play sound
                        if not self.was_on_platform:
                            if get_sound():
                                play_sound('drop')
                        break
                    else:
                        # if the player is not on the platform, move it down
                        self.rect.y -= self.speed * delta_time
                        self.rect.x = old_x

                # if the player is not on a platform, apply gravity
                if not self.on_platform:
                    self.velocity_y += self.gravity * delta_time
            
            # store previous on_platform status
            self.was_on_platform = self.on_platform
                    
            # update the position on velocity
            self.rect.y += self.velocity_y

            # limit fall speed to 5
            if not self.on_platform:
                self.velocity_y = min(self.velocity_y, 5)

            # update the player animation based on movement
            if moving:
                self.current_animation = self.animations[f'walk_{self.direction}']
            else:
                self.current_animation = self.animations[f'idle_{self.direction}']

            # update the animation frame index
            self.animation_frame += 5 * delta_time
            if self.animation_frame >= len(self.current_animation):
                self.animation_frame = 0

            # update the player image
            self.image = self.current_animation[int(self.animation_frame)]
            
            # check
            #self.max_score = max(self.max_score, self.score)

            # check if the player is dead
            self.check_if_dead()
    def draw(self):
        self.screen.blit(self.image, self.rect)