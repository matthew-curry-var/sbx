""" 
Parser

K:King, Q:Queen, R:Rook, B:Bishop, N:Knight, Pawns do not have a character

Each turn counts as: <White move, Black move> w/ space delimiter (e.g. "Nf3 d6" or "e4 c5")

If we have a string of algebraic moves: "d4 a6 Nc3 h6 b3 Rh7 ..."

A parser can be built to convert algebraic notation to moves that can be input onto a board:

Parser Notes:
    1. Load in string which contains an entire game of chess in algebraic notation.
    2. Each move is seperated by space delimiter, so we can iterate through each move (keeping track of white/black player).
    3. Once move is identified, determine which exact piece is moving based on move capabilities on the current board.
    4. Apply move.
    
"""

from engine.Chess import Chess

class Parser(Chess):

    def __init__(self):
        self.chessBoard = Chess()

    """translate: takes input string s which contains a chess game in algebraic notation and converts to a list of coordinate moves."""
    def translate(self, s : str) -> list:
        move, moveList, strlen = "", list(), s.__len__()
        for i in range(strlen):
            if ((s[i] == " " or i == strlen - 1) and len(move) != 0):
                moveList.append(move)
                move = ""
            else:
                move += s[i]
        return moveList


sample_chess_match = "e4 e5 Nf3 d6 d4 Bg4 d4xe5 Bxf3 Qxf3 d6xe5 Bc4 Nf6 Qb3 Qe7 Nc3 c6 Bg5 b5 Nxb5 c6xb5 Bxb5+ Nd7 0-0-0 Rd8 Rxd7 Rxd7 Rd1 Qe6 Bxd7+ Nxd7 Rd1 Qe6 Bxd7+ Nxd7 Qb8+ Nxb8 Rd8#"
p = Parser()
print(p.translate(sample_chess_match))


#Class still under construction.
