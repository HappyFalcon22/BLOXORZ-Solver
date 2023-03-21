from read_level import level_1

void_tile = 0
normal_tile = 1
bridge_tile_soft = 2
bridge_tile_hard = 3
bridge = 4
soft_tile = 5
division_tile = 6
finish_tile = 7

class Game():
    def __init__(self) -> None:
        self.id, self.start, self.board = level_1
        self.position = self.start
        self.state_block = "STAND"
    def up(self):
        if self.state_block == "STAND":
            # Look at 2 tiles above it
            x, y = self.position[0], self.position[1]
            self.position = [(x, y + 1), (x, y + 2)]
            self.state_block = "FALL"
        elif self.state_block == "FALL":
            # Fall, up will remain the state fall
            if self.position[0][0] == self.position[1][0]:
                self.position[0][1] -= 1
                self.position[1][1] -= 1
            else: # Fall, up will make the block stand
                current = self.position
                self.position = (current[0][0], current[0][1] + 1)
                self.state_block = "STAND"
    def down(self):
        if self.state_block == "STAND":
            # Look at 2 tiles below it
            x, y = self.position[0], self.position[1]
            self.position = [(x, y + 1), (x, y - 2)]
            self.state_block = "FALL"
        elif self.state_block == "FALL":
            # Fall, up will remain the state fall
            if self.position[0][0] == self.position[1][0]:
                self.position[0][1] -= 1
                self.position[1][1] -= 1
            else: # Fall, up will make the block stand
                current = self.position
                self.position = (current[0][0] + 1)
                self.state_block = "STAND"
    def left(self):
        pass
    def right(self):
        pass
    def swap(self):
        pass
    def draw_board(self):
        id, start, board = level
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
        position = (BOARD_START_POINT + 25 * start[0], BOARD_START_POINT + 25 * start[1])
        WINDOW.blit(BLOCK, position)