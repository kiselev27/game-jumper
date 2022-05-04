
import pygame
import sys
from pygame.locals import *
from gameParams import Game, Hero

def main():
    game = Game()
    hero = Hero()

    while game.is_runnig:
        game.fps.tick(game.FPS)
        
        game.screen.blit(game.background, (0, 0))
        game.screen.blit(hero.img, (hero.position_X, hero.position_Y))
        
        hero.img = hero.img_stay
        
        for event in pygame.event.get():            
            if event.type == QUIT:
                game.is_runnig = False
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                hero.direction = event.key  # Передаем нажатую кнопку в объект Hero
                
            if event.type == KEYUP:
                hero.direction = False  # Кнопка отпущена
            
        hero.move()
        pygame.display.update()


# def move(direction, hero_pos__X, hero_pos__Y, game, isJumping):
    
#     isJumping = False
#     jumpCount = 10
    
#     if direction:
#         if isJumping:
#             if direction == K_LEFT and hero_pos__X > game.BORDER_WIDTH:
#                 hero_pos__X -= game.STEP
#             elif direction == K_RIGHT and hero_pos__X < game.SCREEN_WIDTH - game.hero_width - game.BORDER_WIDTH:
#                 hero_pos__X += game.STEP
#         elif not isJumping:
#             if direction == K_SPACE:
#                 isJumping = True
                
#                 if jumpCount >= -10:
#                     if jumpCount < 0:
#                         hero_pos__Y += (jumpCount ** 2) / 3
#                     else:
#                         hero_pos__Y -= (jumpCount ** 2) / 3
#                     jumpCount -= 1
#                 else:
#                     isJumping = False
#                     jumpCount = 10
                    
            # hero_pos__Y -= game.STEP
        # elif direction == K_DOWN and hero_pos__y < game.BORDER_HEIGHT - game.BORDER_WIDTH:
        #     hero_pos__Y += game.STEP
            
        
            
    # return hero_pos__X, hero_pos__Y, isJumping

if __name__ == '__main__':
    main()