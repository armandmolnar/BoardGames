def create_board(row=8, col=8):
    board = {}
    for row in range(row):
        for column in range(col):
            board[row, column] = "free"
    return board

#def get_forbidden_grids(board):


initial_board = create_board()
initial_board[1, 1] = "queen"
positions_of_queens = [k for k, v in initial_board.items() if v == 'queen']
for g in positions_of_queens:
    print(g[0])
    for c in range(8):
        if initial_board[g[0], c] == "free":
            initial_board[g[0], c] = "forbidden"
    for r in range(8):
        if initial_board[r, g[1]] == "free":
            initial_board[r, g[1]] = "forbidden"

positions_of_not_free = [k for k, v in initial_board.items() if v != 'free']
print(positions_of_not_free)

"""
# print(keys[0][0])

# todo forbidden legyen átlósan is
"""


