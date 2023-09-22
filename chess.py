from pieces import King, Queen, Pawn, Bishop, Rook, Knight, Side

black = Side(King(1,1), Queen(1,1), Bishop(1,1), Bishop(1,1), Knight(1,1), Knight(1,1), Rook(1,1), Rook(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1))
white = Side(King(1,1), Queen(1,1), Bishop(1,1), Bishop(1,1), Knight(1,1), Knight(1,1), Rook(1,1), Rook(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1), Pawn(1,1))

print(black.king.x)
