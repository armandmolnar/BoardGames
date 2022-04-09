class Board:
    def __init__(self):
        self.row = 8
        self.column = 8
        self.board = {}
        for row in range(self.row):
            for column in range(self.column):
                self.board[row, column] = "free"

    def __str__(self):
        b = ""
        for r in range(self.row):
            for c in range(self.column):
                if self.board[r, c] == "free":
                    b = b + ". "
                elif self.board[r, c] == "queen":
                    b = b + "Q "
                elif self.board[r, c] == "forbidden":
                    b = b + "x "
            b = b + "\n"
        return b

    def put_queen(self, row, column):
        if self.board[row, column] == "free":
            self.board[row, column] = "queen"

    def remove_queen(self, row, column):
        if self.board[row, column] == "queen":
            self.board[row, column] = "free"

    def clear_forbidden_tiles(self):
        rows = self.row
        for r in range(rows):
            for c in range(rows):
                if self.board[r, c] == "forbidden":
                    self.board[r, c] = "free"

    def set_forbidden_tiles(self):
        positions_of_queens = [k for k, v in self.board.items() if v == "queen"]
        rows = self.row
        for x, y in positions_of_queens:
            for n in range(rows):
                # rows of the queens: free->forbidden
                if self.board[x, n] == "free":
                    self.board[x, n] = "forbidden"
                # columns of the queens: free->forbidden
                if self.board[n, y] == "free":
                    self.board[n, y] = "forbidden"
                # left_and_up axes of the queens: free->forbidden
                if (x - n) >= 0 and (y - n) >= 0 and self.board[x - n, y - n] == "free":
                    self.board[x - n, y - n] = "forbidden"
                # left_and_down axes of the queens: free->forbidden
                if (x + n) < rows and (y - n) >= 0 and self.board[x + n, y - n] == "free":
                    self.board[x + n, y - n] = "forbidden"
                # right_and_up axes of the queens: free->forbidden
                if (x - n) >= 0 and (y + n) < rows and self.board[x - n, y + n] == "free":
                    self.board[x - n, y + n] = "forbidden"
                # right_and_down axes of the queens: free->forbidden
                if (x + n) < rows and (y + n) < rows and self.board[x + n, y + n] == "free":
                    self.board[x + n, y + n] = "forbidden"

    def get_free_tiles(self):
        positions_of_free_tiles = [k for k, v in self.board.items() if v == "free"]
        return positions_of_free_tiles


"""
b = Board()
b.put_queen(0, 0)
b.put_queen(1, 2)
b.set_forbidden_tiles()
# print(b.get_free_tiles()[0])
# print(len(b.get_free_tiles()))
print(b)
b.remove_queen(0, 0)
b.clear_forbidden_tiles()
b.set_forbidden_tiles()
print(b)
# print(b.get_free_tiles()[0])
# print(len(b.get_free_tiles()))
"""


def try_to_put_queen(trial_id, placed_queen):
    trial_id += 1
    while trial_id < 9:
        if len(b.get_free_tiles()) > 0:
            for x, y in b.get_free_tiles():
                b.put_queen(x, y)
                b.set_forbidden_tiles()
                placed_queen += 1
                if not try_to_put_queen(trial_id, placed_queen)[2]:
                    pass 
    return trial_id, placed_queen, len(b.get_free_tiles()) > 0

if __name__ == "__main__":
    b = Board()
    queen_no = 0

    if len(b.get_free_tiles()) > 0:



        queen_no += 1
        print(queen_no)


    print(b)





