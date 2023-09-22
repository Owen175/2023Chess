from pieces import King, Queen, Pawn, Bishop, Rook, Knight, Side


class Board:
    def __init__(self, blk, wht):
        self.blk = blk
        self.wht = wht
        # Both of these update with the black and white sides as they are.
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    def setup_board(self):
        for blk_piece in self.blk:
            x, y = blk_piece.x, blk_piece.y
            if self.board[x][y] != 0:
                print('2 pieces have been given the same start position. Error.')
            self.board[blk_piece.x][blk_piece.y] = blk_piece


black = Side(King(5, 7, False), Queen(4, 7, False), Bishop(2, 7, False), Bishop(5, 7, False), Knight(1, 7, False),
             Knight(6, 7, False), Rook(0, 7, False), Rook(7, 7, False), Pawn(0, 6, False), Pawn(1, 6, False),
             Pawn(2, 6, False), Pawn(3, 6, False), Pawn(4, 6, False), Pawn(5, 6, False), Pawn(6, 6, False),
             Pawn(7, 6, False))

white = Side(King(5, 0, True), Queen(4, 0, True), Bishop(2, 0, True), Bishop(5, 0, True), Knight(1, 0, True),
             Knight(6, 0, True), Rook(0, 0, True), Rook(7, 0, True), Pawn(0, 1, True), Pawn(1, 1, True),
             Pawn(2, 1, True), Pawn(3, 1, True), Pawn(4, 1, True), Pawn(5, 1, True), Pawn(6, 1, True), Pawn(7, 1, True))

chessboard = Board(black, white)
black.king.x = 1
chessboard.test()