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


    def movePiece(self, xOrig : int, yOrig : int, xDest : int, yDest : int):
        self.matrix[xDest][yDest] = self.matrix[xOrig][yOrig]
        self.matrix[xOrig][yOrig] = EMPTY_SQ
    
    def getPiece(self, col : int, row : int):
        return self.matrix[col][row]
    
    def print(self):
        print("Board State @ ", time.time())
        for y in reversed(range(len(self.matrix))):
            print("|", end="")
            for x in range(len(self.matrix)):
                print(f'{str(self.matrix[x][y]):3}', end="")
            print("|", end="\n")