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

        chessGame.printGameState()
        moveInput = input(f"{colorMap[chessGame.currentTurn]} turn to enter move (oldx, oldy, newx, newy): ")
        intInputs = str_to_int(re.findall(r"\d+", moveInput))
        if (len(intInputs) != 4):
            print("invalid move input, try again")
        else:



            chessGame.move(intInputs[0], intInputs[1], intInputs[2], intInputs[3])
            chessGame.nextTurn()


def str_to_int(strList : list) -> list:
    return [int(s) for s in strList]

main()