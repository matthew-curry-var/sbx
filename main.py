from Chess import *
from unitTests import *

def main():

    chessGame = Chess()
    chessGame.move(0,1,0,2)
    chessGame.move(0,2,0,3)
    chessGame.move(1,1,1,2)
    chessGame.move(1,2,1,3)
    chessGame.move(2,1,2,2)
    chessGame.move(2,2,2,3)

    chessGame.move(0, 0, 0, 2)
    chessGame.printGameState()
    print(chessGame.getPieceLegalMoves(0, 0))
    print(chessGame.getPieceLegalMoves(0, 2))
    chessGame.move(0,2,6,2)
    chessGame.printGameState()
    print(chessGame.getPieceLegalMoves(6,2))
    chessGame.move(6,2,6,6)
    chessGame.printGameState()
    print(chessGame.getPieceLegalMoves(6,6))

    """

    print("moves for pawn @ (0, 1): ", chessGame.getPieceLegalMoves(0, 1))
    print("moves for pawn @ (4, 1): ", chessGame.getPieceLegalMoves(4, 1))
    print("moves for pawn @ (0, 6): ", chessGame.getPieceLegalMoves(0, 6))

    chessGame.move(0, 1, 0, 2)
    chessGame.move(0, 2, 0, 3)
    chessGame.move(0, 3, 0, 4)
    chessGame.move(4, 1, 4, 2)
    chessGame.move(0, 6, 0, 5)

    chessGame.printGameState()

    print("rook @ 0,0 poss moves: ", chessGame.getPieceLegalMoves(0, 0))

    """

    



main()