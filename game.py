from pieces import King, Queen, Pawn, Bishop, Rook, Knight, Side


class Board:
    def __init__(self, blk, wht):
        self.blk = blk
        self.wht = wht
        # Both of these update with the black and white sides as they are.
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.wht_move = True
        self.piece_idx = [King, Queen, Bishop, Knight, Rook, Pawn]
        self.piece_list = blk.piece_list + wht.piece_list
        self.wht_enPassantSquares = []
        self.blk_enPassantSquares = []
        self.enPassantCapturedPiece = []
    def setup_board(self):
        # Adds the objects to the board
        for piece in (self.blk.piece_list + self.wht.piece_list):
            x, y = piece.x, piece.y
            if self.board[x][y] != 0:
                raise ValueError('Two positions for pieces are duplicates')
            # Raises an error if two pieces are set in the same place.
            self.board[piece.x][piece.y] = piece

    def next_move(self, init_x, init_y, final_x, final_y, chessboard):
        chessboard.enPassantCapturedPiece = []
        valid_move = False
        if self.board[init_x][init_y] != 0:
            if self.board[init_x][init_y].colour == self.wht_move:
                if type(self.board[init_x][init_y]) == Pawn:
                    if self.wht_move:
                        _ = self.board[init_x][init_y].canMove(final_x, final_y, self.board,
                                                               enPassantMoves=self.blk_enPassantSquares, chessboard=chessboard)
                    else:
                        _ = self.board[init_x][init_y].canMove(final_x, final_y, self.board,
                                                               enPassantMoves=self.wht_enPassantSquares, chessboard=chessboard)
                    if type(_) == bool:
                        valid_move = _
                    else:
                        if self.wht_move:
                            valid_move, self.wht_enPassantSquares = _
                        else:
                            valid_move, self.blk_enPassantSquares = _
                else:
                    valid_move = self.board[init_x][init_y].canMove(final_x, final_y, self.board)

                # Checks whether the piece can move to the desired place. True if it can, false if cannot
            else:
                print('Not your piece')

            if valid_move is not True:
                print('Invalid move. Try again.')
                return []
            else:
                if type(self.board[init_x][init_y]) == Pawn and ((self.wht_move and final_y == 7) or
                                                                 (self.wht_move and final_y == 0)):
                    print('Which piece do you want to replace the pawn? '
                          '1 for Queen, 2 for Bishop, 3 for Knight and 4 for Rook')
                    index = int(input())
                    self.board[init_x][init_y] = self.piece_idx[index](final_x, final_y, self.wht_move)
        else:
            print('Click a piece')
            return []
        if type(self.board[init_x][init_y]) != King:
            if self.wht_move:
                if self.wht.king.inCheck(self.wht.king.x, self.wht.king.y, self.wht.king.x, self.wht.king.y, self.board):
                    print('Moves the white king into check. Invalid move.')
                    return []

            else:
                if self.blk.king.inCheck(self.blk.king.x, self.blk.king.y, self.blk.king.x, self.blk.king.y, self.board):
                    print('Moves the black king into check. Invalid move.')
                    return []

        self.move_piece((init_x, init_y), (final_x, final_y))
        # Updates board and piece x and y
        if self.wht_move:
            self.blk_enPassantSquares = []
        else:
            self.wht_enPassantSquares = []
        self.wht_move = not self.wht_move
        # Changes turn
        return (init_x, init_y), (final_x, final_y)

    def move_piece(self, init_pos, final_pos):
        self.board[final_pos[0]][final_pos[1]] = self.board[init_pos[0]][init_pos[1]]
        self.board[init_pos[0]][init_pos[1]] = 0
        self.board[final_pos[0]][final_pos[1]].move(final_pos[0], final_pos[1])


black = Side(King(4, 7, False), Queen(3, 7, False), Bishop(2, 7, False), Bishop(5, 7, False), Knight(1, 7, False),
             Knight(6, 7, False), Rook(0, 7, False), Rook(7, 7, False), Pawn(0, 6, False), Pawn(1, 6, False),
             Pawn(2, 6, False), Pawn(3, 6, False), Pawn(4, 6, False), Pawn(5, 6, False), Pawn(6, 6, False),
             Pawn(7, 6, False))

white = Side(King(4, 0, True), Queen(3, 0, True), Bishop(2, 0, True), Bishop(5, 0, True), Knight(1, 0, True),
             Knight(6, 0, True), Rook(0, 0, True), Rook(7, 0, True), Pawn(0, 1, True), Pawn(1, 1, True),
             Pawn(2, 1, True), Pawn(3, 1, True), Pawn(4, 1, True), Pawn(5, 1, True), Pawn(6, 1, True), Pawn(7, 1, True))

# Initialises 2 instances of the class side, with the pieces in position
