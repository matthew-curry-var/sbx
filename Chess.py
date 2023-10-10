from BoardState import *

class Chess:

    def __init__(self):
        self.board = BoardState()
        self.score = 0

    """move: take move piece input and implement iff. legal"""
    def move(self, xOrig : int, yOrig : int, xDest : int, yDest : int) -> None:
        if (not (xDest, yDest) in self.getPieceLegalMoves(xOrig, yOrig)):
            return
        else:
            self.board.movePiece(xOrig, yOrig, xDest, yDest)

    def getPieceLegalMoves(self, pieceX : int, pieceY : int) -> list:
        if (self.board.getPiece(pieceX, pieceY) is None):
            return []
        else:
            #need to identify piece abilities quickly
            #return list of legal moves
            #what is a legal move?
            #piece have certain moving capabilities
            #piece cannot capture peces of same color
            #piece cannot move off the grid

            pass

    
    def getAllRemainingPieces(self) -> list:
        pass

    def getAllLegalMoves(self) -> list:
        pass

    def check(self) -> bool:
        pass

    def checkMate(self) -> bool:
        pass

    def evaluate(self): #evaluation function (will implement standard score first)
        pass

    def printGameState(self):
        self.board.print()

    