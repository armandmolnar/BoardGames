def create_board(row=8, col=8):
    board = {}
    for row in range(row):
        for column in range(col):
            board[row, column] = "free"
    return board

#def get_forbidden_grids(board):


initial_board = create_board()
initial_board[2, 2] = "queen"
positions_of_queens = [k for k, v in initial_board.items() if v == 'queen']
for g in positions_of_queens:
    for n in range(8):
        # rows of the queens: free->forbidden
        if initial_board[g[0], n] == "free":
            initial_board[g[0], n] = "forbidden"
        # columns of the queens: free->forbidden
        if initial_board[n, g[1]] == "free":
            initial_board[n, g[1]] = "forbidden"
        # left_and_up axes of the queens: free->forbidden
        if g[0] - n >= 0 and g[1] - n >= 0 and initial_board[g[0] - n, g[1] - n] == "free":
            initial_board[g[0] - n, g[1] - n] = "forbidden"
        # left_and_down axes of the queens: free->forbidden
        if g[0] + n <= 7 and g[1] - n >= 0 and initial_board[g[0] + n, g[1] - n] == "free":
            initial_board[g[0] + n, g[1] - n] = "forbidden"
        # right_and_up axes of the queens: free->forbidden
        if g[0] - n >= 0 and g[1] + n >=7 and initial_board[g[0] - n, g[1] + n] == "free":
            initial_board[g[0] - n, g[1] + n] = "forbidden"
        # right_and_down axes of the queens: free->forbidden
        if g[0] + n <= 7 and g[1] + n <= 7 and initial_board[g[0] + n, g[1] + n] == "free":
            initial_board[g[0] + n, g[1] + n] = "forbidden"




positions_of_not_free = [k for k, v in initial_board.items() if v != 'free']
print(positions_of_not_free)

"""
# print(keys[0][0])

# todo forbidden legyen átlósan is
"""


