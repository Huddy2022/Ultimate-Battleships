def new_game():
    """
    Start a new game and get users name, board size and number of ships
    they want to use in the game
    """
    while True:
        print("Welcome to Ultimate Battleships")

        user_name = input("Please enter your name: \n")
        print("-" * 35)

        return user_name


def board_size(user_name):
    board_size = input(f"{user_name} please select a board size between 5-10: \n")
    print("-" * 35)

    return board_size


def number_of_ships(user_name):
    number_of_ships = input(f"{user_name} please select how many ships in the game between 4-8: \n")
    print("-" * 35)

    return number_of_ships()

print(new_game())
print(board_size(user_name))
print(number_of_ships(user_name))
