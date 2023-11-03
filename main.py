from Chess import *
from unitTests import *
import re


def main():

    chessGame = Chess()
    colorMap = dict({0: "Black", 1: "White"})

    while(True):

        if (chessGame.whiteCheckMate == True or chessGame.blackCheckMate == True):
            print("Game over!")
            break

        #Display current status of the board
        chessGame.printGameState()

        #Accept input for the current turn
        moveInput = input(f"{colorMap[chessGame.currentColor]} turn to enter move (oldx, oldy, newx, newy): ")
        intInputs = str_to_int(re.findall(r"\d", moveInput))

        #Invalid input
        if (len(intInputs) != 4):
            print("Invalid input, try again")
            continue

        #Legal move check
        if (not (intInputs[2], intInputs[3]) in chessGame.getPieceLegalMoves(intInputs[0], intInputs[1])):
            print("Illegal move, try again")
            continue

        #Correct color check
        if (not chessGame.board.sameColor(intInputs[0], intInputs[1], chessGame.currentColor)):
            print("You are moving the opponent's piece, try again")
            continue

        #Check / Checkmate ?


        #Apply move
        chessGame.move(intInputs[0], intInputs[1], intInputs[2], intInputs[3])

        #Go to next turn
        chessGame.nextTurn()




def str_to_int(strList : list) -> list:
    return [int(s) for s in strList]

main()