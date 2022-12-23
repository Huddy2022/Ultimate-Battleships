import random


def new_game():
    """
    Start a new game and get users name, board size and number of ships
    they want to use in the game
    """
    print("Welcome to Ultimate Battleships")
    while True:
        user_name = input("Please enter your name: \n")
        print("-" * 35)
        board_size = input(f"{user_name} please select a board size between 5-10: \n")
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
        number_of_ships = input("Please select how many ships in the game between 4-8: \n")
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
    return [["O" for count in range(int(board_size))] for count in range(int(board_size))]


def print_board(board):
    """
    Print the board using the create_board function and 
    print the list elements in single lines with space
    """
    for b in board:
        print(*b)


def add_ships(ships):


def main():
    """
    Main function to run the game
    """
    data = new_game()
    create_board(data)
    board = create_board(data)
    ships = number_of_ships()
    add_ships(ships)
    print_board(board)


main()
