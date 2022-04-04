class Board:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.board = {}
        for row in range(self.row):
            for column in range(self.column):
                self.board[row, column] = "free"

    def __str__(self):
        return "*"

    def put_queen(self, row, column):
        self.board[row, column] = "queen"

    def set_forbidden_tiles(self):
        positions_of_queens = [k for k, v in self.board.items() if v == 'queen']
        for g in positions_of_queens:
            for n in range(8):
                # rows of the queens: free->forbidden
                if self.board[g[0], n] == "free":
                    self.board[g[0], n] = "forbidden"
                # columns of the queens: free->forbidden
                if self.board[n, g[1]] == "free":
                    self.board[n, g[1]] = "forbidden"
                # left_and_up axes of the queens: free->forbidden
                if g[0] - n >= 0 and g[1] - n >= 0 and self.board[g[0] - n, g[1] - n] == "free":
                    self.board[g[0] - n, g[1] - n] = "forbidden"
                # left_and_down axes of the queens: free->forbidden
                if g[0] + n <= 7 and g[1] - n >= 0 and self.board[g[0] + n, g[1] - n] == "free":
                    self.board[g[0] + n, g[1] - n] = "forbidden"
                # right_and_up axes of the queens: free->forbidden
                if g[0] - n >= 0 and g[1] + n >= 7 and self.board[g[0] - n, g[1] + n] == "free":
                    self.board[g[0] - n, g[1] + n] = "forbidden"
                # right_and_down axes of the queens: free->forbidden
                if g[0] + n <= 7 and g[1] + n <= 7 and self.board[g[0] + n, g[1] + n] == "free":
                    self.board[g[0] + n, g[1] + n] = "forbidden"

    def get_free_tiles(self):
        positions_of_free_tiles = [k for k, v in self.board.items() if v == 'free']
        return positions_of_free_tiles


b = Board(8, 8)
b.put_queen(3, 4)
b.set_forbidden_tiles()
print(b.get_free_tiles())


