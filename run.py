from random import randint


def new_game():
    """
    Start a new game and get users name, board size and number of ships
    they want to use in the game
    """
    print("Welcome to Ultimate Battleships")
    while True:
        user_name = input("Please enter your name: \n")
        print("-" * 35)
        board_size = int(input(f"{user_name} please select a board size between 5-10: \n"))
        if validate_board_size(board_size) is True:
            print("-" * 35)
            return board_size
        else:
            return False


def number_of_ships():
    """
    Let user select how many ships they would like to play with between 4-8
    """
    while True:
        number_of_ships = int(input("Please select how many ships in the game between 4-8: \n"))
        if validate_number_of_ships(number_of_ships) is True:
            print("-" * 35)
            return number_of_ships
        else:
            return False


def validate_board_size(value):
    """
    Inside the try it checks the users value is between 5 - 10
    and raises a ValueError if a string is used rather and than integer
    """
    try:
        if not (5 <= int(value) <= 10):
            raise ValueError(f"Please provide a number between 5-10, you provided {value}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def validate_number_of_ships(value):
    """
    Inside the try it checks the users value is between 4 - 8
    and raises a ValueError if a string is used rather and than integer
    """
    try:
        if not (4 <= int(value) <= 8):
            raise ValueError(f"Please provide a number between 4-8, you provided {value}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def create_board(board_size):
    """
    Create the board using the size the user selected.
    Create a list and place O for each space
    """
    return [["O" for count in range(board_size)] for count in range(board_size)]


def print_board(board):
    """
    Print the board using the create_board function and
    the randome_ships function. 
    print the list elements in single lines with space
    """
    for b in board:
        print(*b)
    return


def random_ships(size, ships, board):
    for ship in range(ships):
        ship_row, ship_column = randint(0, size - 1), randint(0, size - 1)
        while board[ship_row][ship_column] == "@":
            ship_row, ship_column = randint(0, size - 1), randint(0, size - 1)
        board[ship_row][ship_column] = "@"
    return ship


def guess(size):
    while True:
        row = input(f"Please enter a ship row between 1 and {size}:\n")
        if validate_guess_row(row, size) is True:
            print("-" * 35)
        else:
            row = input(f"Please enter a ship row between 1 and {size}:\n")
        column = input(f"Please enter a ship column between 1 and {size}:\n")
        if validate_guess_row(column, size) is True:
            print("-" * 35)
        else:
            row = input(f"Please enter a ship row between 1 and {size}:\n")
        return int(row) - 1, int(column) - 1


def validate_guess_row(value, size):
    try:
        if not (1 <= int(value) <= size):
            print("PLEASE ENTER A VALID ROW!")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def game(board, data):
    row, column = guess(data)
    if board[row][column] == "@":
        print("YOU SUNK MY BATTLESHIP")
        board[row][column] = "X"
        print_board(board)
        game(board, data)
    elif board[row][column] == "O":
        print("Sorry, you missed!")
        board[row][column] = "-"
        print_board(board)
        game(board, data)


def main():
    """
    Main function to run the game
    """
    data = new_game()
    create_board(data)
    board = create_board(data)
    ships = number_of_ships()
    random_ships(data, ships, board)
    print_board(board)
    game(board, data)
        

main()
