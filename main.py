from Chess import *
from unitTests import *
from util import *
from LenaAI import LenaAI
import re
import tkinter as tk

def main():

    chessGame = Chess()
    lena_AI = LenaAI(0)

    while (True) :

        if (chessGame.checkMate[0] == True):
            print("White wins!")
            break
        elif (chessGame.checkMate[1] == True):
            print("Black wins!")
            break

        chessGame.printGameState()

        #print("Black moves: ", chessGame.moves[0])
        #print("White moves: ", chessGame.moves[1])

        #print("White King Loc: ", chessGame.kingLocs[1])
        #print("Black King Loc: ", chessGame.kingLocs[0])

        #print("White Moves: ", chessGame.moves[1])
        #print("Black Moves: ", chessGame.moves[0])
        
        inputVal = input("Enter input for next move (x0, y1, x2, y2): ")
        inputs = re.match(pattern=r"^\d{4}", string=inputVal)
        inputsList = tuple(inputs.group(0))
        print("User input: ", inputsList)

        chessGame.applyMove(inputsList)
        chessGame.applyMove(lena_AI.getNextMove(chessGame))
        





main()