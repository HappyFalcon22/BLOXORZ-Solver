# BLOXOR AI SOLVER

## Notation

### Tiles number

| No   | Propertiy          | Value        |
| ---- | ------------------ | ------------ |
| 1    | Board size         | $20\times20$ |
| 2    | Void tile          | 0            |
| 3    | Normal tile        | 1            |
| 4    | Bridge tile - soft | 2            |
| 5    | Bridge tile - hard | 3            |
| 6    | Bridge             | 4            |
| 7    | Soft tile          | 5            |
| 8    | Division tile      | 6            |
| 9    | Finish tile        | 7            |

### Move keyboard

| No   | Key   | Action          |
| ---- | ----- | --------------- |
| 1    | W     | Up              |
| 2    | S     | Down            |
| 3    | A     | Left            |
| 4    | D     | Right           |
| 5    | Space | Reset the level |

## File board_test.py

Includes the main class : `Game`

### Parameters

+ `id` : the identifier of the game (which is the level number btw)
+ `start` : the starting position of the block, ***FIXED***, notation : `(x,y)`
+ `state` : which is the board of the size $20\times20$, each element in the board represents a tile by number.
+ `pos` : the current position of the block on the board
	+ If the block is ***STANDING*** : `pos = (x,y)`
	+ If the block is ***FALLING***  (don't question my English naming) : `pos = (x1, y1, x2, y2)`
+ `state_block` : Indicates the current state of the block such as `FALL`, `STAND` or `DIVIDED`
+ `goal` : the tile that you aim to land the block into, notation is just like the `start` : `pos = (x,y)`
+ `level` : a copy of the level itself when you do ***RESET*** the level.

### Methods

+ `is_up_legal(), is_down_legal(), is_left_legal(), is_right_legal()` : bool functions returns whether a move is legal or not
+ `up(), down(), left(), right()` : void functions, move the block. If the move is illegal, the block will not move and will print out `That move is illegal`.
+ `if_up(), if_down(), if_left(), if_right()` : functions, return :
	+ A tuple representing the position if the block make a corresponding move.
	+ `None` if the corresponding move is illegal.
+ `find_finish_state()` : a function to find the finish tile on the board, called in `__init__`
+ `check_win()` : check if the block is standing in the finish tile.
+ `position()` : returns the current position of the block
+ `show_state()` : print the current state
+ `reset()` : reset the board.
+ `list_legal_move()` return a list of legal moves in the current state, return a `[None]` if there are no moves.
	+ Example : `["W", "A", "D"]` shows that there are 3 legal moves in current state.
+ `move_in_order(move_str : str)` : takes in a string of moves and executes the string.
	+ Example : `"WSADSD"` performs : `Up -> Down -> Left -> Right -> Down -> Right`

## File main.py

The main Python file to draw and animate the game, will annotate later.

## Tile Properties

### 1. Bridge Tile - Soft

Land on the tile to raise or lower the bridge (can land on the tile in any manner, including standing on it or falling on it)

### 2. Bridge Tile - Hard

Must stand on the tile to raise or lower the bridge

### 3. Bridge

Just like the normal tile except that it can be controlled by the Bridge Tile (Soft or Hard)

### 4. Soft Tile

These tile are fragile, can only stand still if the block in the `FALL` state

### 5. Divvy Tile

`STAND` on the tile to divide the block into 2 pieces of $1\times1$, which can be swapped by the key `SPACE`.
