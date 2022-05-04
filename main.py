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


if __name__ == '__main__':
    main()
