def new_game():
    """
    Start a new game and get users name, board size and number of ships
    they want to use in the game
    """
    while True:
        user_name = input("Please enter your name: \n")
        print("-" * 35)
        board_size = input(f"{user_name} please select a board size between 5 - 10: \n")
        if validate_board_size(board_size) is True:
            print("-" * 35)
        else:
            return False
        number_of_ships = input(f"{user_name} please select how many ships in the game between 4-8: \n")
        if validate_number_of_ships(number_of_ships) is True:
            print("-" * 35)
        else:
            return False
        print(user_name, board_size, number_of_ships)

        return 


def validate_board_size(value):
    try:
        if not (5 <= int(value) <= 10):
            raise ValueError(f"Please provide a number between 5-10, you provided {value}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def validate_number_of_ships(value):
    try:
        if not(4 <= int(value) <= 8):
            raise ValueError(f"Please provide a number between 4-8, you provided {value}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

print("Welcome to Ultimate Battleships")
new_game()

