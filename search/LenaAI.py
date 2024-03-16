from engine.Chess import Chess
from engine.BoardState import BoardState
from utility.util import *

class LenaAI:

    def __init__(self, playingColor):
        self.color = playingColor


    """getNextMove: parent caller function for tree search"""
    def getNextMove(self, root : Chess) -> tuple:
        a_i, b_i = float('-inf'), float('inf')
        #root.colorFilter = True
        n = self.minMaxTS(board=root, depth=2, a=a_i, b=b_i, maxSel=True, color=self.color, pMoves=[])
        #root.colorFilter = False
        #print("Return Node: ", n)
        #print("Curr color: ", root.currentColor)
        return n[1][0]
        
 
    """minMaxTS: descend the tree of possible gamestates pursuant to minimax algorithm"""
    def minMaxTS(self, board : Chess, depth : int, a : int, b : int, maxSel : bool, color : int, pMoves : list) -> tuple:
        if (not depth or board.checkMate[0] or board.checkMate[1]):
            eval = self.eval(board)
            #print((eval, pMoves))   #There is a bug with the current color of chess and applying the AI's move. How can I make it work?
            return (eval, pMoves)
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
                    board.currentColor = color

                    if (node[0] > b):
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
                    board.currentColor = color

                    
                    if (node[0] < a):
                        #print("   " * abs(depth-2), "Breaking Alpha")
                        #print("   " * abs(depth-2), "node[0] yielded: ", node[0])
                        #print("   " * abs(depth-2), "Alpha value: ", a)
                        break

                    b = min(b, node[0])


                return node

    
    """
    Feature Engineering:
    1) Material                             -> Use CHESS_PIECE_SCORE to come up with material score
    2) Mobility (exclude pawns/kings)       -> Calculate mobility for non-pawns, non-kings
    3) Pawn Structure                       -> Pawns that are backed up by other pieces
    4) Control of Space                     -> Look at the board itself, see how the control space (what is a "good" control space?)
    5) Piece Coordination (?)               -> Look at pieces that are highly coordinated (offense/defense?)
    """

    def eval(self, state : Chess) -> int:
        #print("Inside evaluation function: ")
        material_score = self.material_eval(state)
        #print("Material Score = ", material_score)
        mobility_score = self.mobility_eval(state)
        #print("Mobility Score = ", mobility_score)
        pawn_struct_score = self.pawn_struct_eval(state)
        #print("Pawn Structure Score = ", pawn_struct_score)
        return (5 * material_score) + (0.2 * mobility_score) + (0.5 * pawn_struct_score)


    #eventually combine into a single function for 1 iteration

    def material_eval(self, state : Chess) -> int:
        score = 0
        for i in range(BOARD_LEN):
            for j in range(BOARD_LEN):
                b = state.getBoardPiece(i, j)
                if (b):
                    score += CHESS_PIECE_SCORE[b]    
        return score
    
    def mobility_eval(self, state : Chess) -> int:
        score = 0
        for i in range(BOARD_LEN):
            for j in range(BOARD_LEN):
                if (state.getBoardPiece(i, j)):
                    score += len(state.getPieceLegalMoves(i, j))
        return score
    
    def pawn_struct_eval(self, state : Chess) -> int:
        score = 0
        for i in range(BOARD_LEN):
            for j in range(BOARD_LEN):
                b = state.getBoardPiece(i, j)
                if (b and (b == PAWNS[self.color])):
                    #score += 1 for any number of adjacent pawns
                    #print(adjacent_squares(i, j))
                    adjacent = adjacent_squares(i, j)
                    for a in adjacent:
                        if state.getBoardPiece(a[0], a[1]) == PAWNS[self.color]:
                            score += 1
        return score

