from Chess import *
from unitTests import *
from util import *
from LenaAI import LenaAI
import re

def main():

    
    chessGame = Chess()
    while (True) :
        chessGame.printGameState()

        print("White King Loc: ", chessGame.kingLocs[1])
        print("Black King Loc: ", chessGame.kingLocs[0])
        
        inputVal = input("Enter input for next move (x0, y1, x2, y2): ")
        inputs = re.match(pattern=r"^\d{4}", string=inputVal)
        inputsList = list(inputs.group(0))
        chessGame.move(int(inputsList[0]), int(inputsList[1]), int(inputsList[2]), int(inputsList[3]))

main()