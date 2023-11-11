from Chess import *
from unitTests import *
from util import *
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
        moveInput = input(f"{COLOR_STR[chessGame.currentColor]} turn to enter move (e.g. a3d6, f1f8): ")
        inputs = str_to_lst(re.findall(r"([a-hA-H]\d[a-hA-H]\d)", moveInput)[0])
        inputs = [CHESS_ALPHA_NUM_COLS[inputs[0]], int(inputs[1]) - 1, CHESS_ALPHA_NUM_COLS[inputs[2]], int(inputs[3]) - 1]

        #Invalid input
        if (len(inputs) != 4 or len(inputs) == 0):
            print("Invalid input, try again")
            continue
        #Legal move check
        if (not (inputs[2], inputs[3]) in chessGame.getPieceLegalMoves(inputs[0], inputs[1])):
            print("Illegal move, try again")
            continue
        #Correct color check
        if (not chessGame.board.sameColor(inputs[0], inputs[1], chessGame.currentColor)):
            print("You are moving the opponent's piece, try again")
            continue
        
        #Apply move
        chessGame.move(inputs[0], inputs[1], inputs[2], inputs[3])
        

main()