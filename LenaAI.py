from Chess import Chess

class LenaAI:

    #NOT USABLE IN THIS CLONE

    def __init__(self):
        self.gameState = None
        self.color = 0 #default AI to play as black

    """getNextMove: parent caller function for tree search"""
    def getNextMove(self, currGameState : Chess) -> tuple:
        depth, alpha, beta = 3, float('-inf'), float('inf')
        self.gameState = currGameState
        bestMove = self.miniMaxTreeSearch(depth, alpha, beta, maximize=True, color=self.color)
        self.gameState = None
        return bestMove
 
    """miniMaxTreeSearch: descend the tree of possible gamestates pursuant to minimax algorithm"""
    def miniMaxTreeSearch(self, depth : int, alpha : int, beta : int, maximize : False, color : int):
        if (depth == 0 or self.gameState.isGameOver()):
            return (self.gameState.evaluate(color), None)
        else:
            if maximize:
                #find legal moves for color
                #apply move
                #recursive call
                #un-apply move
                #use alpha-beta to prune
                pass
            else:
                pass

    