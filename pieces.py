class Side:
    def __init__(self, king, queen, bishop1, bishop2, knight1, knight2, rook1, rook2, pawn1, pawn2, pawn3, pawn4, pawn5,
                 pawn6, pawn7, pawn8):
        self.king = king
        self.queen = queen
        self.bishop1 = bishop1
        self.bishop2 = bishop2
        self.knight1, self.knight2 = knight1, knight2
        self.rook1, self.rook2 = rook1, rook2
        self.pawn1, self.pawn2, self.pawn3, self.pawn4, self.pawn5, self.pawn6, self.pawn7, self.pawn8 = pawn1, pawn2,\
            pawn3, pawn4, pawn5, pawn6, pawn7, pawn8
        self.piece_list = [self.king, self.queen, self.bishop1, self.bishop2, self.knight1, self.knight2, self.rook1,
                           self.rook2, self.pawn1, self.pawn2, self.pawn3, self.pawn4, self.pawn5, self.pawn6,
                           self.pawn7, self.pawn8]

class Pawn:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.hasMoved = False

    def canMove(self, x, y, board):
        print(x,y, self.x, self.y)
        if 0 <= y <= 7 and 0 <= x <= 7:
            if self.colour:
                multiplier = 1
            else:
                multiplier = -1
            print(board)
            print(board[x][y+multiplier * 1], y-multiplier * 1)
            if y == self.y + multiplier * 1:
                if x == self.x and board[x][y] == 0:
                    return True
                elif (x == self.x - 1 and x >= 0 and board[x][y] != 0) or \
                        (x == self.x + 1 and x <= 7 and board[x][y] != 0):
                    return board[x][y].colour is not self.colour
                else:
                    return False
            elif y == self.y + multiplier * 2 and not self.hasMoved and board[x][y-multiplier * 1] == 0 and \
                    board[x][y] == 0:
                return True
        return False

    def move(self, x, y):
        self.x = x
        self.y = y
        self.hasMoved = True

class Bishop:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

class Queen:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

class King:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

class Rook:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

class Knight:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
