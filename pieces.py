import copy

import pygame


class Side:
    def __init__(self, king, queen, bishop1, bishop2, knight1, knight2, rook1, rook2, pawn1, pawn2, pawn3, pawn4, pawn5,
                 pawn6, pawn7, pawn8):
        self.king = king
        self.queen = queen
        self.bishop1 = bishop1
        self.bishop2 = bishop2
        self.knight1, self.knight2 = knight1, knight2
        self.rook1, self.rook2 = rook1, rook2
        self.pawn1, self.pawn2, self.pawn3, self.pawn4, self.pawn5, self.pawn6, self.pawn7, self.pawn8 = pawn1, pawn2, \
            pawn3, pawn4, pawn5, pawn6, pawn7, pawn8
        self.piece_list = [self.king, self.queen, self.bishop1, self.bishop2, self.knight1, self.knight2, self.rook1,
                           self.rook2, self.pawn1, self.pawn2, self.pawn3, self.pawn4, self.pawn5, self.pawn6,
                           self.pawn7, self.pawn8]


class Piece:
    def __init__(self, x, y, colour):
        self.x, self.y = x, y
        self.colour = colour

    def move(self, x, y):
        self.x, self.y = x, y


class Pawn(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)

        self.hasMoved = False
        # hasMoved is used for pawn double movement.

    def canMove(self, x, y, board):
        if self.colour:
            multiplier = 1
        else:
            multiplier = -1

        if y == self.y + multiplier * 1:  # Checks if the piece is moving one square forwards.
            if x == self.x and board[x][y] == 0:  # Checks if the square in front is to be moved to, and is empty.
                return True
            elif (x == self.x - 1 and x >= 0 and board[x][y] != 0) or \
                    (x == self.x + 1 and x <= 7 and board[x][
                        y] != 0):  # Checks if the square being moved to is diagonal
                return board[x][y].colour is not self.colour  # Returns True if the piece can be taken.
            else:
                return False
        elif y == self.y + multiplier * 2 and not self.hasMoved and board[x][y - multiplier * 1] == 0 and \
                board[x][y] == 0:  # Checks for double jump.
            return True

        return False

    def move(self, x, y):
        self.x, self.y = x, y
        self.hasMoved = True


class Bishop(Piece):
    def canMove(self, x, y, board):
        if abs(x - self.x) == abs(y - self.y) and x - self.x != 0 and y - self.y != 0:  # Checks whether it is diagonal
            distance = x - self.x  # Absolute distance is constant between x and y.
            if distance < 0:
                x_multiplier = -1
            else:
                x_multiplier = 1
            if y - self.y < 0:
                y_multiplier = -1
            else:
                y_multiplier = 1

            for i in range(1, abs(distance)):
                if board[self.x + x_multiplier * i][self.y + y_multiplier * i] != 0:
                    # Returns false if the move jumps pieces.
                    return False
            if board[x][y] == 0:
                return True
            elif board[x][y].colour is not self.colour:
                return True

        return False


class Queen(Piece):

    def canMove(self, x, y, board):
        x_change = x - self.x
        y_change = y - self.y
        if x_change < 0:
            x_multiplier = -1
        else:
            x_multiplier = 1
        if y_change < 0:
            y_multiplier = -1
        else:
            y_multiplier = 1

        if not (x_change == 0 and y_change == 0):
            ###########################################
            # Checks for diagonal movement.
            diagonal = False
            if abs(x_change) == abs(y_change) and x - self.x != 0 and y - self.y != 0:  # Checks whether it is diagonal

                for i in range(1, abs(x_change)):
                    if board[self.x + x_multiplier * i][
                        self.y + y_multiplier * i] != 0:  # Returns false if the move jumps pieces.
                        return False
                diagonal = True
            ###########################################

            ###########################################
            # Checks for straight movement
            # if x_change != 0 and y_change != 0:
            #     return False
            straight = False
            if x_change == 0:
                for i in range(1, y_change - 1):
                    if board[x][self.y + y_multiplier * i] != 0:  # Returns false if the move jumps pieces.
                        return False
                straight = True

            if y_change == 0:
                for i in range(1, x_change - 1):
                    if board[self.x + x_multiplier * i][y] != 0:  # Returns false if the move jumps pieces.
                        return False
                straight = True
            if straight or diagonal:
                if board[x][y] == 0:
                    return True
                elif board[x][y].colour is not self.colour:
                    return True
            ###########################################

        return False


