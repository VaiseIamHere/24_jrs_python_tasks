import random

class Game_Board:
    def __init__(self,size=10,bombs=20):
        self.size = 10
        self.bombs = bombs
        self.board = self.make_board()
        self.dugged = []

    def make_board(self):
        board = []
        for i in range(self.size):
            score = []
            for j in range(self.size):
                score.append(None)
            board.append(score)

        return board
    
    def set_mines(self):
        first_row = -1
        first_column = -1
        while True:
            user_input = input("Where would you like to dig? Input as row,col: ")
            if len(user_input) != 3:
                print("Enter a valid expression !!")
                continue
            try:
                first_row = int(user_input[0])
                first_column = int(user_input[-1])
            except:
                print("Invalid Input, Enter in given format !!")
                continue
            if first_row < 0 or first_row >= self.size or first_column < 0 or first_column >= self.size:
                print("Invalid location. Try again.")
                continue
            self.dugged.append((first_row,first_column))
            break
        bombs_planted = 0
        while bombs_planted < self.bombs:
            r1 = random.randint(0, self.size - 1)
            r2 = random.randint(0, self.size - 1)
            if r1 == first_row and r2 == first_column:
                continue
            self.board[r1][r2] = '*'
            
            bombs_planted += 1
        self.assign_values_to_board()
        self.dig(first_row,first_column)

    def assign_values_to_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == '*':
                    continue
                self.board[i][j] = self.neighboring_bombs(i, j)

    def neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for i in range(max(0, row-1), min(self.size-1, row+1)+1):
            for j in range(max(0, col-1), min(self.size-1, col+1)+1):
                if i == row and j == col:
                    continue
                if self.board[i][j] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        self.dugged.append((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        else:
            for i in range(max(0, row-1), min(self.size-1, row+1)+1):
                for j in range(max(0, col-1), min(self.size-1, col+1)+1):
                    if (i, j) in self.dugged:
                        continue
                    self.dig(i, j)
            return True

    def print_board(self):
        visible_board = []
        for i in range(self.size):
            score = []
            for j in range(self.size):
                score.append(None)
            visible_board.append(score)

        for i in range(self.size):
            for j in range(self.size):
                if (i,j) in self.dugged:
                    visible_board[i][j] = str(self.board[i][j])
                else:
                    visible_board[i][j] = ' '

        final_string = ''
        first_line = "   0  1  2  3  4  5  6  7  8  9\n"
        seperator = "----------------------------------\n"
        
        for i in range(len(visible_board)):
            final_string += f'{i} |'
            cells = []
            for j in visible_board[i]:
                cells.append(str(j))
            final_string += ' |'.join(cells)
            final_string += ' |\n'

        str_len = int(len(final_string) / self.size)
        final_string = first_line + seperator + final_string + seperator

        return final_string

def play(size=10,bombs=20):
    board = Game_Board(size,bombs)
    value = size*size - bombs
    safe = True
    print(board.print_board())
    board.set_mines()
    while len(board.dugged) < value:
        print(board.print_board())
        user_input = input("Where would you like to dig? Input as row,col: ")
        try:
            row = int(user_input[0])
            col = int(user_input[-1])
        except:
            print("Invalid Input, Enter in given format !!")
        if row < 0 or row >= board.size or col < 0 or col >= board.size:
            print("Invalid location. Try again.")
            continue

        safe = board.dig(row, col)
        if not safe:
            break

    if safe:
        print("\n\n\nCONGRATULATIONS!!!! YOU ARE WON A LOTTERY!!!")
    else:
        print("\n\n\nSORRY GAME OVER :(")
        board.dugged = [(i,j) for i in range(board.size) for j in range(board.size)]
        for i in range(board.size):
            for j in range(board.size):
                board.dugged.append((i,j))
        print(board.print_board())


print("<-----Welcome to Mine Sweepers !!----->\n\n")
print("Choose Difficulty level:\n\t1.Easy (Upto 10 Mines) --> Enter 'E'\n\t2.Medium (Upto 20 Mines) --> Enter 'M'\n\t3.Hard (Upto 40 Mines) --> Enter 'H'\n")
bombs = 0
while True:
    d = input('Enter: ')
    d = d.replace(" ","").lower()
    if d == 'e':
        bombs = 10
        print("\n\nGameMode: Easy\n\n")
        break
    elif d == 'm':
        bombs = 20
        print("\n\nGameMode: Medium\n\n")
        break
    elif d == 'h':
        bombs = 40
        print("\n\nGameMode: Hard\n\n")
        break
    print("Don't want to play or what ??")

play(bombs=bombs)
