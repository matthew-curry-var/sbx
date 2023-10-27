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
        piece = self.board.getPiece(pieceX, pieceY)
        if (not piece is None):
            color = piece % 2 #0/1

            if (piece == 0x01 or piece == 0x02): #Pawn
                return self.pawnMove(pieceX, pieceY, color)

            elif (piece == 0x03 or piece == 0x04): #Rook
                return self.rookMove(pieceX, pieceY, color)
            
            elif (piece == 0x05 or piece == 0x06): #Knight
                return self.knightMove(pieceX, pieceY, color)

            elif (piece == 0x07 or piece == 0x08): #Bishop
                return self.bishopMove(pieceX, pieceY, color)

            elif (piece == 0x09 or piece == 0x0A): #Queen
                return self.queenMove(pieceX, pieceY, color)

            elif(piece == 0x0B or piece == 0x0C): #King
                return self.kingMove(pieceX, pieceY, color)
        else:
            print("Error - could not identify piece although not None: ", piece)
            return list()

    """isEmpty :  helper function that identifies if a location (x, y) is empty"""
    def isEmpty(self, x, y) -> bool:
        if (self.board.getPiece(x,y) is None):
            return True
        return False
    
    """pawnMove : game function to return the list of legal pawn moves"""
    def pawnMove(self, x, y, color) -> list:
        
        #if color == white, look in: 
        # 1. [x][y+1] -> check empty, 
        # 2. [x-1][y+1] -> check black piece, 
        # 3. [x+1][y+1] -> check black piece

        #if color == black, look in:
        # 1. [x][y-1] -> check empty
        # 2. [x-1][y-1] -> check white piece,
        # 3. [x+1][y-1] -> check white piece

        moves = list()

        if (color == 1):    #white pawn
            if (y < 7):

                if (self.isEmpty(x, y + 1)):
                    moves.append((x, y + 1))

                if (x > 0):
                    leftDiag = self.board.getPiece(x - 1, y + 1)
                    if (leftDiag != None and self.board.isBlack(leftDiag)):
                        moves.append((x - 1,y + 1))

                if (x < 7):
                    rightDiag = self.board.getPiece(x + 1, y + 1)
                    if (rightDiag != None and self.board.isBlack(rightDiag)):
                        moves.append((x + 1, y + 1))

        else:               #black pawn
            if (y > 0):

                if (self.isEmpty(x, y - 1)):
                    moves.append((x, y - 1))

                if (x > 0):
                    leftDiag = self.board.getPiece(x - 1, y - 1)
                    if (leftDiag != None and self.board.isWhite(leftDiag)):
                        moves.append((x - 1, y - 1))

                if (x < 7):
                    rightDiag = self.board.getPiece(x + 1, y - 1)
                    if (rightDiag != None and self.board.isWhite(rightDiag)):
                        moves.append((x + 1, y - 1))

        return moves
    
    """rookMove : game function to return list of legal rook moves"""
    def rookMove(self, x, y, color) -> list:

        #need to make this more efficient with the cursor class....
        #so far the logic works below, but this implementation will be slow when we do RL

        moves = list()

        cursor = (x, y)
        for i in range(7 - y): #upward: 7 - y
            cursor = (cursor[0], cursor[1] + 1)
            if (not self.isEmpty(cursor[0], cursor[1])):
                if (self.board.sameColor(cursor[0], cursor[1], color)):
                    break
                else:
                    moves.append(cursor)
                    break
            else:
                moves.append(cursor)

        cursor = (x, y)
        for i in range(x): #left: x
            cursor = (cursor[0] - 1, cursor[1])
            if (not self.isEmpty(cursor[0], cursor[1])):
                if (self.board.sameColor(cursor[0], cursor[1], color)):
                    break
                else:
                    moves.append(cursor)
                    break
            else:
                moves.append(cursor)

        cursor = (x, y)
        for i in range(y): #downward : y
            cursor = (cursor[0], cursor[1] - 1)
            if (not self.isEmpty(cursor[0], cursor[1])):
                if (self.board.sameColor(cursor[0], cursor[1], color)):
                    break
                else:
                    moves.append(cursor)
                    break
            else:
                moves.append(cursor)

        cursor = (x, y)
        for i in range(7 - x): #right: 7 - x
            cursor = (cursor[0] + 1, cursor[1])
            if (not self.isEmpty(cursor[0], cursor[1])):
                if (self.board.sameColor(cursor[0], cursor[1], color)):
                    break
                else:
                    moves.append(cursor)
                    break
            else:
                moves.append(cursor)


        return moves
    

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

    