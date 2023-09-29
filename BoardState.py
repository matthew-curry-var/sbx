from pieces import bishop
from pieces import king
from pieces import knight
from pieces import pawn
from pieces import queen
from pieces import rook

""" Standard Chess Board Initialization Variables """
BOARD_LEN, BOARD_HGT = 8, 8

""" Mapping Of Board Integers To Respective Piece Type"""
BOARD_INT_MAP = dict({
    1 : pawn,
    2 : rook,
    3 : knight,
    4 : bishop,
    5 : queen,
    6 : king
})

""" Mapping Of Board Colors To Respective Piece Color"""
BOARD_COLOR_MAP = dict({
    0 : "White",
    1 : "Black"
})

""" Mapping Of Board Coordinates To Piece Type and Color (col, row) : (color, piece) """
BOARD_START_POS = dict({
    (0,0) : (0,2), (1,0) : (0,3), (2,0) : (0,4), (3,0) : (0,5), 
    (4,0) : (0,6), (5,0) : (0,4), (6,0) : (0,3), (7,0) : (0,2), 
    (0,1) : (0,1), (1,1) : (0,1), (2,1) : (0,1), (3,1) : (0,1),
    (4,1) : (0,1), (5,1) : (0,1), (6,1) : (0,1), (7,1) : (0,1),
    (0,7) : (1,2), (1,7) : (1,3), (2,7) : (1,4), (3,7) : (1,5), 
    (4,7) : (1,6), (5,7) : (1,4), (6,7) : (1,3), (7,7) : (1,2), 
    (0,6) : (1,1), (1,6) : (1,1), (2,6) : (1,1), (3,6) : (1,1),
    (4,6) : (1,1), (5,6) : (1,1), (6,6) : (1,1), (7,6) : (1,1)
})

class BoardState:

    def __init__(self):
        self.matrix = [[0 for _ in range(BOARD_HGT)] for _ in range(BOARD_LEN)]
        self.numPieces = 32
        init_pos = set(BOARD_START_POS.keys())

        for col in range(len(self.matrix)):
            for row in range(len(self.matrix[col])):
                if (col, row) in init_pos:
                    self.matrix[col][row] = BOARD_START_POS[(col, row)]
                else:
                    self.matrix[col][row] = 0
    
    def findPieces(color=None, type=None):
        pass

        