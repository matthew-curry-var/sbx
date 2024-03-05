from BoardState import *
from util import *
from cursor import *

class Chess:

    def __init__(self):
        self.board = BoardState()
        self.moves = {0: None, 1: None}
        self.kingLocs = {0: (4, 7), 1: (4, 0)}
        self.checkMate = {0: False, 1: False}
        self.currentColor = 1
        self.findLegalMoves(0)
        self.findLegalMoves(1)

    """applyMove: take move input as tuple and send to move function"""
    def applyMove(self, move : tuple) -> None:
        self.move(int(move[0]), int(move[1]), int(move[2]), int(move[3]))

    """move: take move piece input and implement iff. legal according to piece move and check rules"""
    def move(self, xOrig : int, yOrig : int, xDest : int, yDest : int) -> None:
        if (not self.checkMate[self.currentColor]):
            if ((xOrig, yOrig, xDest, yDest) in self.moves[self.currentColor]):
                self.board.movePiece(xOrig, yOrig, xDest, yDest)                    #Apply move
                piece = self.getBoardPiece(xDest, yDest)
                if (piece == 0xB):                                                  #If piece moved is white king
                    self.kingLocs[1] = (xDest, yDest)
                elif(piece == 0xC):                                                 #If piece moved is black king
                    self.kingLocs[0] = (xDest, yDest)
                self.currentColor = (self.currentColor + 1) % 2                     #Next turn
                self.findLegalMoves(0)
                self.findLegalMoves(1)

    """fingLegalMoves: find legal moves for color (includes check filtereing)"""
    def findLegalMoves(self, color : int) -> None:
        moves = self.allPiecewiseMoves(color)                                       #Get all legal piecewise moves for color
        moves = self.checkMoves(moves, color)                                       #Check filter
        if (not len(moves)): self.checkMate[color] = True                           #Checkmate flag
        self.moves[color] = moves                                                   #Add moves to object member

    """returnLegalMoves: helper function to return legal moves outside of the class"""
    def returnLegalMoves(self, color : int) -> list:
        moves = self.allPiecewiseMoves(color)
        moves = self.checkMoves(moves, color)
        return moves

    """legalPiecewiseMoves: returns flattened list of all moves for a given color by piece rules (no check filtering)"""
    def allPiecewiseMoves(self, color) -> list:
        legalMoves = list()
        for coord in self.getColorCoords(color):
            moves = self.getPieceLegalMoves(coord[0], coord[1])
            if (moves):
                for m in moves:
                    legalMoves.append(m)
        return legalMoves

    "checkCondition: return True iff currColor's king is in enemy move list"
    def checkCondition(self, currColor) -> bool:
        oppColor = (currColor + 1) % 2 
        oppMoves = self.allPiecewiseMoves(oppColor)
        for oppMove in oppMoves:
            if (self.kingLocs[currColor] == (oppMove[2], oppMove[3])):
                return True
        return False
    
    """checkMoves: filters out moves that impose check condition on current color"""
    def checkMoves(self, moveList, currColor) -> list:
        legalMoves, oppColor = list(), (currColor + 1) % 2
        for move in moveList:

            #Apply move temporarily
            king = self.isKing(move[0], move[1])                            #Determine if moving piece is king
            temp = self.getBoardPiece(move[2], move[3])                     #Get board piece at destination
            self.board.movePiece(move[0], move[1], move[2], move[3])        #Apply move from theoretical moveList
            if (king): self.kingLocs[king % 2] = (move[2], move[3])         #If king, update kingLoc

            #Determine if temporary move results in check condition
            legal = True
            for oppMove in self.allPiecewiseMoves(oppColor):                #Iterate through opponent piece-legal moves
                if (self.kingLocs[currColor] == (oppMove[2], oppMove[3])):  #Break if king's location is in opponents path
                    legal = False
                    break
            if (legal):
                legalMoves.append(move)

            #Restore board
            self.board.movePiece(move[2], move[3], move[0], move[1])        #Return theoretical piece
            if (king): self.kingLocs[king % 2] = (move[0], move[1])         #Re-update kingLoc if necessary
            self.board.place(move[2], move[3], temp)                        #Return board piece from destination

        return legalMoves
    
    """isKing: returns value of king (if king), 0 otherwise"""
    def isKing(self, x, y) -> int:
        p = self.getBoardPiece(x, y)
        if (p == 0xB or p == 0xC):
            return p
        return 0

    """getColorCoords: return list of (x,y) coordinates where each piece is of a given input color"""
    def getColorCoords(self, color) -> list:
        coords = list()
        for x in range(BOARD_LEN):
            for y in range(BOARD_LEN):
                piece = self.getBoardPiece(x, y)
                if (piece and (piece % 2) == color):
                    coords.append((x, y))
        return coords

    """getPieceLegalMoves: return list of legal moves according to std chess rules"""
    def getPieceLegalMoves(self, pieceX : int, pieceY : int) -> list:
        piece = self.getBoardPiece(pieceX, pieceY)
        if (piece):
            color = piece % 2   #0/1
            if (piece == 0x01 or piece == 0x02):
                moveDests = self.pawnMove(pieceX, pieceY, color)     #Pawn
            elif (piece == 0x03 or piece == 0x04):  
                moveDests = self.rookMove(pieceX, pieceY, color)     #Rook
            elif (piece == 0x05 or piece == 0x06):  
                moveDests = self.knightMove(pieceX, pieceY, color)   #Knight
            elif (piece == 0x07 or piece == 0x08):  
                moveDests = self.bishopMove(pieceX, pieceY, color)   #Bishop
            elif (piece == 0x09 or piece == 0x0A):  
                moveDests = self.queenMove(pieceX, pieceY, color)    #Queen
            elif (piece == 0x0B or piece == 0x0C):  
                moveDests = self.kingMove(pieceX, pieceY, color)     #King
        return self.prependLoc(pieceX, pieceY, moveDests)
    
    """prependLoc: prepend origin coordinate to each tuple in destination locations list"""
    def prependLoc(self, x0 : int, y0 : int, destLocs : list) -> list:
        moves = list()
        for dest in destLocs:
            moves.append((x0, y0, dest[0], dest[1]))
        return moves

    """getBoardPiece: helper function to get the id hex code for a piece at (x, y), 0 otherwise"""
    def getBoardPiece(self, x, y) -> int:
        return self.board.getPiece(x, y)
    
    """pieceMoveLogic: helper func to return list of legal moves acc. to location, color, and directional mapping"""
    def pieceMoveLogic(self, x, y, color, dirMap) -> list:
        moves = list()
        cursor = Cursor(x, y, None)
        for dir in set(dirMap.keys()):
            cursor.x, cursor.y = cursor.ox, cursor.oy
            cursor.modifyUpdateFunc(dir)
            for i in range(dirMap[dir]):
                cursor.update()
                if (not self.getBoardPiece(cursor.x, cursor.y)): #if empty, add and move on
                    moves.append((cursor.x, cursor.y))
                else:
                    if (self.getBoardPiece(cursor.x, cursor.y) % 2 != color % 2): #nonempty and different color
                        moves.append((cursor.x, cursor.y))
                    break
        return moves
    
    """pawnMove: game function to return the list of legal pawn moves"""
    def pawnMove(self, x, y, color) -> list:
        moves = list()
        if (color == 1):    #white pawn (need to add promotion ability)
            if (y == 1):
                if (not self.getBoardPiece(x, y + 1)):
                    moves.append((x, y + 1))
                    if (not self.getBoardPiece(x, y + 2)):
                        moves.append((x, y + 2))    
            elif (y < 7):
                if (not self.getBoardPiece(x, y + 1)): 
                    moves.append((x, y + 1))

            if (x > 0):
                topLeft = self.getBoardPiece(x - 1, y + 1)
                if (topLeft and (topLeft % 2 == 0)): 
                    moves.append((x - 1,y + 1))
            if (x < 7):
                topRight = self.getBoardPiece(x + 1, y + 1)
                if (topRight and (topRight % 2 == 0)): 
                    moves.append((x + 1, y + 1))

        else:               #black pawn (need to add promotion ability)
            if (y == 6):
                if (not self.getBoardPiece(x, y - 1)):
                    moves.append((x, y - 1))
                    if (not self.getBoardPiece(x, y - 2)):
                        moves.append((x, y - 2))
            elif (y > 0):
                if (not self.getBoardPiece(x, y - 1)): 
                    moves.append((x, y - 1))

            if (x > 0):
                botLeft = self.getBoardPiece(x - 1, y - 1)
                if (botLeft and (botLeft % 2 == 1)): 
                    moves.append((x - 1, y - 1))
            if (x < 7):
                botRight = self.getBoardPiece(x + 1, y - 1)
                if (botRight and (botRight % 2 == 1)): 
                    moves.append((x + 1, y - 1))
   
        return moves

    """rookMove: game function to return list of legal rook moves"""
    def rookMove(self, x, y, color) -> list:
        directions = {right: 7 - x, left: x, up: 7 - y, down: y}
        return self.pieceMoveLogic(x, y, color, directions)
    
    """bishopMove: game function to return list of legal bishop moves"""
    def bishopMove(self, x, y, color) -> list:
        directions = {upRight : min((7 - x), (7 - y)), downRight: min((7 - x), y), upLeft: min(x, (7 - y)), downLeft: min(x, y)}
        return self.pieceMoveLogic(x, y, color, directions)
    
    """knightMove: game function to return list of legal knight moves"""
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
    
    """queenMove: game function to return list of legal queen moves"""
    def queenMove(self, x, y, color) -> list:
        return self.bishopMove(x, y, color) + self.rookMove(x, y, color)
    
    """kingMove: game function to return list of legal king moves"""
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

    """printGameState: call board print function"""
    def printGameState(self):
        self.board.print()
