# Notation

| No   | Propertiy          | Value        |
| ---- | ------------------ | ------------ |
| 1    | Board size         | $20\times20$ |
| 2    | Void tile          | 0            |
| 3    | Normal tile        | 1            |
| 4    | Bridge tile - soft | 2            |
| 5    | Bridge tile - hard | 3            |
| 6    | Bridge             | Alphabet     |
| 7    | Soft tile          | 5            |
| 9    | Finish tile        | 7            |

Define the first line : `[level_ID] [start_X] [start_Y]`

+ `level_ID` : the identifier number of the level
+ `start_X` : the starting position in rows
+ `start_Y` : the starting position in columns

Define the second line : `[number_of_bridge] [bridge1_x] [bridge1_y] [Alphabet] ...`

+ `number_of_bridge` : the name says itself
+ `bridge<i>_x,y`    : define the coordinates of the bridge tiles
+ `[Alphabet]`       : define which bridge belong to which bridge tiles

Define 

