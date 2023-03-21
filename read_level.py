def load_level(id : int):
    board = [[None for _ in range(20)] for _ in range(20)]
    filename = "Assets/Board/Levels/" + str(id) + ".txt"
    f = open(filename, "r")
    info = f.readline().splitlines()[0].split(" ")
    id, start_position = int(info[0]), [int(info[1]),int(info[2])]
    temp = f.readlines()
    for i in range(400):
        board[i // 20][i % 20] = int(temp[i // 20][i % 20])
    return (id, start_position, board)

level_1 = load_level(1)
# level_2 = load_level(2)
# level_3 = load_level(3)
# level_4 = load_level(4)
# level_5 = load_level(5)
# level_6 = load_level(6)
# level_7 = load_level(7)
# level_8 = load_level(8)

"""
print("Level :", id)
print("Starting position :", start)
print("Board :")
for i in range(len(board[0])):
    print(board[i])
"""