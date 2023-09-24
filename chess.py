import pygame
from game import Board, black, white
from pieces import Spritesheet


def process_click(x, y, clk_list):
    if len(click_list) == 2:
        moved = chessboard.next_move(clk_list[0], clk_list[1], x, y)
        return [], moved
    else:
        return [x, y], []


def draw_board():
    cboard.fill(white)
    count = 0
    for x in range(8):
        for y in range(8):
            if count % 2 == 0:
                pygame.draw.rect(cboard, white,
                                 [x * square_side_len, y * square_side_len, square_side_len, square_side_len])
            else:
                pygame.draw.rect(cboard, green,
                                 [x * square_side_len, y * square_side_len, square_side_len, square_side_len])
            count += 1
        count -= 1
    pygame.display.update()


def draw_pieces():
    for piece in chessboard.piece_list:
        idx = get_sheet_index(chessboard, (piece.x, piece.y))
        sp_sheet_area = spritesheet.get_piece(idx)

        cboard.blit(spritesheet.sp_sheet, (piece.x * square_side_len, 800 - (piece.y + 1) * square_side_len), sp_sheet_area)

def clear_square(pos):
    x, y = pos
    if (7 * x + y) % 2 == 1:
        pygame.draw.rect(cboard, white,
                         [x * square_side_len, (7-y) * square_side_len, square_side_len, square_side_len])
    else:
        pygame.draw.rect(cboard, green,
                         [x * square_side_len, (7-y) * square_side_len, square_side_len, square_side_len])


def get_sheet_index(cb, cgs):
    piece = cb.board[cgs[0]][cgs[1]]
    idx = cb.piece_idx.index(type(piece))
    colour = piece.colour
    if not colour:
        idx += 6
    return idx


chessboard = Board(black, white)
chessboard.setup_board()

pygame.init()
square_side_len = 100
white, green = (236, 236, 212), (116, 148, 84)
dimensions = (square_side_len * 8, square_side_len * 8)

cboard = pygame.display.set_mode(dimensions)
draw_board()

pygame.display.set_caption('Chess')
spritesheet = Spritesheet()
draw_pieces()
pygame.display.update()

gameEnd = False

click_list = []

while not gameEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_list, changes = process_click(event.pos[0] // square_side_len,
                                                    7 - event.pos[1] // square_side_len, click_list)
                # Check for check. If check, dont allow any changes.
                if len(changes) == 2:
                    idx = get_sheet_index(chessboard, changes[1])
                    sp_sheet_area = spritesheet.get_piece(idx)
                    x, y = changes[1][0], changes[1][1]
                    print(changes)
                    clear_square(changes[0])
                    clear_square(changes[1])
                    cboard.blit(spritesheet.sp_sheet, (x * square_side_len, 800 - (y + 1) * square_side_len),
                                sp_sheet_area)
                    pygame.display.update()

# En Passant
# If king in check, make sure that the next move gets out of it.
#