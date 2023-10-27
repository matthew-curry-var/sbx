import Cursor

def upRight(c : Cursor) -> None:
    c.x += 1
    c.y += 1

def upLeft(c : Cursor) -> None:
    c.x -+ 1
    c.y += 1

def downRight(c : Cursor) -> None:
    c.x += 1
    c.y -= 1

def downLeft(c : Cursor) -> None:
    c.x -= 1
    c.y -= 1