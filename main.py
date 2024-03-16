from engine.Chess import *
from utility.util import *
from search.LenaAI import LenaAI
import re, pygame

#GUI Constants / Setup
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 1200
R_COLOR, G_COLOR, B_COLOR = 195, 209, 157
SQUARE_SIZE, MARGIN_LEN = 83.75, 60
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chess")

#Load image files as pygame images objects
chessboard_image = pygame.image.load("img/img/blank-chess-board.gif")
ai_image = pygame.image.load("img/img/alan-turing-9512017-1-402.jpg").convert_alpha()
piece_images = {
    "img/Chess_rdt60.png" : pygame.image.load("img/Chess_rdt60.png"), "img/Chess_ndt60.png" : pygame.image.load("img/Chess_ndt60.png"),
    "img/Chess_bdt60.png" : pygame.image.load("img/Chess_bdt60.png"), "img/Chess_qdt60.png" : pygame.image.load("img/Chess_qdt60.png"),
    "img/Chess_kdt60.png" : pygame.image.load("img/Chess_kdt60.png"), "img/Chess_bdt60.png" : pygame.image.load("img/Chess_bdt60.png"),
    "img/Chess_ndt60.png" : pygame.image.load("img/Chess_ndt60.png"), "img/Chess_rdt60.png" : pygame.image.load("img/Chess_rdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"), "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"), "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"), "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"), "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"), "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"), "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"), "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"), "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_rlt60.png" : pygame.image.load("img/Chess_rlt60.png"), "img/Chess_nlt60.png" : pygame.image.load("img/Chess_nlt60.png"),
    "img/Chess_blt60.png" : pygame.image.load("img/Chess_blt60.png"), "img/Chess_qlt60.png" : pygame.image.load("img/Chess_qlt60.png"),
    "img/Chess_klt60.png" : pygame.image.load("img/Chess_klt60.png"), "img/Chess_blt60.png" : pygame.image.load("img/Chess_blt60.png"),
    "img/Chess_nlt60.png" : pygame.image.load("img/Chess_nlt60.png"), "img/Chess_rlt60.png" : pygame.image.load("img/Chess_rlt60.png")
    }


def main():

    #Mapping of positions to image objects used for drawing images
    piece_image_src = {
    (0, 0) : "img/Chess_rdt60.png", (1, 0) : "img/Chess_ndt60.png", (2, 0) : "img/Chess_bdt60.png", (3, 0) : "img/Chess_qdt60.png",
    (4, 0) : "img/Chess_kdt60.png", (5, 0) : "img/Chess_bdt60.png", (6, 0) : "img/Chess_ndt60.png", (7, 0) : "img/Chess_rdt60.png",
    (0, 1) : "img/Chess_pdt60.png", (1, 1) : "img/Chess_pdt60.png", (2, 1) : "img/Chess_pdt60.png", (3, 1) : "img/Chess_pdt60.png",
    (4, 1) : "img/Chess_pdt60.png", (5, 1) : "img/Chess_pdt60.png", (6, 1) : "img/Chess_pdt60.png", (7, 1) : "img/Chess_pdt60.png",
    (0, 6) : "img/Chess_plt60.png", (1, 6) : "img/Chess_plt60.png", (2, 6) : "img/Chess_plt60.png", (3, 6) : "img/Chess_plt60.png",
    (4, 6) : "img/Chess_plt60.png", (5, 6) : "img/Chess_plt60.png", (6, 6) : "img/Chess_plt60.png", (7, 6) : "img/Chess_plt60.png",
    (0, 7) : "img/Chess_rlt60.png", (1, 7) : "img/Chess_nlt60.png", (2, 7) : "img/Chess_blt60.png", (3, 7) : "img/Chess_qlt60.png",
    (4, 7) : "img/Chess_klt60.png", (5, 7) : "img/Chess_blt60.png", (6, 7) : "img/Chess_nlt60.png", (7, 7) : "img/Chess_rlt60.png"
    }

    #Initialize Chess game and opponent
    chessGame = Chess()
    lena_AI = LenaAI(0)

    #GUI control variables
    running, opponent = True, False
    dragged_piece = None
    offset_x, offset_y = 0, 0

    while (running):
        #User event detection
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
                square_x = (mouse_x - MARGIN_LEN) // SQUARE_SIZE
                square_y = (mouse_y - MARGIN_LEN) // SQUARE_SIZE
                clicked_square = (square_x, square_y)

                if clicked_square in piece_image_src.keys():
                    dragged_piece = piece_image_src[clicked_square]
                    offset_x = mouse_x - ((clicked_square[0] * SQUARE_SIZE) + MARGIN_LEN)
                    offset_y = mouse_y - ((clicked_square[1] * SQUARE_SIZE) + MARGIN_LEN)

            elif (event.type == pygame.MOUSEBUTTONUP):
                square_x = (mouse_x - MARGIN_LEN) // SQUARE_SIZE
                square_y = (mouse_y - MARGIN_LEN) // SQUARE_SIZE
                dropped_square = (square_x, square_y)
                if (clicked_square != dropped_square):
                    move = (clicked_square[0], 7 - clicked_square[1], dropped_square[0], 7 - dropped_square[1])
                    if (move in chessGame.moves[1]):
                        piece_image_src[dropped_square] = dragged_piece
                        piece_image_src.pop(clicked_square)
                        opponent = True
                    chessGame.applyMove(move)
                    chessGame.printGameState()
                    dragged_piece = None




        #Calculate and apply opponent move
        if (opponent):
            try:
                opponentMove = lena_AI.getNextMove(chessGame)
                chessGame.applyMove(opponentMove)
                og_square, dest_square = (opponentMove[0], 7 - opponentMove[1]), (opponentMove[2], 7 - opponentMove[3])
                piece_image_src[dest_square] = piece_image_src[og_square]
                piece_image_src.pop(og_square)
                opponent = False
            except:
                print("AI failed to produce move")

        #Draw elements to the board
        screen.fill((R_COLOR, G_COLOR, B_COLOR))
        screen.blit(chessboard_image, (60, 60))
        screen.blit(ai_image, (800, 60))
        for position, piece in piece_image_src.items():
            piece_image = piece_images[piece]
            piece_x = (position[0] * SQUARE_SIZE) + 70
            piece_y = (position[1] * SQUARE_SIZE) + 70
            screen.blit(piece_image, (piece_x, piece_y))


        if dragged_piece:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            piece_x = mouse_x - offset_x
            piece_y = mouse_y - offset_y
            screen.blit(piece_images[dragged_piece], (piece_x, piece_y))

        pygame.display.flip()


main()