class King(Piece):
    def canMove(self, x, y, board):
        if (abs(x - self.x), abs(y - self.y)) in [(1, 1), (1, 0), (0, 1)]:
            if board[x][y] == 0:
                return not self.inCheck(self.x, self.y, x, y, board)
            elif board[x][y].colour is not self.colour:
                return not self.inCheck(self.x, self.y, x, y, board)
        return False

    def inCheck(self, init_x, init_y, x, y, board):
        # return True if in check
        if self.colour:
            multiplier = 1
        else:
            multiplier = -1

        temp_board = copy.deepcopy(board)
        # Does not work with list slicing - you need to deep copy or the board gets changed.
        temp_board[x][y] = temp_board[init_x][init_y]
        temp_board[init_x][init_y] = 0

        # Pawn Check
        if type(temp_board[x - 1][y + multiplier]) == Pawn:
            if temp_board[x - 1][y + multiplier].colour is not self.colour:
                print('p')
                return True
        if type(temp_board[x + 1][y + multiplier]) == Pawn:
            if temp_board[x + 1][y + multiplier].colour is not self.colour:
                print('p')
                return True

        # Knight Check
        knightPosList = [(x + 2, y + 1), (x + 2, y - 1), (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2),
                         (x - 2, y + 1), (x - 2, y - 1)]
        for pos in knightPosList:
            if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7:
                if type(temp_board[pos[0]][pos[1]]) == Knight:
                    if temp_board[pos[0]][pos[1]].colour is not self.colour:
                        print('k')
                        return True

        # King Check
        kingPosList = [(x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y + 1), (x - 1, y),
                       (x - 1, y - 1)]
        for pos in kingPosList:
            if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7:
                if type(temp_board[pos[0]][pos[1]]) == King:
                    if temp_board[pos[0]][pos[1]].colour is not self.colour:
                        print('kng')
                        return True

        # Rook Check + straight Queen check
        temp_x = x
        noPiece = True
        while temp_x >= 0 and noPiece:  # Checks the left of the king
            if temp_board[temp_x][y] != 0:
                noPiece = False
                if type(temp_board[temp_x][y]) == Rook or type(temp_board[temp_x][y]) == Queen:
                    if temp_board[temp_x][y].colour is not self.colour:
                        print('r/q')
                        return True

            temp_x -= 1

        temp_x = x
        noPiece = True
        while temp_x <= 7 and noPiece:  # Checks the right of the king
            if temp_board[temp_x][y] != 0:
                noPiece = False
                if type(temp_board[temp_x][y]) == Rook or type(temp_board[temp_x][y]) == Queen:
                    if temp_board[temp_x][y].colour is not self.colour:
                        print('r/q')
                        return True
            temp_x += 1
        return False

        temp_y = y
        noPiece = True
        while temp_y >= 0 and noPiece:  # Checks above of the king
            if temp_board[x][temp_y] != 0:
                noPiece = False
                if type(temp_board[x][temp_y]) == Rook or type(temp_board[x][temp_y]) == Queen:
                    if temp_board[x][temp_y].colour is not self.colour:
                        print('r/q')
                        return True
            temp_y -= 1

        temp_y = y
        noPiece = True
        while temp_y <= 7 and noPiece:  # Checks below the king
            if temp_board[x][temp_y] != 0:
                noPiece = False
                if type(temp_board[x][temp_y]) == Rook or type(temp_board[x][temp_y]) == Queen:
                    if temp_board[x][temp_y].colour is not self.colour:
                        print('r/q')
                        return True
            temp_y += 1

        # Bishop Check + diagonal Queen check
        temp_x = x
        temp_y = y
        noPiece = True
        while temp_x >= 0 and temp_y >= 0 and noPiece:
            if temp_board[temp_x][temp_y] != 0:
                noPiece = False
                if type(temp_board[temp_x][temp_y]) == Bishop or type(temp_board[temp_x][temp_y]) == Queen:
                    if temp_board[temp_x][temp_y].colour is not self.colour:
                        print('r/q')
                        return True
            temp_x -= 1
            temp_y -= 1

        temp_x = x
        temp_y = y
        noPiece = True
        while temp_x >= 0 and temp_y <= 7 and noPiece:
            if temp_board[temp_x][temp_y] != 0:
                noPiece = False
                if type(temp_board[temp_x][temp_y]) == Bishop or type(temp_board[temp_x][temp_y]) == Queen:
                    if temp_board[temp_x][temp_y].colour is not self.colour:
                        return True
            temp_x -= 1
            temp_y += 1

        temp_x = x
        temp_y = y
        noPiece = True
        while temp_x <= 7 and temp_y >= 0 and noPiece:
            if temp_board[temp_x][temp_y] != 0:
                noPiece = False
                if type(temp_board[temp_x][temp_y]) == Bishop or type(temp_board[temp_x][temp_y]) == Queen:
                    if temp_board[temp_x][temp_y].colour is not self.colour:
                        return True
            temp_x += 1
            temp_y -= 1

        temp_x = x
        temp_y = y
        noPiece = True
        while temp_x <= 7 and temp_y <= 7 and noPiece:
            if temp_board[temp_x][temp_y] != 0:
                noPiece = False
                if type(temp_board[temp_x][temp_y]) == Bishop or type(temp_board[temp_x][temp_y]) == Queen:
                    if temp_board[temp_x][temp_y].colour is not self.colour:
                        return True
            temp_x += 1
            temp_y += 1
        return False
        # Need to make a theoretical board copy when you move it there and check diagonals, straights and knight positions.


