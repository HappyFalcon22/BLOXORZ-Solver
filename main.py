import pygame
import os
from read_level import level_1
from Images import VOID_TILE, NORMAL_TILE, FINISH_TILE, BLOCK
import keyboard
import time

# Set parameters
WIDTH, HEIGHT = 800, 700
WHITE = (255, 255, 255)
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

class Game():
    def __init__(self, level) -> None:
        self.id, self.start, self.board = level
        self.position = self.start
        self.state_block = "STAND"
    def up(self):
        if self.state_block == "STAND":
            # Look at 2 tiles above it
            x, y = self.position[0], self.position[1]
            self.position = [[x, y - 1], [x, y - 2]]
            self.state_block = "FALL"
        elif self.state_block == "FALL":
            # Fall, up will remain the state fall
            x1, y1, x2, y2 = self.position[0][0], self.position[0][1], self.position[1][0], self.position[1][1]
            if y1 == y2:
                y1 -= 1
                y2 -= 1
                self.position = [[x1, y1], [x2, y2]]
            else: # Fall, up will make the block stand
                current = self.position
                pos1 = current[0]
                pos2 = current[1]
                if y1 - 1 == y2 - 2:
                    self.position = [x1, y1 - 1]
                else:
                    self.position = [x1, y1 - 2]
                self.state_block = "STAND"
    def down(self):
        if self.state_block == "STAND":
            # Look at 2 tiles below it
            x, y = self.position[0], self.position[1]
            self.position = [[x, y + 1], [x, y + 2]]
            self.state_block = "FALL"
        elif self.state_block == "FALL":
            # Fall, up will remain the state fall
            x1, y1, x2, y2 = self.position[0][0], self.position[0][1], self.position[1][0], self.position[1][1]
            if y1 == y2:
                y1 += 1
                y2 += 1
                self.position = [[x1, x2], [y1, y2]]
            else: # Fall, up will make the block stand
                if y1 + 1 == y2 + 2:
                    self.position = [x1, y1 + 1]
                else:
                    self.position = [x1, y1 + 2]
                self.state_block = "STAND"
    def left(self):
        if self.state_block == "STAND":
            # Look at 2 tiles left of it
            x, y = self.position[0], self.position[1]
            self.position = [[x - 1, y], [x - 2, y]]
            self.state_block = "FALL"
        elif self.state_block == "FALL":
            # Fall, left will remain the state fall
            x1, y1, x2, y2 = self.position[0][0], self.position[0][1], self.position[1][0], self.position[1][1]
            if x1 == x2:
                x1 -= 1
                x2 -= 1
                self.position = [[x1, y1], [x2, y2]]
            else: # Fall, up will make the block stand
                if x1 - 1 == x2 - 2:
                    self.position = [x1 - 1, y1]
                else:
                    self.position = [x1 - 2, y1]
                self.state_block = "STAND"
    def right(self):
        if self.state_block == "STAND":
            # Look at 2 tiles right of it
            x, y = self.position[0], self.position[1]
            self.position = [[x + 1, y], [x + 2, y]]
            self.state_block = "FALL"
        elif self.state_block == "FALL":
            x1, y1, x2, y2 = self.position[0][0], self.position[0][1], self.position[1][0], self.position[1][1]
            # Fall, left will remain the state fall
            if x1 == x2:
                x1 += 1
                x2 += 1
                self.position = [[x1, y1], [x2, y2]]
            else: # Fall, up will make the block stand
                if x1 + 1 == x2 + 2:
                    self.position = [x1 + 1, y1]
                else:
                    self.position = [x1 + 2, y2]
                self.state_block = "STAND"
    def swap(self):
        pass
    def draw_board(self):
        board = self.board
        for i in range(400):
            position = (BOARD_START_POINT + 25 * (i % 20), BOARD_START_POINT + 25 * (i // 20))
            tile = board[i // 20][i % 20]
            if tile == 0: # Void tile
                WINDOW.blit(VOID_TILE, position)
            elif tile == 1: # Normal tile
                WINDOW.blit(NORMAL_TILE, position)
            elif tile == 7: # Finish tile
                WINDOW.blit(FINISH_TILE, position)
        # Draw the block 
        if self.state_block == "FALL":
            position_1 = (BOARD_START_POINT + 25 * self.position[0][0], BOARD_START_POINT + 25 * self.position[0][1])
            position_2 = (BOARD_START_POINT + 25 * self.position[1][0], BOARD_START_POINT + 25 * self.position[1][1])
            WINDOW.blit(BLOCK, position_1)
            WINDOW.blit(BLOCK, position_2)
        else:
            position = (BOARD_START_POINT + 25 * self.position[0], BOARD_START_POINT + 25 * self.position[1])
            WINDOW.blit(BLOCK, position)
        pygame.display.update()

def draw_window():
    WINDOW.fill(GRAY)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    lvl = Game(level_1)
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
        lvl.draw_board()
    pygame.quit()

if __name__ == "__main__":
    main()