import time

""" Useful Constants """
BOARD_LEN, EMPTY_SQ = 8, 0x0

""" Mapping Of Board Coordinates To Piece Type and Color """
BOARD_START_POS = dict({
    (0,0) : 0x3, #white rook
    (1,0) : 0x5, #white knight
    (2,0) : 0x7, #white bishop
    (3,0) : 0x9, #white queen
    (4,0) : 0xB, #white king
    (5,0) : 0x7, #white bishop
    (6,0) : 0x5, #white knight
    (7,0) : 0x3, #white rook
    (0,1) : 0x1, #white pawn
    (1,1) : 0x1, #white pawn
    (2,1) : 0x1, #white pawn
    (3,1) : 0x1, #white pawn
    (4,1) : 0x1, #white pawn
    (5,1) : 0x1, #white pawn
    (6,1) : 0x1, #white pawn
    (7,1) : 0x1, #white pawn
    (0,6) : 0x2, #black pawn
    (1,6) : 0x2, #black pawn
    (2,6) : 0x2, #black pawn
    (3,6) : 0x2, #black pawn
    (4,6) : 0x2, #black pawn
    (5,6) : 0x2, #black pawn
    (6,6) : 0x2, #black pawn
    (7,6) : 0x2, #black pawn
    (0,7) : 0x4, #black rook
    (1,7) : 0x6, #black knight
    (2,7) : 0x8, #black bishop
    (3,7) : 0xA, #black queen
    (4,7) : 0xC, #black king
    (5,7) : 0x8, #black bishop
    (6,7) : 0x6, #black knight
    (7,7) : 0x4 #black bishop
})

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
    
    """print : fancy print function for terminal printing"""
    def print(self):
        print("Board State @ ", time.time())
        for y in reversed(range(len(self.matrix))):
            print("|", end="")
            for x in range(len(self.matrix)):
                print(f'{str(self.matrix[x][y]):3}', end="")
            print("|", end="\n")