class Rook(Piece):
    def canMove(self, x, y, board):
        x_change = x - self.x
        y_change = y - self.y
        if x_change < 0:
            x_multiplier = -1
        else:
            x_multiplier = 1
        if y_change < 0:
            y_multiplier = -1
        else:
            y_multiplier = 1

        if not (x_change == 0 and y_change == 0):
            if x_change != 0 and y_change != 0:
                return False

            if x_change == 0:
                for i in range(1, y_change - 1):
                    if board[x][self.y + y_multiplier * i] != 0:  # Returns false if the move jumps pieces.
                        return False

            if y_change == 0:
                for i in range(1, x_change - 1):
                    if board[self.x + x_multiplier * i][y] != 0:  # Returns false if the move jumps pieces.
                        return False

            if board[x][y] == 0:
                return True
            elif board[x][y].colour is not self.colour:
                return True

        return False


class Knight(Piece):
    def canMove(self, x, y, board):
        abs_vector = (abs(x - self.x), abs(y - self.y))
        if abs_vector in [(1, 2), (2, 1)]:
            if board[x][y] == 0:
                return True
            elif board[x][y].colour is not self.colour:
                return True
        return False


class Spritesheet:
    def __init__(self):
        self.sp_sheet = pygame.image.load('C:/Users/owenc/Documents/Github/chess/Chess/pieces.png').convert_alpha()
        self.rows = 2
        self.cols = 6
        self.rect_count = self.cols * self.rows
        self.rect = self.sp_sheet.get_rect()
        self.cell_width = self.rect.width // self.cols
        self.cell_height = self.rect.height // self.rows
        self.cells = list([(i % self.cols * self.cell_width, i // self.cols * self.cell_height, self.cell_width,
                            self.cell_height) for i in range(self.rect_count)])

    def get_piece(self, i):
        return self.cells[i]
