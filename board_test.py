from read_level import level_list
import time
from string import ascii_uppercase
import copy
import math
import random

# Game() class, with attributes :
# + id          : defined the id of the level
# + start       : the starting position on the board, FIXED
# + pos         : the current position on the board, which will be :
#   - (x, y) if the block is standing
#   - (x1, y1, x2, y2) if the block is falling or the block is splitted into two halves
# + state_block : indicates the state of the block, consists of : "FALL", "STAND" or "DIVIDED"
# + state       : the 20x20 board, notations of the tiles are described
# + goal        : the tile that you need to move the block to, undefined in init
# + level       : just another copy of the level, to do Reset() function

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
        self.level = level
        self.id, self.start, self.state, self.bridge_list = level
        self.pos = self.start
        self.state_block = "STAND"
        self.goal = self.find_finish_state()
        print("The goal is at :", self.goal, ". Good luck !")

    def is_up_legal(self):
        pos = self.if_up()
        if len(pos) == 2:
            if self.state[pos[0]][pos[1]] == 0 : # Void_tile
                return False
            if str(self.state[pos[0]][pos[1]]) in ascii_uppercase: # Stand in the bridge
                # Find where the bridge tiles belong to
                bridge_id = self.state[pos[0]][pos[1]]
                for i in self.bridge_list:
                    if i[2] == bridge_id and i[3] == 0: # Inactive bridge
                        return False
            
            if self.state[pos[0]][pos[1]] == 5: # Stand on a soft tile
                return False
        if len(pos) == 4: # Fall
            if self.state[pos[0]][pos[1]] == 0 or self.state[pos[2]][pos[3]] == 0:
                return False
            if str(self.state[pos[0]][pos[1]]) in ascii_uppercase or str(self.state[pos[2]][pos[3]]) in ascii_uppercase: # Stand in the bridge
                # Find where the bridge tiles belong to
                bridge_id_1 = self.state[pos[0]][pos[1]]
                for i in self.bridge_list:
                    if i[2] == bridge_id_1 and i[3] == 0: # Inactive bridge
                        return False
                bridge_id_2 = self.state[pos[2]][pos[3]]
                for i in self.bridge_list:
                    if i[2] == bridge_id_2 and i[3] == 0: # Inactive bridge
                        return False
        return True
            

    def is_down_legal(self):
        pos = self.if_down()
        if len(pos) == 2:
            if self.state[pos[0]][pos[1]] == 0 : # Void_tile
                return False
            if str(self.state[pos[0]][pos[1]]) in ascii_uppercase: # Stand in the bridge
                # Find where the bridge tiles belong to
                bridge_id = self.state[pos[0]][pos[1]]
                for i in self.bridge_list:
                    if i[2] == bridge_id and i[3] == 0: # Inactive bridge
                        return False
            if self.state[pos[0]][pos[1]] == 5: # Stand on a soft tile
                return False
        if len(pos) == 4: # Fall
            if self.state[pos[0]][pos[1]] == 0 or self.state[pos[2]][pos[3]] == 0:
                return False
            if str(self.state[pos[0]][pos[1]]) in ascii_uppercase or str(self.state[pos[2]][pos[3]]) in ascii_uppercase: # Stand in the bridge
                # Find where the bridge tiles belong to
                bridge_id_1 = self.state[pos[0]][pos[1]]
                for i in self.bridge_list:
                    if i[2] == bridge_id_1 and i[3] == 0: # Inactive bridge
                        return False
                bridge_id_2 = self.state[pos[2]][pos[3]]
                for i in self.bridge_list:
                    if i[2] == bridge_id_2 and i[3] == 0: # Inactive bridge
                        return False
        return True
    
    def is_left_legal(self):
        pos = self.if_left()
        if len(pos) == 2:
            if self.state[pos[0]][pos[1]] == 0 : # Void_tile
                return False
            if str(self.state[pos[0]][pos[1]]) in ascii_uppercase: # Stand in the bridge
                # Find where the bridge tiles belong to
                bridge_id = self.state[pos[0]][pos[1]]
                for i in self.bridge_list:
                    if i[2] == bridge_id and i[3] == 0: # Inactive bridge
                        return False
            if self.state[pos[0]][pos[1]] == 5: # Stand on a soft tile
                return False
        if len(pos) == 4: # Fall
            if self.state[pos[0]][pos[1]] == 0 or self.state[pos[2]][pos[3]] == 0:
                return False
            if str(self.state[pos[0]][pos[1]]) in ascii_uppercase or str(self.state[pos[2]][pos[3]]) in ascii_uppercase: # Stand in the bridge
                # Find where the bridge tiles belong to
                bridge_id_1 = self.state[pos[0]][pos[1]]
                for i in self.bridge_list:
                    if i[2] == bridge_id_1 and i[3] == 0: # Inactive bridge
                        return False
                bridge_id_2 = self.state[pos[2]][pos[3]]
                for i in self.bridge_list:
                    if i[2] == bridge_id_2 and i[3] == 0: # Inactive bridge
                        return False
        return True
        
    def is_right_legal(self):
        pos = self.if_right()
        if len(pos) == 2:
            if self.state[pos[0]][pos[1]] == 0 : # Void_tile
                return False
            if str(self.state[pos[0]][pos[1]]) in ascii_uppercase: # Stand in the bridge
                # Find where the bridge tiles belong to
                bridge_id = self.state[pos[0]][pos[1]]
                for i in self.bridge_list:
                    if i[2] == bridge_id and i[3] == 0: # Inactive bridge
                        return False
            if self.state[pos[0]][pos[1]] == 5: # Stand on a soft tile
                return False
        if len(pos) == 4: # Fall
            if self.state[pos[0]][pos[1]] == 0 or self.state[pos[2]][pos[3]] == 0:
                return False
            if str(self.state[pos[0]][pos[1]]) in ascii_uppercase or str(self.state[pos[2]][pos[3]]) in ascii_uppercase: # Stand in the bridge
                # Find where the bridge tiles belong to
                bridge_id_1 = self.state[pos[0]][pos[1]]
                for i in self.bridge_list:
                    if i[2] == bridge_id_1 and i[3] == 0: # Inactive bridge
                        return False
                bridge_id_2 = self.state[pos[2]][pos[3]]
                for i in self.bridge_list:
                    if i[2] == bridge_id_2 and i[3] == 0: # Inactive bridge
                        return False
        return True

    def list_legal_moves(self):
        legal_moves = []
        if self.is_right_legal():
            legal_moves.append("D")
        if self.is_down_legal():
            legal_moves.append("S")
        if self.is_up_legal():
            legal_moves.append("W")
        if self.is_left_legal():
            legal_moves.append("A")
        return legal_moves
    
    def find_finish_state(self):
        for i in range(400):
            if self.state[i // 20][i % 20] == 7:
                return (i // 20, i % 20)
    
    # Method : step_on_special_tiles() : executes actions if the block is standing on some special tiles
    def step_on_special_tiles(self):
        # Traverse the list of bridge tiles
        for i in range (len(self.bridge_list)):
            x, y = self.bridge_list[i][0], self.bridge_list[i][1]
            # Check if the bridge tile is soft 
            if self.state[x][y] == 2:
                # Just one part of the block standing on it is enough
                if self.state_block == "STAND" and self.pos[0] == x and self.pos[1] == y:
                    temp = list(self.bridge_list[i])
                    if temp[3] == 0:
                        temp[3] = 1
                        self.bridge_list[i] = tuple(temp)
                    else:
                        temp[3] = 0
                        self.bridge_list[i] = tuple(temp)
                if self.state_block == "FALL":
                    if (self.pos[0] == x and self.pos[1] == y) or (self.pos[2] == x and self.pos[3] == y):
                        temp = list(self.bridge_list[i])
                        if temp[3] == 0:
                            temp[3] = 1
                            self.bridge_list[i] = tuple(temp)
                        else:
                            temp[3] = 0
                            self.bridge_list[i] = tuple(temp)
            # Check if the bridge tile is hard
            if self.state[x][y] == 3:
                # The block must stand on the tile
                if self.state_block == "STAND" and (self.pos[0] == x and self.pos[1] == y):
                    temp = list(self.bridge_list[i])
                    if temp[3] == 0:
                        temp[3] = 1
                        self.bridge_list[i] = tuple(temp)
                    else:
                        temp[3] = 0
                        self.bridge_list[i] = tuple(temp)
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
            self.step_on_special_tiles()
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
            self.step_on_special_tiles()
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
            self.step_on_special_tiles()
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
            self.step_on_special_tiles()
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

    def reset(self):
        print("Level resetted !")
        self.id, self.start, self.state = self.level
        self.pos = self.start
        self.state_block = "STAND"
        self.goal = self.find_finish_state()
        print("The goal is at :", self.goal, ". Good luck !")
    
    def check_win(self):
        if (self.state_block == "STAND" and self.pos == self.goal):
            return True
        else:
            return False

    # def swap(self):
    #     pass

#Search using BFS 
class BFS(Game):
    def __init__(self,level,move="") -> None:
        super().__init__(level)
        self.g = 0
        self.move = move
        self.soft = False
        self.hard = False

    #Checking if the map has bridge or not
    def has_soft_bridge(self):
        for i in range(400):
            if self.state[i // 20][i % 20] == 2:
                return (i // 20, i % 20)
        return None
    def has_hard_bridge(self):
        for i in range(400):
            if self.state[i // 20][i % 20] == 3:
                return (i // 20, i % 20)
        return None
    
    def is_standing_on_soft_bridge_button(self):
        b = self.has_soft_bridge()
        if b is None:
            return False
        if b[0] == self.pos[0] and b[1] == self.pos[1]:
            return True
        elif len(self.pos) == 4:
            if b[0] == self.pos[2] and b[1] == self.pos[3]:
                return True
        return False
    def is_standing_on_hard_bridge_button(self):
        b = self.has_hard_bridge()
        if b is None:
            return False
        if self.state_block == "STAND" and b[0] == self.pos[0] and b[1] == self.pos[1]:
            return True
        return False
    
    #-----------------------
    #   Redefine 4 method: left,right,up,down
    #   In class game : only change pos of block
    #   Here : no need checking legal, return block itself
    #-----------------------
    # Method : left(), move the block to the left : <--
    def left(self):
        if self.state_block == "STAND":  # The block is standing
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
            else:  # Fall, up will make the block stand
                if y1 - 1 == y2 - 2:
                    self.pos = (x1, y1 - 1)
                else:
                    self.pos = (x1, y1 - 2)
                self.state_block = "STAND"
        self.step_on_special_tiles()
        return self

    # Method : right(), move the block to the right : -->
    def right(self):
        if self.state_block == "STAND":  # The block is standing
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
            else:  # Fall, up will make the block stand
                if y1 + 1 == y2 + 2:
                    self.pos = (x1, y1 + 1)
                else:
                    self.pos = (x1, y1 + 2)
                self.state_block = "STAND"
        self.step_on_special_tiles()
        return self

    # Method : down(), move the block down
    def down(self):
        if self.state_block == "STAND":  # The block is standing
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
            else:  # Fall, up will make the block stand
                if x1 + 1 == x2 + 2:
                    self.pos = (x1 + 1, y1)
                else:
                    self.pos = (x1 + 2, y1)
                self.state_block = "STAND"
        self.step_on_special_tiles()
        return self

    # Method : up(), move the block up
    def up(self):
        if self.state_block == "STAND":  # The block is standing
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
            else:  # Fall, up will make the block stand
                if x1 - 1 == x2 - 2:
                    self.pos = (x1 - 1, y1)
                else:
                    self.pos = (x1 - 2, y1)
                self.state_block = "STAND"
        self.step_on_special_tiles()
        return self

    # These 2 find method: search for block position in open_list and close_list
    # return index if found, None otherwise
    def find_in_open(self,open_list):
        for index,item in enumerate(open_list):
            if item.pos == self.pos:
                return index
        return None
    def find_in_close(self,close_list):
        for index,item in enumerate(close_list):
            if item.pos == self.pos:
                return index
        return None

    # Method used to solve problem using BFS
    # return a string of movement
    def solve(self):
        # Create 2 list for unvisited and visited node
        open_list = []
        close_list = []
        # First add start node
        open_list.append(self)

        #if bridge exist, first try to touch bridge
        soft_bridge = self.has_soft_bridge()
        hard_bridge = self.has_hard_bridge()
        if soft_bridge is not None:
            self.soft = True
        
        if hard_bridge is not None:
            self.hard = True
        
        while len(open_list) != 0:
            # Take the first node in unvisited list
            # Visit it and add to visited list
            currCell = open_list[0]
            open_list.pop(0)
            close_list.append(currCell)
            # Check winning condition
            if currCell.check_win():
                return currCell.move
            
            # List all legal move
            legal_move = currCell.list_legal_moves()
            for m in legal_move:
                if m == "D":
                    #have to copy currcell to nextmove, to avoid currcell change after call right() func
                    nextMove = copy.deepcopy(currCell)
                    nextMove = nextMove.right()
                    nextMove.g = currCell.g + 1
                    nextMove.move = currCell.move + "D"
                if m == "S":
                    nextMove = copy.deepcopy(currCell)
                    nextMove = nextMove.down()
                    nextMove.g = currCell.g + 1
                    nextMove.move = currCell.move + "S"
                if m == "A":
                    nextMove = copy.deepcopy(currCell)
                    nextMove = nextMove.left()
                    nextMove.g = currCell.g + 1
                    nextMove.move = currCell.move + "A"
                if m == "W":
                    nextMove = copy.deepcopy(currCell)
                    nextMove = nextMove.up()
                    nextMove.g = currCell.g + 1
                    nextMove.move = currCell.move + "W"
                if nextMove.is_standing_on_soft_bridge_button():
                    nextMove.soft = not nextMove.soft
                if nextMove.is_standing_on_hard_bridge_button():
                    nextMove.hard = not nextMove.hard
                # For each legal move, consider its position
                open_idx = nextMove.find_in_open(open_list)
                close_idx = nextMove.find_in_close(close_list)
                # Node is not exist in both list -> add to unvisited list
                if open_idx == None and close_idx == None:
                    open_list.append(nextMove)
                # Node is already exist in unvisited list and its cost is larger -> replace node
                elif open_idx != None:
                    if open_list[open_idx].soft == True and nextMove.soft == False:
                        open_list[open_idx] = nextMove
                        continue
                    if open_list[open_idx].hard == True and nextMove.hard == False:
                        open_list[open_idx] = nextMove
                        continue
                    if open_list[open_idx].g > nextMove.g:
                        open_list[open_idx] = nextMove
                        continue
                elif close_idx != None:
                    if close_list[close_idx].soft == True and nextMove.soft == False:
                        open_list.append(nextMove)
                        close_list.pop(close_idx)
                        continue
                    if close_list[close_idx].hard == True and nextMove.hard == False:
                        open_list.append(nextMove)
                        close_list.pop(close_idx)
                        continue
        return None

# Search using A*
class aStar(BFS):
    def __init__(self, level, move="") -> None:
        super().__init__(level,move)
        self.f = self.heuristic_func()

    # Heuristic function: Chebyshev
    def heuristic_func(self):
        x1_dis = abs(self.pos[0] - self.goal[0])
        y1_dis = abs(self.pos[1] - self.goal[1])
        if (len(self.pos) == 2):
            # Standing state
            return max(x1_dis, y1_dis)
        else:
            # Lying state, calculate more distance
            x2_dis = abs(self.pos[2] - self.goal[0])
            y2_dis = abs(self.pos[3] - self.goal[1])
            return max(max(x1_dis, y1_dis), max(x2_dis, y2_dis))

    # Method used to solve problem using A*
    # return a string of movement
    def solve(self):
        open_list = []
        close_list = []
        open_list.append(self)

        #if bridge exist, first try to touch bridge
        soft_bridge = self.has_soft_bridge()
        hard_bridge = self.has_hard_bridge()
        if soft_bridge is not None:
            self.soft = True
        if hard_bridge is not None:
            self.hard = True

        while len(open_list) != 0:
            # In A*, the node in unvisited list is visited in increasing order
            # Node with the smallest cost f = g + h, is pop out first
            currCell = open_list[0]
            currIdx = 0
            for index,item in enumerate(open_list):
                if item.f < currCell.f:
                    currIdx = index
                    currCell = item
            open_list.pop(currIdx)
            close_list.append(currCell)

            # Check winning condition
            if currCell.check_win():
                return currCell.move
            
            # List all legal move
            legal_move = currCell.list_legal_moves()
            for m in legal_move:
                if m == "D":
                    #have to copy currcell to nextmove, to avoid currcell change after call right() func
                    nextMove = copy.deepcopy(currCell)
                    nextMove = nextMove.right()
                    nextMove.g = currCell.g + 1
                    nextMove.f = nextMove.g + nextMove.heuristic_func()
                    nextMove.move = currCell.move + "D"
                if m == "S":
                    nextMove = copy.deepcopy(currCell)
                    nextMove = nextMove.down()
                    nextMove.g = currCell.g + 1
                    nextMove.f = nextMove.g + nextMove.heuristic_func()
                    nextMove.move = currCell.move + "S"
                if m == "A":
                    nextMove = copy.deepcopy(currCell)
                    nextMove = nextMove.left()
                    nextMove.g = currCell.g + 1
                    nextMove.f = nextMove.g + nextMove.heuristic_func()
                    nextMove.move = currCell.move + "A"
                if m == "W":
                    nextMove = copy.deepcopy(currCell)
                    nextMove = nextMove.up()
                    nextMove.g = currCell.g + 1
                    nextMove.f = nextMove.g + nextMove.heuristic_func()
                    nextMove.move = currCell.move + "W"
                if nextMove.is_standing_on_soft_bridge_button():
                    nextMove.soft = not nextMove.soft
                if nextMove.is_standing_on_hard_bridge_button():
                    nextMove.hard = not nextMove.hard
                # For each legal move, consider its position
                open_idx = nextMove.find_in_open(open_list)
                close_idx = nextMove.find_in_close(close_list)
                # Node is not exist in both list -> add to unvisited list
                if open_idx == None and close_idx == None:
                    open_list.append(nextMove)
                # Node existed in unvisited list and its cost is larger -> replace node
                elif open_idx != None:
                    if open_list[open_idx].soft == True and nextMove.soft == False:
                        open_list[open_idx] = nextMove
                        continue
                    if open_list[open_idx].hard == True and nextMove.hard == False:
                        open_list[open_idx] = nextMove
                        continue
                    if open_list[open_idx].f > nextMove.f:
                        open_list[open_idx] = nextMove
                        continue
                # Node existed in close list and its cost is larger -> add to open_list, remove from close_list
                elif close_idx != None:
                    if close_list[close_idx].soft == True and nextMove.soft == False:
                        open_list.append(nextMove)
                        close_list.pop(close_idx)
                        continue
                    if close_list[close_idx].hard == True and nextMove.hard == False:
                        open_list.append(nextMove)
                        close_list.pop(close_idx)
                        continue
                    if close_list[close_idx].f > nextMove.f:
                        open_list.append(nextMove)
                        close_list.pop(close_idx)
                        continue
        return None

class MCTS(Game):
    def __init__(self, level) -> None:
        super().__init__(level)
        self.childen = []
        self.parent = None
        self.visited = 0
        self.reward = 0
        self.possible_action = self.get_neighbor()

    # Base on Euclidian distance
    def cal_reward(self):  # ->>>>get reward
        if self.check_win():
            return 20
        x_goal, y_goal = self.goal
        x1, y1 = [self.pos[0], self.pos[1]]
        if len(self.pos) == 2:
            return 20 - math.sqrt((x1-x_goal)**2 + (y1-y_goal)**2)
        if len(self.pos) == 4:
            x2, y2 = [self.pos[2], self.pos[3]]
            dis1 = math.sqrt((x1-x_goal)**2 + (y1-y_goal)**2)
            dis2 = math.sqrt((x2-x_goal)**2 + (y2-y_goal)**2)
            return 20 - 0.5*(dis1+dis2)

    # Expand all legal move from a node
    def get_neighbor(self):
        result = []
        legal_move = self.list_legal_moves()
        for m in legal_move:
            if m == "D":
                nextMove = copy.deepcopy(self)
                nextMove = nextMove.right()
            if m == "S":
                nextMove = copy.deepcopy(self)
                nextMove = nextMove.down()
            if m == "A":
                nextMove = copy.deepcopy(self)
                nextMove = nextMove.left()
            if m == "W":
                nextMove = copy.deepcopy(self)
                nextMove = nextMove.up()
            nextMove.parent = self
            result.append(nextMove)
        return result

    def backup(self):
        while self is not None:
            self.reward += self.cal_reward()
            self.visited += 1
            self = self.parent

    def best_neighbor(self, exploration_param = 1.4):
        best_neighbor = None
        best_score = -float("inf")
        for node in self.childen():
            exploitation_score = node.reward/node.visited
            exploration_score = exploration_param * math.sqrt(math.log(self.visited)/node.visited)
            total_score =  exploitation_score + exploration_score
            if total_score > best_score:
                best_score = total_score
                best_neighbor = node
        return best_neighbor
    
    def default_policy(self):
        node = copy.deepcopy(self)
        while not node.check_win() and len(node.possible_action) > 0:
            if len(node.possible_action) > 0:
                n = random.randint(0,len(self.possible_action)-1)
                node = node.possible_action[n]
        return node.cal_reward()

    def select_untried_action(self):
        while not self.check_win():
            untried = list(set(self.possible_action) - set(self.childen))
            if len(untried) > 0:
                return untried[0]
            else:
                return None
        return None   
    def tree_policy(self):
        while not self.check_win():
            node = self.select_untried_action()
            if node is not None:
                self.childen.append(node)
                return node
            else:
                node = self.best_neighbor()
        return self            
    def MCTS(self):
        while not self.check_win():
            node = self.select_untried_action()
            if node is not None:
                node.parent = self
                node.visited = self.visited + 1
                node.reward = node.cal_reward()
                self.childen.append(node)
            else:
                return self.best_neighbor()
        return self.best_neighbor()
    def solve(self):
        finish = self
        result = []
        while not finish.check_win():
            finish = finish.MCTS()
        while finish.parent is not None:
            result.append(finish.pos)
            finish = finish.parent
        return result
