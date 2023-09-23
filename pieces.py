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


class Pawn:
    def __init__(self, x, y, colour):
        self.x, self.y = x, y

        self.colour = colour
        self.hasMoved = False
        # hasMoved is used for pawn double movement.

    def canMove(self, x, y, board):
        if self.colour:
            multiplier = 1
        else:
            multiplier = -1

        if y == self.y + multiplier * 1:    # Checks if the piece is moving one square forwards.
            if x == self.x and board[x][y] == 0:    # Checks if the square in front is to be moved to, and is empty.
                return True
            elif (x == self.x - 1 and x >= 0 and board[x][y] != 0) or \
                    (x == self.x + 1 and x <= 7 and board[x][y] != 0):  # Checks if the square being moved to is diagonal
                return board[x][y].colour is not self.colour    # Returns True if the piece can be taken.
            else:
                return False
        elif y == self.y + multiplier * 2 and not self.hasMoved and board[x][y - multiplier * 1] == 0 and \
                board[x][y] == 0:   # Checks for double jump.
            return True

        return False

    def move(self, x, y):
        self.x, self.y = x, y
        self.hasMoved = True


class Bishop:
    def __init__(self, x, y, colour):
        self.x, self.y = x, y

        self.colour = colour

    def canMove(self, x, y, board):
        if abs(x - self.x) == abs(y - self.y) and x - self.x != 0 and y - self.y != 0:  # Checks whether it is diagonal
            distance = x - self.x   # Absolute distance is constant between x and y.
            if distance < 0:
                x_multiplier = -1
            else:
                x_multiplier = 1
            if y - self.y < 0:
                y_multiplier = -1
            else:
                y_multiplier = 1

            for i in range(1, abs(distance)):
                if board[self.x + x_multiplier * i][self.y + y_multiplier * i] != 0:    # Returns false if the move jumps pieces.
                    return False
            if board[x][y] == 0:
                return True
            elif board[x][y].colour is not self.colour:
                return True

        return False

    def move(self, x, y):
        self.x, self.y = x, y


class Queen:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour


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
                    if board[self.x + x_multiplier * i][self.y + y_multiplier * i] != 0:    # Returns false if the move jumps pieces.
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

    def move(self, x, y):
        self.x, self.y = x, y


class King:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour


    def canMove(self, x, y, board):
        pass

class Rook:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

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
                for i in range(1, y_change-1):
                    if board[x][self.y + y_multiplier * i] != 0:    # Returns false if the move jumps pieces.
                        return False

            if y_change == 0:
                for i in range(1, x_change - 1):
                    if board[self.x + x_multiplier * i][y] != 0:    # Returns false if the move jumps pieces.
                        return False

            if board[x][y] == 0:
                return True
            elif board[x][y].colour is not self.colour:
                return True

        return False

    def move(self, x, y):
        self.x, self.y = x, y


class Knight:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
