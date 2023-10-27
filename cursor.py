class Cursor:

    def __init__(self, x, y, func):
        self.x = x
        self.y = y
        self.updateFunc = func

    def update(self) -> None:
        self.updateFunc(self)