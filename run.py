def new_game():
    """
    Start a new game and get users name, board size and number of ships
    they want to use in the game
    """
    while True:
        print("Welcome to Ultimate Battleships")

        user_name = input("Please enter your name: \n")
        print("-" * 35)
        board_size = input(f"{user_name} please select a board size between 5-10: \n")
        print("-" * 35)
        number_of_ships = input(f"{user_name} please select how many ships in the game between 4-8: \n")
        print("-" * 35)
        print(user_name, board_size, number_of_ships)

        return 


new_game()
print(new_game())

