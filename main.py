from engine.Chess import *
from utility.util import *
from search.LenaAI import LenaAI
import pygame

#GUI Constants / Setup
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 1200
R_COLOR, G_COLOR, B_COLOR = 0, 0, 0
SQUARE_SIZE, MARGIN_LEN = 84, 60

def main():

    #GUI setup
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Chess")

    #Import positon -> image_loc & image_loc -> pygame image mappings from util
    piece_pos_image = {key: PIECE_POS_SOURCE[key] for key in PIECE_POS_SOURCE.keys()}
    piece_images = {key: PIECE_PYIMAGES[key] for key in PIECE_PYIMAGES.keys()}

    #Initialize Chess game and opponent
    chessGame = Chess()
    lena_AI = LenaAI(0)

    #GUI control variables
    running = True
    select, select_coord = False, None
    opponent = False
    target_moves = list()

    while (running):

        #User event detection
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                break

            elif (event.type == pygame.MOUSEBUTTONDOWN):

                #Find location of button click, piece at location, and possible moves given the current board state
                position_x, position_y = pygame.mouse.get_pos()
                square_x, square_y = int((position_x - MARGIN_LEN) // SQUARE_SIZE), 7 - int((position_y - MARGIN_LEN) // SQUARE_SIZE)
                #print(square_x, square_y)


                if (0 <= square_x <= 7 and 0 <= square_y <= 7):
                    p = chessGame.getBoardPiece(square_x, square_y)
                    p_moves = chessGame.checkMoves(chessGame.getPieceLegalMoves(square_x, square_y), 1)

                    #If there is a piece selected apply move if legal move (else reset select)
                    if (select):
                        move = (select_coord[0], select_coord[1], square_x, square_y)
                        if (move in target_moves):

                            #Apply move to internal chess board and modify GUI representation
                            chessGame.applyMove(move)
                            chessGame.printGameState()
                            piece_pos_image[(square_x, square_y)] = piece_pos_image[(select_coord[0], select_coord[1])]
                            piece_pos_image.pop((select_coord[0], select_coord[1]))
                            opponent = True
                            
                        select, select_coord, target_moves = False, None, None
                        break
                        
                            
                    #If we are selecting a new location, determine if piece eligible for selecting
                    if (p and len(p_moves) != 0):
                        select, select_coord, target_moves = True, (square_x, square_y), p_moves
                        break

                    #No piece selected
                    else:
                        select, select_coord, target_moves = False, None, None

                else:
                    select, select_coord, target_moves = False, None, None


        #If opponent's turn, call getNextMove and apply to gamestate
        if (opponent):
            opponentMove = lena_AI.getNextMove(chessGame)
            chessGame.applyMove(opponentMove)
            piece_pos_image[(opponentMove[2], opponentMove[3])] = piece_pos_image[(opponentMove[0], opponentMove[1])]
            piece_pos_image.pop((opponentMove[0], opponentMove[1]))
            opponent = False
            
    
        #Draw elements to the board
        screen.fill((R_COLOR, G_COLOR, B_COLOR))
        screen.blit(CHESSBOARD_IMAGE, (60, 60))

        if (select):
            screen.blit(SELECT_SQUARE, (MARGIN_LEN + (square_x * SQUARE_SIZE) , (MARGIN_LEN + (7 - square_y) * SQUARE_SIZE)))
            for move in target_moves:
                screen.blit(TARGET_SQUARE, (MARGIN_LEN + (move[2] * SQUARE_SIZE) , (MARGIN_LEN + (7 - move[3]) * SQUARE_SIZE)))


        for position, piece in piece_pos_image.items():
            piece_image = piece_images[piece]
            piece_x = (position[0] * SQUARE_SIZE) + 70
            piece_y = ((7 - position[1]) * SQUARE_SIZE) + 70
            screen.blit(piece_image, (piece_x, piece_y))

        

        pygame.display.flip()


main()