from cursor import *

def left(c : Cursor) -> None:
    c.x -= 1

def right(c : Cursor) -> None:
    c.x += 1

def up(c : Cursor) -> None:
    c.y += 1

def down(c : Cursor) -> None:
    c.y -= 1

def upRight(c : Cursor) -> None:
    c.x += 1
    c.y += 1

def upLeft(c : Cursor) -> None:
    c.x -= 1
    c.y += 1

def downRight(c : Cursor) -> None:
    c.x += 1
    c.y -= 1

def downLeft(c : Cursor) -> None:
    c.x -= 1
    c.y -= 1