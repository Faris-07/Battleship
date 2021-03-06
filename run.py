# Libraries
import random
import time

# Player and computer board variables
PLAYER_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]

# The SHIP_LENGTHS list contains the length of each ship on the board
SHIP_LENGTHS = [2, 3, 3, 4, 5]

# The letters_conversion dictionary assigns letters to numbers that can be
# used for ship placements
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

# The PHASE variable prints "=" 80 times as a line break.
PHASE = "=" * 80


def welcome_message():
    """
    The welcome_message function displays a welcome message every new game
    """
    print("""\
    \u001b[32m
  ____        _   _   _           _     _           
 |  _ \      | | | | | |         | |   (_)          
 | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___ 
 |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ |
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                         | |        
                                         |_| 
\u001b[0m       
""")

    # Welcome Message
    print("\nWelcome To Battleships!\n")
    print("THE BOARD IS A GRID OF 8x8 WITH FIVE SHIPS TO SINK")
    print("\u001b[32mCARRIER - \u001b[33mBATTLESHIP - \
\u001b[34mCRUISER - \u001b[35mSUBMARINE - \u001b[36mDESTROYER\
    \u001b[0m")
    print("EACH PLAYER HAS 17 LIVES, \
THE FIRST TO STRIKE 17 BLOWS TO THE ENEMYS SHIPS WINS\n")
    time.sleep(5)
    print(PHASE)

    # Instructions
    print("\u001b[31mINSTRUCTIONS:\u001b[0m \n")
    print("THE FIRST PLAYER TO GET A HIT COUNT OF 17 HITS DESTROYING ALL ENEMY \
SHIPS WINS")
    print("THE AIM OF THE GAME IS TO DESTROY THE AI \
ENEMY BY DESTROYING ALL THEIR SHIPS")
    print("BEFORE THEY DESTROY YOURS. THE THING IS WELL \
BOTH OF YOU CANT SEE WHERE TO")
    print("SHOOT... BUT THAT SHOULDNT BE MUCH OF A PROBLEM.")
    print("THE RULES ARE AS FOLLOWS: \n")
    print("SHIPS: \n")
    print("\u001b[36mDESTROYER\u001b[0m - SIZE OF 2 ON THE BOARD\n")
    print("\u001b[35mSUBMARINE\u001b[0m - SIZE OF 3 ON THE BOARD\n")
    print("\u001b[34mCRUISER\u001b[0m - SIZE OF 3 ON THE BOARD\n")
    print("\u001b[33mBATTLESHIP\u001b[0m - SIZE OF 4 ON THE BOARD\n")
    print("\u001b[32mCARRIER\u001b[0m - SIZE OF 5 ON THE BOARD\n")
    # Instructions - Markers
    print("MARKERS: \n")
    print("@ IS A SHIP")
    print("- IS A MISS")
    print("X IS A HIT/SUNK SHIP")
    time.sleep(5)
    print(PHASE)


def name_input():
    """
    The name_input function takes input from the user and stores it 
    in a variable that can be used further into the program
    """
    print("WHAT SHALL YOU BE KNOWN BY CAPTAIN?")
    while True:
        player_name = input("PLEASE ENTER A NAME:\n").upper()
        if check_player_name(player_name):
            break
    print(f"\nTHE NAME YOU CHOSE IS: CAPTAIN {player_name}\n")
    print(PHASE)
    time.sleep(1)
    print(' ')
    return player_name


