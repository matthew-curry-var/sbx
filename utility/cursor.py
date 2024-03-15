"""cursor : helper class that represents a current (x,y) state to be evaluated and a corresponding update function"""
class Cursor:

    def __init__(self, x, y, func):
        self.ox = x
        self.oy = y
        self.x = x
        self.y = y
        self.updateFunc = func

    def update(self) -> None:
        self.updateFunc(self)

    def modifyUpdateFunc(self, newFunc) -> None:
        self.updateFunc = newFunc