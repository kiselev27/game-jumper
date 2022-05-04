import pygame
from pygame.locals import *

class Game:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 900
    BACKGROUND_IMG = 'C:/Users/kisel/PycharmProjects/jumper/Images/Background/bg_layer1.png'
    GAME_ICON = 'C:/Users/kisel/PycharmProjects/jumper/Images/Players/bunny1_stand.png'
    BORDER_WIDTH = 5
    STEP = 5
    FPS = 120
    
    

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.game_caption = pygame.display.set_caption('Rabbit Jumper')
        self.icon = pygame.display.set_icon(pygame.image.load(self.GAME_ICON))
        self.fps = pygame.time.Clock()
        self.background = pygame.image.load(self.BACKGROUND_IMG)
        self.is_runnig = True
        
        # pygame.mixer.init()
        
        # playsound('C:/Users/kisel/PycharmProjects/jumper/Music/background.mp3')
        
        # self.background_sound = pygame.mixer.Sound('C:/Users/kisel/PycharmProjects/jumper/Music/background.mp3')
        # self.background_sound.set_volume(0.05)
        # self.background_sound.play()
        
        
class Hero(Game):
    HERO_IMG =  'C:/Users/kisel/PycharmProjects/jumper/Images/Players/bunny1_stand.png'
    HERO_IMG_JUMP =  'C:/Users/kisel/PycharmProjects/jumper/Images/Players/bunny1_jump.png'
    HERO_IMG_JUMP_READY =  'C:/Users/kisel/PycharmProjects/jumper/Images/Players/bunny1_ready.png'
    
    HERO_IMG_WALK_RIGHT =  'C:/Users/kisel/PycharmProjects/jumper/Images/Players/bunny1_walk_right.png'
    HERO_IMG_WALK_RIGHT_MOTION =  'C:/Users/kisel/PycharmProjects/jumper/Images/Players/bunny1_walk2.png'
    
    HERO_IMG_WALK_LEFT =  'C:/Users/kisel/PycharmProjects/jumper/Images/Players/bunny1_walk_left.png'
    HERO_IMG_WALK_LEFT_MOTION =  'C:/Users/kisel/PycharmProjects/jumper/Images/Players/bunny1_walk2_left.png'
    
    
    
    def __init__(self):
        self.img = pygame.image.load(self.HERO_IMG)
        self.img_jump = pygame.image.load(self.HERO_IMG_JUMP)
        self.img_jump_ready = pygame.image.load(self.HERO_IMG_JUMP_READY)
        
        
        self.img_jump_walk_right = pygame.image.load(self.HERO_IMG_WALK_RIGHT)
        self.img_jump_walk_right_motion = pygame.image.load(self.HERO_IMG_WALK_RIGHT_MOTION)
        self.walk_right = [self.img_jump_walk_right, self.img_jump_walk_right_motion]
        
        
        self.img_jump_walk_left = pygame.image.load(self.HERO_IMG_WALK_LEFT)
        self.img_jump_walk_left_motion = pygame.image.load(self.HERO_IMG_WALK_LEFT_MOTION)
        self.walk_left = [self.img_jump_walk_left, self.img_jump_walk_left_motion]
        
        self.img_stay = self.img
        
        
        self.hero_width = self.img.get_width()
        self.hero_height = self.img.get_height()
        
        self.direction = False
        
        self.position_X = (Game.SCREEN_WIDTH - self.hero_width) / 2
        self.position_Y = (Game.SCREEN_HEIGHT - self.hero_height) - Game.BORDER_WIDTH
        
        self.isJumping = False
        self.jumpCount = 10
        
        # self.jump_sound = pygame.mixer.Sound('C:/Users/kisel/PycharmProjects/jumper/Music/jump.mp3')
        # self.jump_sound.set_volume(0.05)
        
    def move(self):
        if not self.isJumping:
            # Обрабатываем пробел (Прыжок)
            if self.direction == K_SPACE:
                self.isJumping = True
        
        if self.isJumping:
            # self.jump_sound.play()
            self.jump()
            
        
        if self.direction == K_LEFT and self.position_X > Game.BORDER_WIDTH:
            self.img = self.img_jump_walk_left
            self.position_X -= Game.STEP
        elif self.direction == K_RIGHT and self.position_X < Game.SCREEN_WIDTH - self.hero_width - Game.BORDER_WIDTH:
            # for animation in
            self.img = self.img_jump_walk_right
            self.position_X += Game.STEP
                    
        return self.position_X, self.position_Y, self.isJumping
    
    
    def jump(self):
        self.img = self.img_jump

        if self.jumpCount >= -10:
            if self.jumpCount < 0:
                self.position_Y += ((self.jumpCount ** 2) / 2)
            else:
                self.position_Y -= ((self.jumpCount ** 2) / 2)
                
            self.jumpCount -= 0.5
        else:
            self.isJumping = False
            self.jumpCount = 10
            self.img = self.img_stay
        