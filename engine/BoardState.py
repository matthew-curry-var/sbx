import time
from utility.util import BOARD_START_POS, BOARD_LEN, EMPTY_SQ, CHESS_HEX_TO_ASCII, CHESS_NUM_ALPHA_COLS

class BoardState:

    def __init__(self):
        self.matrix = [[0 for _ in range(BOARD_LEN)] for _ in range(BOARD_LEN)]
        for row in range(BOARD_LEN):
            for col in range(BOARD_LEN):
                if (row, col) in BOARD_START_POS.keys():
                    self.matrix[row][col] = BOARD_START_POS[(row, col)]
                else:
                    self.matrix[row][col] = EMPTY_SQ

    """movePiece : move piece representation from (x0, y0) -> (x1, y1)"""
    def movePiece(self, x0 : int, y0 : int, x1 : int, y1 : int):
        self.matrix[x1][y1] = self.matrix[x0][y0]
        self.matrix[x0][y0] = EMPTY_SQ
    
    """getPiece : return piece representation from (x,y) if valid piece"""
    def getPiece(self, x : int, y : int):
        return self.matrix[x][y]
    
    """place: place piece onto board"""
    def place(self, x : int, y : int, p : int):
        self.matrix[x][y] = p
    
    """print : fancy print function for terminal printing"""
    def print(self):
        print(end="\n")
        print("Board State @ ", time.time())
        
        #Print board rows
        for y in reversed(range(len(self.matrix))):
            print(" "*3 + str(y) + " ", end="")
            print(" |", end="")
            for x in range(len(self.matrix)):
                print(f'{str(CHESS_HEX_TO_ASCII[self.matrix[x][y]]):3}', end="")
            print("|", end="\n")

        #Print board alpha columns
        print(" "*7, end="")
        for y in range(len(self.matrix)):
            print(f'{str(y):3}', end="")
        print(end="\n")