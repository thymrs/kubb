def is_valid_position(x, y, size):
    return 0 <= x < size and 0 <= y < size

def check_by_king(king_pos, piece_pos):
    king_x, king_y = king_pos
    piece_x, piece_y = piece_pos
    return max(abs(king_x - piece_x), abs(king_y - piece_y)) == 1

def can_piece_check_king(king_pos, piece_pos, piece_type, board_size):
    directions = {
        "Queen": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)],
        "Rook": [(1, 0), (-1, 0), (0, 1), (0, -1)],
        "Bishop": [(1, 1), (-1, -1), (1, -1), (-1, 1)],
        "Pawn": [(1, 0), (-1, 0)]  # Assuming pawns can move both directions for simplicity
    }
    for dx, dy in directions[piece_type]:
        x, y = piece_pos
        while is_valid_position(x + dx, y + dy, board_size):
            x, y = x + dx, y + dy
            if (x, y) == king_pos:
                return True
    return False

def check_or_checkmate(board, king_pos, pieces, board_size):
    for piece_type, piece_pos in pieces.items():
        if check_by_king(king_pos, piece_pos):
            return "Success"
        elif can_piece_check_king(king_pos, piece_pos, piece_type, board_size):
            return "Success"
    return "Fail"
