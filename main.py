from Chess import *
from unitTests import *

def main():

    chessGame = Chess()
    chessGame.printGameState()



    print("moves for pawn @ (0, 1): ", chessGame.getPieceLegalMoves(0, 1))
    print("moves for pawn @ (4, 1): ", chessGame.getPieceLegalMoves(4, 1))
    print("moves for pawn @ (0, 6): ", chessGame.getPieceLegalMoves(0, 6))

    print()
    print()

    chessGame.move(0, 1, 0, 2)
    chessGame.move(4, 1, 4, 2)
    chessGame.move(0, 6, 0, 5)

    chessGame.printGameState()

main()