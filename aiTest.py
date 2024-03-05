from Chess import Chess
from LenaAI import LenaAI

def main():
    chessGame = Chess()
    chessGame.printGameState()
    lena = LenaAI(0)
    
    chessGame.move(1, 1, 1, 3) #W
    chessGame.move(3, 6, 3, 4) #B
    chessGame.move(2, 1, 2, 3) #W
    chessGame.move(6, 7, 5, 5) #B
    chessGame.move(7, 1, 7, 3) #W

    chessGame.printGameState()

    print(lena.getNextMove(chessGame))



main()
