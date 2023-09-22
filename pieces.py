class Side:
    def __init__(self, king, queen, bishop1, bishop2, knight1, knight2, rook1, rook2, pawn1, pawn2, pawn3, pawn4, pawn5, pawn6, pawn7, pawn8):
        self.king = king
        self.queen = queen
        self.bishop1 = bishop1
        self.bishop2 = bishop2
        self.knight1, self.knight2 = knight1, knight2
        self.rook1, self.rook2 = rook1, rook2
        self.pawn1, self.pawn2, self.pawn3, self.pawn4, self.pawn5, self.pawn6, self.pawn7, self.pawn8 = pawn1, pawn2, pawn3, pawn4, pawn5, pawn6, pawn7, pawn8

class Pawn:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bishop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class King:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rook:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Knight:
    def __init__(self, x, y):
        self.x = x
        self.y = y