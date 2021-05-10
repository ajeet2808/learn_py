
WHITE_PAWN = "^"
EMPTY = "_"
ROOK = "R"
row = []


def print_2d(board):
    i = 0
    print("---------------------------2d--------------------------------------")
    for row in board:
        print(i,row)
        i +=1

for i in range(8):
    row.append(WHITE_PAWN)

print(row)

#list comprehension
row = [WHITE_PAWN for i in range(8)]
print(row)


squares = [x ** 2 for x in range(10)]

odds = [x for x in squares if x % 2 != 0 ]

#2D list
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
print_2d(board)

board = [[EMPTY for i in range(8)] for j in range(8)]
print_2d(board)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print_2d(board)


#############################
temps = [[0.0 for h in range(24)] for d in range(31)]
print_2d(temps)


# Three-dimensional arrays
def print_3d(list_3d):
    print("**********************************3d*************************************")
    i = 0
    for list_2d in list_3d:
        print(i,end=" ")
        i+=1
        print_2d(list_2d)

rooms = [[[False for r in range(10)] for f in range(5)] for t in range(3)]
print_3d(rooms)