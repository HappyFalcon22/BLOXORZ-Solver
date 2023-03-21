import pygame
import os
from read_level import level_1
from Images import VOID_TILE, NORMAL_TILE, FINISH_TILE, BLOCK
import time
from board_test import Game
import keyboard

# Set parameters
WIDTH, HEIGHT = 800, 700
WHITE = (250, 250, 250)
GRAY = (180, 180, 180)
BOARD_START_POINT = 75
# Create a window

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLOXORZ")

FPS = 60

void_tile = 0
normal_tile = 1
bridge_tile_soft = 2
bridge_tile_hard = 3
bridge = 4
soft_tile = 5
division_tile = 6
finish_tile = 7


def draw_board(game : Game):
    board = game.state
    for i in range(20):
        for j in range(20):
            position = (BOARD_START_POINT + 25 * j, BOARD_START_POINT + 25 * i)
            tile = board[i][j]
            if tile == 0: # Void tile
                WINDOW.blit(VOID_TILE, position)
                pass
            elif tile == 1: # Normal tile
                WINDOW.blit(NORMAL_TILE, position)
            elif tile == 7: # Finish tile
                WINDOW.blit(FINISH_TILE, position)
    # Draw the block 
    if game.state_block == "FALL":
        position_1 = (BOARD_START_POINT + 25 * game.pos[1], BOARD_START_POINT + 25 * game.pos[0])
        position_2 = (BOARD_START_POINT + 25 * game.pos[3], BOARD_START_POINT + 25 * game.pos[2])
        WINDOW.blit(BLOCK, position_1)
        WINDOW.blit(BLOCK, position_2)
    else:
        position = (BOARD_START_POINT + 25 * game.pos[1], BOARD_START_POINT + 25 * game.pos[0])
        WINDOW.blit(BLOCK, position)
    pygame.display.update()


def draw_window():
    WINDOW.fill(WHITE)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    lvl = Game(level_1)
    draw_window()
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False
        if keyboard.is_pressed("w"):
            lvl.up()
            time.sleep(0.2)
        if keyboard.is_pressed("s"):
            lvl.down()
            time.sleep(0.2)
        if keyboard.is_pressed("a"):
            lvl.left()
            time.sleep(0.2)
        if keyboard.is_pressed("d"):
            lvl.right()
            time.sleep(0.2)
        draw_board(lvl)
    pygame.quit()

if __name__ == "__main__":
    main()