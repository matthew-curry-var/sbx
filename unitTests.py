from BoardState import *

""" Test BoardState.movePiece() """
def testOne():
    boardOne = BoardState()
    boardOne.movePiece(0,1,0,3) #white pawn a2->a4
    boardOne.movePiece(6,6,6,5) #black pawn g7->g6
    assert(boardOne.getPiece(0,1) == EMPTY_SQ)
    assert(boardOne.getPiece(6,6) == EMPTY_SQ)
    assert(boardOne.getPiece(0,3) == 0x1)
    assert(boardOne.getPiece(6,5) == 0x2)



    
    