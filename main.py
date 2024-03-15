from engine.Chess import *
from utility.util import *
from search.LenaAI import LenaAI
import re, pygame

#GUI Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 1200
R_COLOR, G_COLOR, B_COLOR = 195, 209, 157
SQUARE_SIZE = 83.75
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chess")

#Load chessboard images
chessboard_image = pygame.image.load("img/img/blank-chess-board.gif")
ai_image = pygame.image.load("img/img/alan-turing-9512017-1-402.jpg").convert_alpha()
piece_images = {
    #Black piece set
    "img/Chess_rdt60.png" : pygame.image.load("img/Chess_rdt60.png"),
    "img/Chess_ndt60.png" : pygame.image.load("img/Chess_ndt60.png"),
    "img/Chess_bdt60.png" : pygame.image.load("img/Chess_bdt60.png"),
    "img/Chess_qdt60.png" : pygame.image.load("img/Chess_qdt60.png"),
    "img/Chess_kdt60.png" : pygame.image.load("img/Chess_kdt60.png"),
    "img/Chess_bdt60.png" : pygame.image.load("img/Chess_bdt60.png"),
    "img/Chess_ndt60.png" : pygame.image.load("img/Chess_ndt60.png"),
    "img/Chess_rdt60.png" : pygame.image.load("img/Chess_rdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    "img/Chess_pdt60.png" : pygame.image.load("img/Chess_pdt60.png"),
    #White piece set
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_plt60.png" : pygame.image.load("img/Chess_plt60.png"),
    "img/Chess_rlt60.png" : pygame.image.load("img/Chess_rlt60.png"),
    "img/Chess_nlt60.png" : pygame.image.load("img/Chess_nlt60.png"),
    "img/Chess_blt60.png" : pygame.image.load("img/Chess_blt60.png"),
    "img/Chess_qlt60.png" : pygame.image.load("img/Chess_qlt60.png"),
    "img/Chess_klt60.png" : pygame.image.load("img/Chess_klt60.png"),
    "img/Chess_blt60.png" : pygame.image.load("img/Chess_blt60.png"),
    "img/Chess_nlt60.png" : pygame.image.load("img/Chess_nlt60.png"),
    "img/Chess_rlt60.png" : pygame.image.load("img/Chess_rlt60.png")
    }

def main():

    chessGame = Chess()
    lena_AI = LenaAI(0)

    piece_image_src = {
    #Black piece set
    (0, 0) : "img/Chess_rdt60.png",
    (1, 0) : "img/Chess_ndt60.png",
    (2, 0) : "img/Chess_bdt60.png",
    (3, 0) : "img/Chess_qdt60.png",
    (4, 0) : "img/Chess_kdt60.png",
    (5, 0) : "img/Chess_bdt60.png",
    (6, 0) : "img/Chess_ndt60.png",
    (7, 0) : "img/Chess_rdt60.png",
    (0, 1) : "img/Chess_pdt60.png",
    (1, 1) : "img/Chess_pdt60.png",
    (2, 1) : "img/Chess_pdt60.png",
    (3, 1) : "img/Chess_pdt60.png",
    (4, 1) : "img/Chess_pdt60.png",
    (5, 1) : "img/Chess_pdt60.png",
    (6, 1) : "img/Chess_pdt60.png",
    (7, 1) : "img/Chess_pdt60.png",
    #White piece set
    (0, 6) : "img/Chess_plt60.png",
    (1, 6) : "img/Chess_plt60.png",
    (2, 6) : "img/Chess_plt60.png",
    (3, 6) : "img/Chess_plt60.png",
    (4, 6) : "img/Chess_plt60.png",
    (5, 6) : "img/Chess_plt60.png",
    (6, 6) : "img/Chess_plt60.png",
    (7, 6) : "img/Chess_plt60.png",
    (0, 7) : "img/Chess_rlt60.png",
    (1, 7) : "img/Chess_nlt60.png",
    (2, 7) : "img/Chess_blt60.png",
    (3, 7) : "img/Chess_qlt60.png",
    (4, 7) : "img/Chess_klt60.png",
    (5, 7) : "img/Chess_blt60.png",
    (6, 7) : "img/Chess_nlt60.png",
    (7, 7) : "img/Chess_rlt60.png"
    }


    # Keep track of the currently dragged piece
    dragged_piece = None
    offset_x = 0
    offset_y = 0
    running = True


    #Caution! The below code is my naive GUI and will certainly be reimplemented in later iterations

    while (running):

        #Event detection (this could use some improvement)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                break


            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                square_x = (mouse_x - 60) // 83.75
                square_y = (mouse_y - 60) // 83.75
                clicked_square = (square_x, square_y)

                # Check if a piece is clicked
                if clicked_square in piece_image_src:                                   
                    # Set the dragged piece and calculate offset
                    dragged_piece = piece_image_src[clicked_square]
                    offset_x = mouse_x - ((clicked_square[0] * SQUARE_SIZE) + 70)
                    offset_y = mouse_y - ((clicked_square[1] * SQUARE_SIZE) + 70)
            elif event.type == pygame.MOUSEBUTTONUP:
                # Release the dragged piece
                if dragged_piece:
                    square_x = (mouse_x - 60) // 83.75
                    square_y = (mouse_y - 60) // 83.75
                    dropped_square = (square_x, square_y)
                    if (clicked_square != dropped_square):
                        #Alter Y-values for coordinate representation conversion
                        chessGame.applyMove((clicked_square[0], 7 - clicked_square[1], dropped_square[0], 7 - dropped_square[1]))
                        chessGame.printGameState()
                        piece_image_src[dropped_square] = dragged_piece
                        piece_image_src.pop(clicked_square)
                        
                        #Conduct opponent move in context-switch
                        opponentMove = lena_AI.getNextMove(chessGame)
                        chessGame.applyMove((opponentMove[0], opponentMove[1], opponentMove[2], opponentMove[3]))
                        og_square, dest_square = (opponentMove[0], 7 - opponentMove[1]), (opponentMove[2], 7 - opponentMove[3])
                        dragged_piece = piece_image_src[og_square]
                        piece_image_src[dest_square] = dragged_piece
                        piece_image_src.pop(og_square)

                        dragged_piece = None

                        break

        
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