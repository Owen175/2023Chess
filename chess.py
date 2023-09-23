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

    def setup_board(self):
        # Adds the objects to the board
        for piece in (self.blk.piece_list + self.wht.piece_list):
            x, y = piece.x, piece.y
            if self.board[x][y] != 0:
                raise ValueError('Two positions for pieces are duplicates')
            # Raises an error if two pieces are set in the same place.
            self.board[piece.x][piece.y] = piece

    def next_move(self):
        y_conversion = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        range_check = [0, 1, 2, 3, 4, 5, 6, 7]

        if self.wht_move:
            team = 'white'
        else:
            team = 'black'

        # Input is in algebraic chess notation, where A-H represent the x axis and 1-8 represents the y
        valid_move = False
        while valid_move is not True:
            correct_data = False
            while correct_data is not True:
                print(f'What is {team}\'s move')
                move = input()

                init_x = y_conversion.index(move[0].upper())
                init_y = int(move[1]) - 1
                final_x = y_conversion.index(move[2].upper())
                final_y = int(move[3]) - 1
                # Converts from algebraic chess notation to cartesian coordinates, indexed at 0 for the board.

                correct_data = init_x in range_check and init_y in range_check and final_x in range_check and \
                    final_y in range_check
                # Checks that the coordinate values are in the board
                if correct_data is not True:
                    print('Please input data in the range of A-F and 1-8')

            if self.board[init_x][init_y] != 0:
                if self.board[init_x][init_y].colour == self.wht_move:

                    valid_move = self.board[init_x][init_y].canMove(final_x, final_y, self.board)
                    # Checks whether the piece can move to the desired place. True if it can, false if cannot
                else:
                    print('Not your piece')

                if valid_move is not True:
                    print('Invalid move. Try again.')

        self.move_piece((init_x, init_y), (final_x, final_y))
        # Updates board and piece x and y

        self.wht_move = not self.wht_move
        # Changes turn

        self.next_move()

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

chessboard = Board(black, white)
chessboard.setup_board()

chessboard.next_move()
