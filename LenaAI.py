from Chess import Chess
from util import PIECE_SCORE, Stack

class LenaAI:


    #Implementation not yet released.

    def __init__(self, colorInput):
        self.color = colorInput
        self.layerFuncs = [max, min]

    
    """miniMaxTreeSearch: apply depth-limited minimax search algorithm and returns (x0, y0, x1, y1) tuple"""
    def miniMaxTreeSearch(self, gameState : Chess, depth : int) -> tuple:
        if (depth == 0):
            pass
        return


    """evaluate: evaluates chess gamestate to construct a scoreing methodology"""
    def evaluate(self, gameState : Chess):
        score = 0
        for m in gameState.getColorPieces(self.color):
            score += PIECE_SCORE[gameState.getBoardPiece(m[0], m[1])]
        return score

    