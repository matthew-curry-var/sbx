from cursor import *

chessHexToAscii = {
    0x0 : "0",
    0x1 : "\u265F", #white pawn
    0x2: "\u2659", #black pawn
    0x3: "\u265C", #white rook
    0x4: "\u2656", #black rook
    0x5: "\u265E", #white knight
    0x6: "\u2658", #black knight
    0x7: "\u265D", #white bishop
    0x8: "\u2657", #black bishop
    0x9: "\u265B", #white queen
    0xA: "\u2655", #black queen
    0xB: "\u265A", #white king
    0xC: "\u2654" #black king
}

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