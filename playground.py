from cursor import Cursor
from util import *

c = Cursor(2, 2, upLeft)

print(c.x)
print(c.y)

c.update()

print(c.x)
print(c.y)