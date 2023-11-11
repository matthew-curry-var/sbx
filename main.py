from Chess import *
from unitTests import *
from LenaAI import LenaAI
import re


def main():


    chessGame = Chess()

    while(True):

        if (chessGame.checkMateFlag):
            print("Checkmate!")
            print("Congratulations to: ", COLOR_STR[(chessGame.currentColor + 1) % 2])
            chessGame.printGameState()
            break

        chessGame.printGameState()

        if (chessGame.checkCond[0] == True):
            print("Black is in check!")
        if (chessGame.checkCond[1] == True):
            print("White is in check!")

        #Accept input for the current turn
        moveInput = input(f"{COLOR_STR[chessGame.currentColor]} turn to enter move (oldx, oldy, newx, newy): ")
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
        
        #Apply move
        chessGame.move(intInputs[0], intInputs[1], intInputs[2], intInputs[3])
        
    
        
        

def str_to_int(strList : list) -> list:
    return [int(s) for s in strList]

main()