def check_player_name(name):
    """
    The check_player_name function checks if the players name is longer 
    than 10 or not long enough. Then it tells the player to enter a valid name
    """
    if len(name) > 10:
        print('INVALID NAME. 10 CHARACTERS MAX')
        return False
    elif len(name) == 0:
        print('INVALID NAME. NOT LONG ENOUGH')
    else:
        return True


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
    and then places the ship.
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
                                board[row][i] = "@"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "@"
                        break
            else:
                place_ship = True
                print('Place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if fit_ship_check(ship_length, row, column, orientation):
                    # check if ship overlaps
                    if ship_overlap(board, row, column, orientation,
                                    ship_length):
                        print(PHASE)
                        print("THE SHIP DOSENT FIT HERE CAPTAIN \n")
                    else:
                        print(PHASE)
                        print("EXCELLENT POSITIONING OF THE SHIP CAPTAIN \n")
                        # place ship
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "@"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "@"
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
            if board[row][i] == "@":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "@":
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
                orientation = input("Enter orientation (H or V): \n").upper()
                if orientation == "H" or orientation == "V":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid orientaion (H or V)")
        while True:
            try:
                row = input("Enter the row of the ship 1-8: \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid letter between 1-8")
        while True:
            try:
                column = input("Enter the column of the ship A-H: \n").upper()
                if column not in 'ABCDEFGH':
                    print("Please enter a valid letter between A-H")
                else:
                    column = letters_conversion[column]
                    break
            except KeyError:
                print("Please enter a valid letter between A-H")
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter the row of the ship 1-8: \n")
                if row in '12345678':
                    row = int(row) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid letter between 1-8")
        while True:
            try:
                column = input("Enter the column of the ship A-H: \n").upper()
                if column not in 'ABCDEFGH':
                    print("Please enter a valid letter between A-H")
                else:
                    column = letters_conversion[column]
                    break
            except KeyError:
                print("Please enter a valid letter between A-H")
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
        elif COMPUTER_BOARD[row][column] == "@":
            board[row][column] = "X"
            print("WE HIT THEM, GREAT SHOT CAPTAIN")
        else:
            board[row][column] = "-"
            print("WE MISSED, WE WILL GET THEM ON THE NEXT SHOT")
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "@":
            board[row][column] = "X"
            print("WE ARE HIT, FIRE BACK!")
            print("COMPUTERS BOARD \n")
        else:
            board[row][column] = "-"
            print("THE COMPUTER MISSED, PHEW...\n")
            print("COMPUTERS BOARD \n")


def start_game():
    """
    Start game function
    """
    start_key = input("PRESS P TO START GAME: \n").upper()
    while start_key != "P":
        start_key = input("PRESS P TO START GAME: \n").upper()
    print(PHASE)
    # Computer places ships
    place_ship(COMPUTER_BOARD)
    # Computer board displayed
    # print_board(COMPUTER_BOARD)
    # Player board displayed
    print_board(PLAYER_BOARD)
    # Player places ships
    place_ship(PLAYER_BOARD)

    while True:
        # Player turn
        while True:
            print(PHASE)
            print('GUESS A BATTLESHIP LOCATION CAPTAIN!\n')
            print_board(PLAYER_GUESS_BOARD)
            turn(PLAYER_GUESS_BOARD)
            time.sleep(2)
            break
        if hit_count(PLAYER_GUESS_BOARD) == 17:
            print("\u001b[32mYOU WON!\u001b[0m, BRILLIANT SHOOTING CAPTAIN")
            break
        # Computer turn
        while True:
            turn(COMPUTER_GUESS_BOARD)
            time.sleep(2)
            break
        print_board(COMPUTER_GUESS_BOARD)
        if hit_count(COMPUTER_GUESS_BOARD) == 17:
            print(
                "UNLUCKY \u001b[31mYOU LOSE\u001b[0m CAPTAIN, WE WILL GET THEM \
                NEXT TIME")
            break


def play_again():

    """
    Asks the player if they want to play again or quit
    """
    print("WOULD YOU LIKE TO PLAY AGAIN?, CAPTAIN \n")
    answer = input("ENTER Y OR N: \n").upper()
    print(' ')
    while True:
        if answer == "Y":
            print(PHASE)
            time.sleep(2)
            welcome_message()
        elif answer == "N":
            print(' ')
            print('GOODBYE!, SEE YOU SOON CAPTAIN')
            print(' ')
            print(PHASE)
            return False
            welcome_message()
        else:
            print(' ')
            print('PLEASE ENTER Y OR N')
            answer = input('ENTER Y OR N: \n').upper()


if __name__ == "__main__":
    welcome_message()
    name_input()
    start_game()
    play_again()

