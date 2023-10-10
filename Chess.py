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

    """getPieceLegalMoves: return list of legal moves according to std chess rules"""
    def getPieceLegalMoves(self, pieceX : int, pieceY : int) -> list:
        piece, moves = self.board.getPiece(pieceX, pieceY), list()
        if (piece is None):
            return moves
        else:
            if (piece % 2 != 0): #White piece
                if (piece == 0x01): #White pawn
                    pass
                elif (piece == 0x03): #White rook
                    pass
                elif (piece == 0x05): #White knight
                    pass
                elif (piece == 0x07): #White bishop
                    pass
                elif (piece == 0x09): #White queen
                    pass
                else: #White king (== 0x0B)
                    pass

            else: #Black piece
                if (piece == 0x02): #Black pawn
                    pass
                elif (piece == 0x04): #Black rook
                    pass
                elif (piece == 0x06): #Black knight
                    pass
                elif (piece == 0x08): #Black bishop
                    pass
                elif (piece == 0x0A): #Black queen
                    pass
                else: #Black king (== 0x0C)
                    pass

    def isEmpty(self, x, y) -> bool:
        if (self.board.getPiece(x,y) is None):
            return True
        return False

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

    