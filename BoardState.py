import time
from util import BOARD_START_POS, BOARD_LEN, EMPTY_SQ, CHESS_HEX_TO_ASCII

class BoardState:

    def __init__(self):
        self.matrix = [[0 for _ in range(BOARD_LEN)] for _ in range(BOARD_LEN)]
        self.numPieces = 32
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
        if (self.matrix[x][y] != 0x0):
            return self.matrix[x][y]
        return None
    
    """isWhite : return True if given piece is white, False otherwise"""
    def isBlack(self, x : int, y : int) -> bool:
        if (self.matrix[x][y] % 2 == 0):
            return True
        return False

    """isBlack : return True if given piece is black, False otherwise"""
    def isWhite(self, x : int, y : int) -> bool:
        if (self.matrix[x][y] % 2 == 1):
            return True
        return False
    
    """sameColor : return True if given piece is same color as color input"""
    def sameColor(self, x : int, y : int, color : int) -> bool:
        if (self.matrix[x][y] % 2 != color):
            return False
        return True
    
    """place: place piece onto board"""
    def place(self, x : int, y : int, p : int):
        self.matrix[x][y] = p
    
    """print : fancy print function for terminal printing"""
    def print(self):
        print("Board State @ ", time.time())
        for y in reversed(range(len(self.matrix))):
            print("|", end="")
            for x in range(len(self.matrix)):
                print(f'{str(CHESS_HEX_TO_ASCII[self.matrix[x][y]]):3}', end="")
            print("|", end="\n")