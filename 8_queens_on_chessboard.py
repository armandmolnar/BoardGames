from os import system, name
import time


def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Board:
    def __init__(self, rows, cols):
        self.row = rows
        self.column = cols
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

    def set_forbidden(self, row, column):
        self.board[row, column] = "forbidden"

    def remove_queen(self, row, column):
        if self.board[row, column] == "queen":
            self.board[row, column] = "free"

    def clear_forbidden_tiles(self):
        rows = self.row
        cols =self.column
        for r in range(rows):
            for c in range(cols):
                if self.board[r, c] == "forbidden":
                    self.board[r, c] = "free"

    def set_forbidden_tiles(self):
        positions_of_queens = [k for k, v in self.board.items() if v == 'queen']
        rows = self.row
        cols = self.column
        for x, y in positions_of_queens:
            for n in range(max(rows, cols)):
                # rows of the queens: free->forbidden
                if (n < cols) and self.board[x, n] == "free":
                    self.board[x, n] = "forbidden"
                # columns of the queens: free->forbidden
                if (n < rows) and self.board[n, y] == "free":
                    self.board[n, y] = "forbidden"
                # left_and_up axes of the queens: free->forbidden
                if (x - n) >= 0 and (y - n) >= 0 and self.board[x - n, y - n] == "free":
                    self.board[x - n, y - n] = "forbidden"
                # left_and_down axes of the queens: free->forbidden
                if (x + n) < rows and (y - n) >= 0 and self.board[x + n, y - n] == "free":
                    self.board[x + n, y - n] = "forbidden"
                # right_and_up axes of the queens: free->forbidden
                if (x - n) >= 0 and (y + n) < cols and self.board[x - n, y + n] == "free":
                    self.board[x - n, y + n] = "forbidden"
                # right_and_down axes of the queens: free->forbidden
                if (x + n) < rows and (y + n) < cols and self.board[x + n, y + n] == "free":
                    self.board[x + n, y + n] = "forbidden"

    def get_free_tiles(self):
        positions_of_free_tiles = [k for k, v in self.board.items() if v == 'free']
        return positions_of_free_tiles

    def get_queens(self):
        positions_of_queens = [k for k, v in self.board.items() if v == 'queen']
        return positions_of_queens


b = Board(8, 8)
clear_screen()
print(b)
start_time = time.time()
seconds = 5
b.put_queen(0,0)
b.set_forbidden_tiles()

while time.time() - start_time < seconds:
    clear_screen()
    print(b)
    time.sleep(.5)
    free_tiles = b.get_free_tiles()
    print (free_tiles)
    
    if len(free_tiles):
        x, y = free_tiles[0]
        b.put_queen(x,y)
        b.clear_forbidden_tiles()
        b.set_forbidden_tiles()

    else:
        b.remove_queen(x, y)
        b.clear_forbidden_tiles()
        b.set_forbidden_tiles()
        b.set_forbidden(x, y)
        
        '''b.clear_forbidden_tiles()
        b.set_forbidden_tiles()
        clear_screen()
        print(b)
        time.sleep(.5)
        x, y = b.get_queens()[-1:]
        b.remove_queen(x, y)
        b.clear_forbidden_tiles()'''














"""
b.put_queen(7, 7)
b.put_queen(1, 2)
b.set_forbidden_tiles()
print(b.get_free_tiles()[0])
print(len(b.get_free_tiles()))
print(b)
b.remove_queen(7, 7)
b.clear_forbidden_tiles()
b.set_forbidden_tiles()
print(b)
print(b.get_free_tiles()[0])
print(len(b.get_free_tiles()))



if __name__ == "main":
    b = Board()
    for queen_no in range(1, 8):
        if len(b.get_free_tiles()) > 0:
            for free_tile in b.get_free_tiles():
                b.put_queen(free_tile)
                b.set_forbidden_tiles()



"""
