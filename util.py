from cursor import *

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

""" Mapping Of Board Pieces to ASCII Code """
CHESS_HEX_TO_ASCII = {
    0x0 : "-",
    0x2 : "\u265F", #white pawn
    0x1: "\u2659", #black pawn
    0x4: "\u265C", #white rook
    0x3: "\u2656", #black rook
    0x6: "\u265E", #white knight
    0x5: "\u2658", #black knight
    0x8: "\u265D", #white bishop
    0x7: "\u2657", #black bishop
    0xA: "\u265B", #white queen
    0x9: "\u2655", #black queen
    0xC: "\u265A", #white king
    0xB: "\u2654" #black king
}

CHESS_PIECE_SCORE = {
    0x1: 1, #white pawn
    0x2: 1, #black pawn
    0x3: 5, #white rook
    0x4: 5, #black rook
    0x5: 3, #white knight
    0x6: 3, #black knight
    0x7: 3, #white bishop
    0x8: 3, #black bishop
    0x9: 9, #white queen
    0xA: 9, #black queen
    0xB: 200, #white king
    0xC: 200, #black king
}

KINGS = {
    0 : 0xC, #black king
    1 : 0xB  #white king
}

COLOR_STR = {
    0 : "Black", #black
    1 : "White"  #white
}

CHESS_NUM_ALPHA_COLS = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}

CHESS_ALPHA_NUM_COLS = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5, 
    "g": 6,
    "h": 7
}

"""LIFO (Last In First Out) Stack Class"""
class Stack:

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

"""left: increment cursor left"""
def left(c : Cursor) -> None:
    c.x -= 1

"""right: increment cursor right"""
def right(c : Cursor) -> None:
    c.x += 1

"""up: increment cursor up"""
def up(c : Cursor) -> None:
    c.y += 1

"""down: increment cursor down"""
def down(c : Cursor) -> None:
    c.y -= 1

"""upRight: increment cursor up right"""
def upRight(c : Cursor) -> None:
    c.x += 1
    c.y += 1

"""upLeft: increment cursor up left"""
def upLeft(c : Cursor) -> None:
    c.x -= 1
    c.y += 1

"""downRight: increment cursor down right"""
def downRight(c : Cursor) -> None:
    c.x += 1
    c.y -= 1

"""downLeft: increment cursor down left"""
def downLeft(c : Cursor) -> None:
    c.x -= 1
    c.y -= 1

"""knightL1: move cursor to knight L1"""
def knightL1(c : Cursor) -> None:
    c.x -= 2
    c.y += 1

"""knightL2: move cursor to knight L2"""
def knightL2(c : Cursor) -> None:
    c.x -= 1
    c.y += 2

"""knightL3: move cursor to knight L3"""
def knightL3(c : Cursor) -> None:
    c.x += 1
    c.y += 2

"""knightL4: move cursor to knight L4"""
def knightL4(c : Cursor) -> None:
    c.x += 2
    c.y += 1

"""knightL5: move cursor to knight L5"""
def knightL5(c : Cursor) -> None:
    c.x += 2
    c.y -= 1

"""knightL6: move cursor to knight L6"""
def knightL6(c : Cursor) -> None:
    c.x += 1
    c.y -= 2

"""knightL7: move cursor to knight L7"""
def knightL7(c : Cursor) -> None:
    c.x -= 1
    c.y -= 2

"""knightL8: move cursor to knight L8"""
def knightL8(c : Cursor) -> None:
    c.x -= 2
    c.y -= 1

"""listToDict: convert list to dictionary where list elements are keys w default val"""
def listToDict(listVar : list, defVal : int) -> dict:
    return {listVar[i]: defVal for i in range(0, len(listVar))}

"""str_to_int: convert a string into list of strings"""
def str_to_lst(strVar : list) -> list:
    return [strVar[i] for i in range(len(strVar))]