import BoardState

class Chess:

    def __init__(self):
        self.board = BoardState()

    #implement logic

    def getPieceLegalMoves(self, pieceX : int, pieceY : int) -> list:
        pass

    def getAllLegalMoves(self) -> list:
        pass

    def check(self) -> bool:
        pass

    def checkMate(self) -> bool:
        pass

    def evaluate(self): #evaluation function (will implement standard score first)
        pass

    