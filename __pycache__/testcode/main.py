from checkmate import check_or_checkmate

def main():
    board_size = 8
    king_pos = (3, 3)
    pieces = {
        "Queen": (5, 3),
        "Bishop": (2, 5),
        "Rook": (1, 3),
        "Pawn": (3, 2)
    }
    
    result = check_or_checkmate(board_size, king_pos, pieces, board_size)
    print(result)

if __name__ == "__main__":
    main()
