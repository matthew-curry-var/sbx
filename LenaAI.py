from Chess import Chess
from BoardState import BoardState
from util import CHESS_PIECE_SCORE, BOARD_LEN

class LenaAI:

    def __init__(self, playingColor):
        self.color = playingColor


    """getNextMove: parent caller function for tree search"""
    def getNextMove(self, root : Chess) -> tuple:
        a_i, b_i = float('-inf'), float('inf')
        n = self.minMaxTS(board=root, depth=2, a=a_i, b=b_i, maxSel=True, color=self.color, pMoves=[])
        return n[1][0]
        
 
    """minMaxTS: descend the tree of possible gamestates pursuant to minimax algorithm"""
    def minMaxTS(self, board : Chess, depth : int, a : int, b : int, maxSel : bool, color : int, pMoves : list) -> tuple:
        if (not depth or board.checkMate[0] or board.checkMate[1]):
            return (self.naiveEval(board), pMoves)
        else:
            moves = board.moves[color]
            if (maxSel):
                node = (float('-inf'), pMoves)
                for move in moves:

                    temp1= board.getBoardPiece(move[0], move[1]) #Prologue
                    temp2 = board.getBoardPiece(move[2], move[3])
                    board.applyMove(move)

                    descend = self.minMaxTS(board, depth-1, a, b, False, (color+1)%2, pMoves + [move])

                    if (node[0] < descend[0]):
                        node = descend

                    board.board.place(move[0], move[1], temp1) #Epilogue
                    board.board.place(move[2], move[3], temp2)

                    if (node[0] > b):
                        print("Breaking Beta")
                        break

                    a = max(a, node[0])
                return node


            else:
                node = (float('inf'), pMoves)
                for move in moves:

                    temp1 = board.getBoardPiece(move[0], move[1]) #Prologue
                    temp2 = board.getBoardPiece(move[2], move[3])
                    board.applyMove(move)

                    descend = self.minMaxTS(board, depth-1, a, b, True, (color+1)%2, pMoves + [move])
        
                    if (node[0] > descend[0]):
                        node = descend

                    board.board.place(move[0], move[1], temp1) #Epilogue
                    board.board.place(move[2], move[3], temp2)

                    if (node[0] < a):
                        print("Breaking Alpha")
                        break

                    b = min(b, node[0])
                return node

    #This heuristic is hilariously bad
    """naiveEval: return naive chess score for LenaAI's color (this could be a temporary heuristic)"""
    def naiveEval(self, state : Chess) -> int:
        score = 0
        for i in range(BOARD_LEN):
            for j in range(BOARD_LEN):
                b = state.getBoardPiece(i, j)
                if (b):
                    if (b % 2 == self.color):
                        score += CHESS_PIECE_SCORE[b]
                    else:
                        score -= CHESS_PIECE_SCORE[b]

        return score
    

#Building a good chess evaluation function
#Mobility
#King Safety
#Pawn Structure
#Control of Space
#Piece Coordination
