import pygame
from game import Board, black, white

pygame.init()
square_side_len = 100
dimensions = (square_side_len * 8, square_side_len * 8)
chessboard = Board(black, white)
chessboard.setup_board()

pygame.init()

changes = chessboard.next_move()