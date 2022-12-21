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


print(new_game())
