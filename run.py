PLAYER_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]  
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]


def print_board(board):
    """
    The print_board function prints out the battleship board
    """
    print("  A B C D E F G H")
    print("  ---------------")     
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
