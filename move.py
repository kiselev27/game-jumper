import pygame


class Move:
    def move(direction, spritex, spritey, step):
        if direction:
            if direction == K_UP:
                spritey -= step
            elif direction == K_DOWN:
                spritey += step
            if direction == K_LEFT:
                spritex -= step
            elif direction == K_RIGHT:
                spritex += step
        return spritex, spritey