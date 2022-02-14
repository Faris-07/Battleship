# Libraries
import random
import time

PLAYER_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]

SHIP_LENGTHS = [2, 3, 3, 4, 5]

letters_conversion = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


def welcome_message():
    """
    The welcome_message function displays a welcome message every new game
    """
    print("\nWelcome To Battleships!\n")
    print("THE BOARD IS A GRID OF 8x8 WITH FIVE SHIPS TO SINK")
    print("CARRIER - BATTLESHIP - CRUISER - SUBMARINE - DESTROYER")
    print("EACH PLAYER HAS 17 LIVES, THEY LOSE 1 PER HIT\n")


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


def place_ship(board):
    """
    The place ship function loops throught the lengths of the ships and then
    loops until the ship fits and dosent overlap any other ships on the board
    """
    #  loop through length of ships
    for ship_length in SHIP_LENGTHS:
        #  loop until ship fits and doesn't overlap
        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["H", "V"]), \
                    random.randint(0, 7), random.randint(0, 7)
                if fit_ship_check(ship_length, row, column, orientation):
                    #  check if ship overlaps
                    if not ship_overlap(board, row, column, orientation,
                                        ship_length):
                        #  place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ship == True
                print('Place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if fit_ship_check(ship_length, row, column, orientation):
                    # check if ship overlaps
                    if not ship_overlap(board, row, column, orientation,
                                        ship_length):
                        # place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                            print_board(PLAYER_BOARD)
                            break


def fit_ship_check(SHIP_LENGTH, row, column, orientation):
    """
    The fit_ship_check checks if the ships inputted fit on the board
    """
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True


def ship_overlap(board, row, column, orientation, ship_length):
    """
    The ship_overlap function checks if inputted ships overlap any existing
    ships already on the board
    """
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False


def user_input(place_ship):
    """
    The user_input function takes input from the user to enter where they want
    to place their ships as well as guessing the computers ships on the board
    """
    if place_ship == True:
        while True:
            try:
                orientation = input("Enter orientation (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('Enter a valid orientation H or V')
        while True:
            try:
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = letters_conversion[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Enter a valid letter between 1-8')
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in 'ABCDEFGH':
                    column = letters_conversion[column]
                    break
            except KeyError:
                print('Enter a valid letter between A-H')
        return row, column


def hit_count(board):
    """
    The hit_count function counts the number of hits each board (Player,
    Computer) has taken
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def turn(board):
    """
    The turn function goes through the users and computers turns
    """
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"


def start_game():
    """
    Start game function
    """
    start_key = input("press P to start Game").upper()
    while start_key != "P":
        start_key = input("press P to start Game").upper()
    # Computer places ships
    place_ship(COMPUTER_BOARD)
    # Computer board displayed
    print_board(COMPUTER_BOARD)
    # Player board displayed
    print_board(PLAYER_BOARD)
    # Player places ships
    place_ship(PLAYER_BOARD)

    while True:
        # Player turn
        while True:
            print('Guess a battleship location')
            print_board(PLAYER_GUESS_BOARD)
            turn(PLAYER_GUESS_BOARD)
            time.sleep(2)
            break
        if hit_count(PLAYER_GUESS_BOARD) == 17:
            print("You win!")
            break
        # Computer turn
        while True:
            turn(COMPUTER_GUESS_BOARD)
            time.sleep(2)
            break
        print_board(COMPUTER_GUESS_BOARD)
        if hit_count(COMPUTER_GUESS_BOARD) == 17:
            print("Sorry, the computer won.")
            break


if __name__ == "__main__":
    welcome_message()
    start_game()
