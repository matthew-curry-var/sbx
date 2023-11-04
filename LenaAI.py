from Chess import Chess
from util import PIECE_SCORE

class LenaAI:

    def __init__(self, colorInput):
        self.color = colorInput

    def treeSearch(self, gameState : Chess, depth=2):
        return

    def evaluate(self, gameState : Chess):
        score = 0
        for m in gameState.getColorPieces(self.color):
            score += PIECE_SCORE[gameState.getBoardPiece(m[0], m[1])]
        return score

    