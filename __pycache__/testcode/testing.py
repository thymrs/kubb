board = """\
.......
.......
..R....
..R....
.....K.
.....P.
.......
\
"""
board1 = board.strip('\n').split()
print(board1)
def checkmate(piece):
    pass

def pawn():
  pawn_board = """\
  . . . . . . .
  . . . . . . .
  . . X . X . .
  . . . P . . .
  . . . . . . .
  . . . . . . .
  . . . . . . .
  . . . . . . .
  """
  pawn, board = "P" in pawn_board, board

  is_check = pawn_check(pawn_board, "P")  # Assuming white pawn here

  if is_check:
    print("The pawn can deliver a check!")
  else:
    print("The pawn cannot deliver a check.")


def bishop():
    bishop_board = """\
        X . . . . . X
        . X . . . X .
        . . X . X . .
        . . . B . . .
        . . X . X . .
        . X . . . X .
        X . . . . . X
        . . . . . . .\
        """
    is_check = bishop_check(bishop_board, "B")  # Call the bishop_check function

    if is_check:
        print("The bishop can deliver a check!")
    else:
        print("The bishop cannot deliver a check.")
        
def find_bishop_position(board, bishop):
  for row in range(8):
    for col in range(8):
      if board[row][col] == bishop:
        return row, col
  raise ValueError("Bishop not found on the board")  # Handle case if bishop is not present

    
def rook():
    rook_board = """\
        . . . X . . .
        . . . X . . .
        . . . X . . .
        X X X R X X X
        . . . X . . .
        . . . X . . .
        . . . X . . .
        . . . X . . .\
        """
    rook = "R" in rook_board, board
    print(rook)
    rook_check = "X" in rook_board #let it know that if King replace X, they can check the King

def queen():
    queen_board = """\
        X . . X . . X
        . X . X . X .
        . . X X X . .
        X X X Q X X X
        . . X X X . .
        . X . X . X .
        X . . X . . X
        . . . X . . .\
        """
    queen = "Q" in queen_board, board
    print(queen)
    queen_check = "X" in queen_board #let it know that if King replace X, they can check the King

def king():
    king_board = """\
        . . . . . . .
        . . . . . . .
        . . X X X . .
        . . X K X . .
        . . X X X . .
        . . . . . . .
        . . . . . . .
        . . . . . . .\
        """
    king = "K" in king_board, board
    print(king)
    
def bishop_check(bishop_board, bishop):
  bishop_row, bishop_col = find_bishop_position(bishop_board, bishop)  # Add a function to find bishop position

  # Check diagonally in all four directions until encountering a piece or the board edge

  for row_offset, col_offset in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
    current_row, current_col = bishop_row + row_offset, bishop_col + col_offset
    while 0 <= current_row < 8 and 0 <= current_col < 8:
      piece_at_current = bishop_board[current_row][current_col]
      if piece_at_current != ".":  # Encountered a piece (including the king)
        if piece_at_current == "X":  # Check if it's the king
          return True
        break  # Stop iterating in this direction
      current_row += row_offset
      current_col += col_offset

  return False

def rook_check(rook_board, rook):
  rook_row, rook_col = find_rook_position(rook_board, rook)  # Add a function to find rook position

  # Check horizontally and vertically until encountering a piece or the board edge

  for row_offset in [-1, 1]:
    for col_offset in [-1, 1]:
      current_row, current_col = rook_row + row_offset, rook_col + col_offset
      while 0 <= current_row < 8 and 0 <= current_col < 8:
        piece_at_current = rook_board[current_row][current_col]
        if piece_at_current != ".":  # Encountered a piece (including the king)
          if piece_at_current == "X":  # Check if it's the king
            return True
          break  # Stop iterating in this direction
        current_row += row_offset
        current_col += col_offset

  return False

def queen_check(queen_board, queen):
  # Combine bishop and rook check logic for queen
  return bishop_check(queen_board, queen) or rook_check(queen_board, queen)

# Add functions to find piece positions (find_bishop_position, find_rook_position)

def pawn_check(pawn_board, pawn):
  pawn_row, pawn_col = find_pawn_position(pawn_board, pawn)  # Add a function to find pawn position

  # Analyze based on pawn symbol and its position
  if pawn == "P":  # White pawn
    # Check diagonally one square upwards for black king ("X")
    return (pawn_row - 1 >= 0 and 
            (pawn_board[pawn_row - 1][pawn_col - 1] == "X" or 
             pawn_board[pawn_row - 1][pawn_col + 1] == "X"))
  else:  # Black pawn
    # Check diagonally one square downwards for white pawn ("P")
    return (pawn_row + 1 <= 7 and 
            (pawn_board[pawn_row + 1][pawn_col - 1] == "P" or 
             pawn_board[pawn_row + 1][pawn_col + 1] == "P"))


