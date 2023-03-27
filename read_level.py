import string

# Function : load_level(id : int), will read the file "<id>.txt" depicting the board of that level
# Returns : + id
#           + start_position : tuple (x, y)
#           + board          : 2D list of size 20x20
def load_level(id : int):
    board = [[None for _ in range(20)] for _ in range(20)]
    filename = "Assets/Board/Levels/" + str(id) + ".txt"
    f = open(filename, "r")
    info = f.readline().splitlines()[0].split(" ")
    id, start_position = int(info[0]), (int(info[1]),int(info[2]))
    info = f.readline().splitlines()[0].split(" ")
    bridge_num = int(info[0])
    bridge_list = []
    if bridge_num != 0:
        for i in range(1,len(info), 3):
            bridge_list.append((int(info[i]), int(info[i + 1]), info[i + 2], 0))
    temp = f.readlines()
    for i in range(400):
        if temp[i // 20][i % 20] not in string.ascii_uppercase:
            board[i // 20][i % 20] = int(temp[i // 20][i % 20])
        else:
            board[i // 20][i % 20] = temp[i // 20][i % 20]
    return (id, start_position, board, bridge_list)

# level_5 = load_level(5)
# level_6 = load_level(6)
# level_7 = load_level(7)
# level_8 = load_level(8)

level_idx = [1, 2, 3, 4, 6, 13, 14]
level_list = []
for i in level_idx:
    level_list.append(load_level(i))


# print("Level :", id)
# print("Starting position :", start)
# print("Board :")
# for i in range(len(board[0])):
#     print(board[i])
