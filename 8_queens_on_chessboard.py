'''
 ,---.                                                    
|  o  |  ,---.  ,--.,--.  ,---.   ,---.  ,--,--,   ,---.  
.'   '. | .-. | |  ||  | | .-. : | .-. : |      \ (  .-'  
|  o  | ' '-' | '  ''  ' \   --. \   --. |  ||  | .-'  `) 
 `---'   `-|  |  `----'   `----'  `----' `--''--' `----'  
           `--'                                           
'''

from os import system, name
import time



def clear_screen() -> None:
    '''
    clears terminal screen in all OS
    '''
    # for windows
    if name == 'nt':
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Board(object):
    def __init__(self, rows:int, cols:int):
        self.row = rows
        self.column = cols
        self.board = {}
        for row in range(self.row):
            for column in range(self.column):
                self.board[row, column] = "free"

    def __str__(self) -> str:
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

    def get_cols(self) -> int:
        return self.column

    def put_queen(self, row:int, column:int) -> None:
        if self.board[row, column] == "free":
            self.board[row, column] = "queen"

    def set_forbidden(self, row:int, column:int) -> None:
        for c in range(column+1):
            self.board[row, c] = "forbidden"

    def remove_queen(self, row:int, column:int) -> None:
        if self.board[row, column] == "queen":
            self.board[row, column] = "free"

    def clear_forbidden_tiles(self) -> None:
        rows = self.row
        cols =self.column
        for r in range(rows):
            for c in range(cols):
                if self.board[r, c] == "forbidden":
                    self.board[r, c] = "free"
    
    
    def validate_rows(self) -> bool:
        rows = self.row
        cols = self.column
        for r in range(rows):
            forbiddens = 0
            for c in range(cols):
                if self.board[r, c] == "forbidden":
                    forbiddens += 1
            if forbiddens == cols:
                return False
        return True

    def set_forbidden_tiles(self) -> None:
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

    def get_free_tiles(self) -> list:
        positions_of_free_tiles = [k for k, v in self.board.items() if v == 'free']
        return positions_of_free_tiles

    def get_queens(self) -> list:
        positions_of_queens = [k for k, v in self.board.items() if v == 'queen']
        return positions_of_queens


BOARD_SIZE = 8
TIMEOUT_SECONDS = 600
DELAY = .00
all_solutions = 0

b = Board(BOARD_SIZE, BOARD_SIZE)
clear_screen()
print(b)
start_time = time.time()
b.put_queen(0,0)
b.set_forbidden_tiles()

while time.time() - start_time < TIMEOUT_SECONDS:
    clear_screen()
    print(b)
    free_tiles = b.get_free_tiles()
    time.sleep(DELAY)

    if len (b.get_queens()) == b.get_cols():
        all_solutions += 1
        print(f'Solution #{all_solutions}')
        time.sleep(1.0)

    if len(free_tiles) and b.validate_rows():
        x, y = free_tiles[0]
        b.put_queen(x,y)
        b.clear_forbidden_tiles()
        b.set_forbidden_tiles()

    else:
        if b.get_queens():
            x, y = b.get_queens()[-1:][0]
            b.remove_queen(x, y)
            b.clear_forbidden_tiles()
            b.set_forbidden_tiles()
            b.set_forbidden(x, y)
        else:
            clear_screen()
            print(f"{BOARD_SIZE}-queen problem has {all_solutions} solutions.")
            break