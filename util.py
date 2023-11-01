from cursor import *

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