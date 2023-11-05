from BoardState import *
from util import *
from cursor import *

colorFuncMap = dict()

class Chess:

    def __init__(self):
        self.board = BoardState()
        self.whiteCheck = False
        self.blackCheck = False
        self.whiteCheckMate = False
        self.blackCheckMate = False
        self.currentColor = 1

    """move: take move piece input and implement iff. legal"""
    def move(self, xOrig : int, yOrig : int, xDest : int, yDest : int) -> None:
        if (not (xDest, yDest) in self.getPieceLegalMoves(xOrig, yOrig)):
            return
        else:
            self.board.movePiece(xOrig, yOrig, xDest, yDest)
            self.check(self.currentColor)
            self.nextTurn()

    """getPieceLegalMoves: return list of legal moves according to std chess rules"""
    def getPieceLegalMoves(self, pieceX : int, pieceY : int) -> list:
        piece = self.board.getPiece(pieceX, pieceY)
        if (not piece is None):
            color = piece % 2 #0/1
            if (piece == 0x01 or piece == 0x02): return self.pawnMove(pieceX, pieceY, color) #Pawn
            elif (piece == 0x03 or piece == 0x04): return self.rookMove(pieceX, pieceY, color) #Rook
            elif (piece == 0x05 or piece == 0x06): return self.knightMove(pieceX, pieceY, color) #Knight
            elif (piece == 0x07 or piece == 0x08): return self.bishopMove(pieceX, pieceY, color) #Bishop
            elif (piece == 0x09 or piece == 0x0A): return self.queenMove(pieceX, pieceY, color) #Queen
            elif(piece == 0x0B or piece == 0x0C): return self.kingMove(pieceX, pieceY, color) #King
        return list()

    """isEmpty :  helper function that identifies if a location (x, y) is empty"""
    def isEmpty(self, x, y) -> bool:
        if (self.board.getPiece(x,y) is None):
            return True
        return False
    
    """getBoardPiece : helper function to get the id hex code for a piece at (x, y), 0 otherwise"""
    def getBoardPiece(self, x, y) -> int:
        if (not self.isEmpty(x, y)):
            return self.board.getPiece(x, y)
        return 0
    
    """pieceMoveLogic: helper func to return list of legal moves acc. to location, color, and directional mapping"""
    def pieceMoveLogic(self, x, y, color, dirMap) -> list:
        moves = list()
        cursor = Cursor(x, y, None)
        for dir in set(dirMap.keys()):
            cursor.x, cursor.y = cursor.ox, cursor.oy
            cursor.modifyUpdateFunc(dir)
            for i in range(dirMap[dir]):
                cursor.update()
                if (self.isEmpty(cursor.x, cursor.y)): #if empty, add and move on
                    moves.append((cursor.x, cursor.y))
                else:
                    if (not self.board.sameColor(cursor.x, cursor.y, color)): #not-empty, add(?) then break
                        moves.append((cursor.x, cursor.y))
                    break
        return moves
    
    """pawnMove : game function to return the list of legal pawn moves"""
    def pawnMove(self, x, y, color) -> list:
        moves = list()
        
        if (color == 1):    #white pawn (need to add promotion ability)
            if (y < 7):
                if (self.isEmpty(x, y + 1)): moves.append((x, y + 1))
                if (x > 0):
                    if (not self.isEmpty(x - 1, y + 1) and self.board.isBlack(x - 1, y + 1)): moves.append((x - 1,y + 1))
                if (x < 7):
                    if (not self.isEmpty(x + 1, y + 1) and self.board.isBlack(x - 1, y + 1)): moves.append((x + 1, y + 1))
            if (y == 1):
                if (self.isEmpty(x, y + 1) and self.isEmpty(x, y + 2)): moves.append((x, y + 2))
        else:               #black pawn (need to add promotion ability)
            if (y > 0):
                if (self.isEmpty(x, y - 1)): moves.append((x, y - 1))
                if (x > 0):
                    if (not self.isEmpty(x - 1, y - 1) and self.board.isWhite(x - 1, y - 1)): moves.append((x - 1, y - 1))
                if (x < 7):
                    if (not self.isEmpty(x + 1, y - 1) and self.board.isWhite(x + 1, y - 1)): moves.append((x + 1, y - 1))
            if (y == 6):
                if (self.isEmpty(x, y - 1) and self.isEmpty(x, y - 2)): moves.append((x, y - 2))
        return moves

    """rookMove : game function to return list of legal rook moves"""
    def rookMove(self, x, y, color) -> list:
        directions = {right: 7 - x, left: x, up: 7 - y, down: y}
        return self.pieceMoveLogic(x, y, color, directions)
    
    """bishopMove : game function to return list of legal bishop moves"""
    def bishopMove(self, x, y, color) -> list:
        directions = {upRight : min((7 - x), (7 - y)), downRight: min((7 - x), y), upLeft: min(x, (7 - y)), downLeft: min(x, y)}
        return self.pieceMoveLogic(x, y, color, directions)
    
    """knightMove : game function to return list of legal knight moves"""
    def knightMove(self, x, y, color) -> list:
        directions = list((knightL1, knightL2, knightL3, knightL4, knightL5, knightL6, knightL7, knightL8))
        
        if (not (x >= 2 and x <= 5)):
            if (x == 0): dirX = directions[2:6]                     #knightL - 3, 4, 5, 6
            elif (x == 1): dirX = directions[-7::1]                 #knightL - 2, 3, 4, 5, 6, 7, 8
            elif (x == 6): dirX = directions[:3] + directions[5:]   #knightL - 1, 2, 3, 6, 7, 8
            elif (x == 7): dirX = directions[:2] + directions[6:]   #knightL - 1, 2, 7, 8      
        else: dirX = directions
    
        if (not (y >= 2 and y <= 5)):
            if (y == 0): dirY = directions[:4]                      #knightL - 1, 2, 3, 4
            elif (y == 1): dirY = directions[:5] + directions[-1:]  #knightL - 1, 2, 3, 4, 5, 8
            elif (y == 6): dirY = directions[0:1] + directions[3:]  #knightL - 1, 4, 5, 6, 7, 8
            elif (y == 7): dirY = directions[4:]                    #knightL - 5, 6, 7, 8
        else: dirY = directions

        directions = listToDict(list(set(dirX) & set(dirY)), defVal = 1)

        return self.pieceMoveLogic(x, y, color, directions)
    
    """queenMove : game function to return list of legal queen moves"""
    def queenMove(self, x, y, color) -> list:
        return self.bishopMove(x, y, color) + self.rookMove(x, y, color)
    
    """kingMove : game function to return list of legal king moves"""
    def kingMove(self, x, y, color) -> list:
        directions = list((upLeft, up, upRight, right, downRight, down, downLeft, left))

        if (x == 0): dirX = directions[1:6]
        elif (x == 7): dirX = directions[:2] + directions[6:]
        else: dirX = directions

        if (y == 0): dirY = directions[:4] + directions[7:]
        elif (y == 7): dirY = directions[3:]
        else: dirY = directions
        
        directions = listToDict(list(set(dirX) & set(dirY)), defVal=1)
        
        return self.pieceMoveLogic(x, y, color, directions)
    
    """pieceLocation : game function to find (x, y) list of respective piece type"""
    def pieceLocation(self, pieceType) -> list:
        allPieceLocs, locs = self.getAllRemainingPieces(), list()
        for pieceLoc in allPieceLocs:
            if (self.getBoardPiece(pieceLoc[0], pieceLoc[1]) == pieceType):
                locs.append(pieceLoc)
        return locs

    """getAllRemainingPieces: returns a list of pieces on board by coordinates"""
    def getAllRemainingPieces(self) -> list:
        pieces = list()
        for y in range(8):
            for x in range(8):
                if (not self.isEmpty(x, y)): pieces.append((x, y))
        return pieces

    """getAllLegalMoves: returns a list of all possible moves for all pieces on board"""
    def getAllLegalMoves(self) -> list:
        moves = list()
        for y in range(8):
            for x in range(8):
                pMoves = self.getPieceLegalMoves(x, y)
                if (len(pMoves) != 0): 
                    for m in pMoves: moves.append(m)
        return moves
    
    """getAllLegalMovesColor: returns a list of all possible moves for all pieces of color type"""
    def getAllLegalMovesColor(self, color) -> list:
        moves, colorPieces = list(), self.getColorPieces(color)
        for p in colorPieces:
            pMoves = self.getPieceLegalMoves(p[0], p[1])
            if (len(pMoves) != 0): 
                for m in pMoves: moves.append(m)
        return moves
    
    """getColorPieces: returns a list of all color pieces by (x, y) coordinates"""
    def getColorPieces(self, color) -> list:
        dPieces, pieces = list(), self.getAllRemainingPieces()
        for c in pieces:
            if (self.board.sameColor(c[0], c[1], color)): dPieces.append(c)
        return dPieces

    """nextTurn: updates necessary variables when we go to the next turn"""
    def nextTurn(self) -> None:
        self.currentColor = (self.currentColor + 1) % 2

    """check: modifies check member variable if check condition for color is met otherwise False"""
    def check(self, color) -> None:
        if (color == 1):                #check if black king in check
            if (self.pieceLocation(0xC)[0] in self.getAllLegalMovesColor(1)):
                self.blackCheck = True
                self.checkMate(0)       #call checkmate to see if black king in checkmate
            else: self.blackCheck = False
        else:                           #check if white king in check
            if (self.pieceLocation(0xB)[0] in self.getAllLegalMovesColor(0)): 
                self.whiteCheck = True
                self.checkMate(1)       #call checkmate to see if white king in checkmate
            else: self.whiteCheck = False

    """checkMate: modifies checkmate member variable if checkmate condition for color is met otherwise False"""
    def checkMate(self, color) -> None:
        pass

    def printGameState(self):
        self.board.print()

    