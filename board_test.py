from read_level import level_1
import time

# Game() class, with attributes :
# + id          : defined the id of the level
# + start       : the starting position on the board, FIXED
# + pos         : the current position on the board, which will be :
#   - (x, y) if the block is standing
#   - (x1, y1, x2, y2) if the block is falling or the block is splitted into two halves
# + state_block : indicates the state of the block, consists of : "FALL", "STAND" or "DIVIDED"
# + state       : the 20x20 board, notations of the tiles are described
# + goal        : the tile that you need to move the block to, undefined in init

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
        self.id, self.start, self.state = level
        self.pos = self.start
        self.state_block = "STAND"
        self.goal = self.find_finish_state()
        print("The goal is at :", self.goal)

    def is_up_legal(self):
        pos = self.if_up()
        if len(pos) == 2:
            if self.state[pos[0]][pos[1]] == 0 : # Void_tile
                return False
        if len(pos) == 4: # Fall
            if self.state[pos[0]][pos[1]] == 0 or self.state[pos[2]][pos[3]] == 0:
                return False
        return True
            

    def is_down_legal(self):
        pos = self.if_down()
        if len(pos) == 2:
            if self.state[pos[0]][pos[1]] == 0 : # Void_tile
                return False
        if len(pos) == 4: # Fall
            if self.state[pos[0]][pos[1]] == 0 or self.state[pos[2]][pos[3]] == 0:
                return False
        return True
    
    def is_left_legal(self):
        pos = self.if_left()
        if len(pos) == 2:
            if self.state[pos[0]][pos[1]] == 0 : # Void_tile
                return False
        if len(pos) == 4: # Fall
            if self.state[pos[0]][pos[1]] == 0 or self.state[pos[2]][pos[3]] == 0:
                return False
        return True
        
    def is_right_legal(self):
        pos = self.if_right()
        if len(pos) == 2:
            if self.state[pos[0]][pos[1]] == 0 : # Void_tile
                return False
        if len(pos) == 4: # Fall
            if self.state[pos[0]][pos[1]] == 0 or self.state[pos[2]][pos[3]] == 0:
                return False
        return True

    def list_legal_moves(self):
        legal_moves = []
        if self.is_up_legal():
            legal_moves.append("W")
        if self.is_down_legal():
            legal_moves.append("S")
        if self.is_left_legal():
            legal_moves.append("A")
        if self.is_right_legal():
            legal_moves.append("D")
        return legal_moves
    
    def find_finish_state(self):
        for i in range(400):
            if self.state[i // 20][i % 20] == 7:
                return (i // 20, i % 20)

    # Method : show_state(), displays the state as the board, tile descriptions are described
    def show_state(self):
        for i in range(20):
            print(self.state[i])
        print("Current position :", self.pos)
    
    #Method : pos(), shows the position of the block
    def position(self):
        return self.pos
    
    # Method : up(), move the block up
    def up(self):
        if self.is_up_legal():
            if self.state_block == "STAND": # The block is standing
                # Look at 2 tiles above it
                x, y = self.pos[0], self.pos[1]
                self.pos = (x - 1, y, x - 2, y)
                self.state_block = "FALL"
            elif self.state_block == "FALL":
                # Fall, up will remain the state fall
                x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[2], self.pos[3]
                if x1 == x2:
                    x1 -= 1
                    x2 -= 1
                    self.pos = (x1, y1, x2, y2)
                else: # Fall, up will make the block stand
                    if x1 - 1 == x2 - 2:
                        self.pos = (x1 - 1, y1)
                    else:
                        self.pos = (x1 - 2, y1)
                    self.state_block = "STAND"
        else:
            print("That move is illegal")

    # Method : if_up(), return a coordinate if the move is legal, None if it is illegal
    def if_up(self):
        if self.state_block == "STAND": # The block is standing
            # Look at 2 tiles above it
            x, y = self.pos[0], self.pos[1]
            return (x - 1, y, x - 2, y)
        elif self.state_block == "FALL":
            # Fall, up will remain the state fall
            x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[2], self.pos[3]
            if x1 == x2:
                x1 -= 1
                x2 -= 1
                return (x1, y1, x2, y2)
            else: # Fall, up will make the block stand
                if x1 - 1 == x2 - 2:
                    return (x1 - 1, y1)
                else:
                    return (x1 - 2, y1)

    # Method : down(), move the block down
    def down(self):
        if self.is_down_legal():
            if self.state_block == "STAND": # The block is standing
                # Look at 2 tiles below it
                x, y = self.pos[0], self.pos[1]
                self.pos = (x + 1, y, x + 2, y)
                self.state_block = "FALL"
            elif self.state_block == "FALL":
                # Fall, up will remain the state fall
                x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[2], self.pos[3]
                if x1 == x2:
                    x1 += 1
                    x2 += 1
                    self.pos = (x1, y1, x2, y2)
                else: # Fall, up will make the block stand
                    if x1 + 1 == x2 + 2:
                        self.pos = (x1 + 1, y1)
                    else:
                        self.pos = (x1 + 2, y1)
                    self.state_block = "STAND"
        else:
            print("That move is illegal")
    
    # Method : if_down() : return a coordinate if the move is legal, None if the move is illegal
    def if_down(self):
        if self.state_block == "STAND": # The block is standing
            # Look at 2 tiles below it
            x, y = self.pos[0], self.pos[1]
            return (x + 1, y, x + 2, y)
        elif self.state_block == "FALL":
            # Fall, up will remain the state fall
            x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[2], self.pos[3]
            if x1 == x2:
                x1 += 1
                x2 += 1
                return (x1, y1, x2, y2)
            else: # Fall, up will make the block stand
                if x1 + 1 == x2 + 2:
                    return (x1 + 1, y1)
                else:
                    return (x1 + 2, y1)

    # Method : left(), move the block to the left : <--
    def left(self):
        if self.is_left_legal():
            if self.state_block == "STAND": # The block is standing
                # Look at 2 tiles on the left of it
                x, y = self.pos[0], self.pos[1]
                self.pos = (x, y - 1, x, y - 2)
                self.state_block = "FALL"
            elif self.state_block == "FALL":
                # Fall, up will remain the state fall
                x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[2], self.pos[3]
                if y1 == y2:
                    y1 -= 1
                    y2 -= 1
                    self.pos = (x1, y1, x2, y2)
                else: # Fall, up will make the block stand
                    if y1 - 1 == y2 - 2:
                        self.pos = (x1, y1 - 1)
                    else:
                        self.pos = (x1, y1 - 2)
                    self.state_block = "STAND"
        else:
            print("That move is illegal")
    
    # Method : if_left() : return a coordinate if the move is legal, None if the move is illegal
    def if_left(self):
        if self.state_block == "STAND": # The block is standing
            # Look at 2 tiles on the left of it
            x, y = self.pos[0], self.pos[1]
            return (x, y - 1, x, y - 2)
        elif self.state_block == "FALL":
            # Fall, up will remain the state fall
            x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[2], self.pos[3]
            if y1 == y2:
                y1 -= 1
                y2 -= 1
                return (x1, y1, x2, y2)
            else: # Fall, up will make the block stand
                if y1 - 1 == y2 - 2:
                    return (x1, y1 - 1)
                else:
                    return (x1, y1 - 2)

    # Method : right(), move the block to the right : -->
    def right(self):
        if self.is_right_legal():
            if self.state_block == "STAND": # The block is standing
                # Look at 2 tiles on the right of it
                x, y = self.pos[0], self.pos[1]
                self.pos = (x, y + 1, x, y + 2)
                self.state_block = "FALL"
            elif self.state_block == "FALL":
                # Fall, up will remain the state fall
                x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[2], self.pos[3]
                if y1 == y2:
                    y1 += 1
                    y2 += 1
                    self.pos = (x1, y1, x2, y2)
                else: # Fall, up will make the block stand
                    if y1 + 1 == y2 + 2:
                        self.pos = (x1, y1 + 1)
                    else:
                        self.pos = (x1, y1 + 2)
                    self.state_block = "STAND"
        else:
            print("That move is illegal")

    # Method : if_right(), move the block to the right : -->
    def if_right(self):
        if self.state_block == "STAND": # The block is standing
            # Look at 2 tiles on the right of it
            x, y = self.pos[0], self.pos[1]
            return (x, y + 1, x, y + 2)
        elif self.state_block == "FALL":
            # Fall, up will remain the state fall
            x1, y1, x2, y2 = self.pos[0], self.pos[1], self.pos[2], self.pos[3]
            if y1 == y2:
                y1 += 1
                y2 += 1
                return (x1, y1, x2, y2)
            else: # Fall, up will make the block stand
                if y1 + 1 == y2 + 2:
                    return (x1, y1 + 1)
                else:
                    return (x1, y1 + 2)

    
    # Method : move_in_order() : make the block move in order
    def move_in_order(self, move_str: str):
        for i in move_str:
            if i == "W":
                self.up()
            if i == "S":
                self.down()
            if i == "A":
                self.left()
            if i == "D":
                self.right()
            time.sleep(0.5)
        print("Done moving")
    # def swap(self):
    #     pass
