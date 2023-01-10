from random import randint


PLAYER_GAME_SCORE = 0
COMPUTER_GAME_SCORE = 0


def user():
    """
    Gets user to add their name for the game.
    """
    print("Welcome to Ultimate Battleships\n")
    print("-" * 35)
    player_name = input("Please enter your name:\n")
    print("-" * 35)
    return player_name


def board_size(name):
    """
    Lets user select the board size for the game
    between 5 - 10.
    """
    return validate_data("Please select a board size between", 5, 10, name)


def validate_data(prompt, start, end, name):
    """
    This function validates the data passed to it from the functions
    board_size and number_ships.
    It checks if the correct input is being put in by the user and uses
    a try and except to test this.
    """
    while True:
        try:
            num = int(input(f"{name} {prompt} " +
                            f"{start}-{end}:\n"))
            if not (start <= (num) <= end):
                print(f"Please provide a number between {start}-{end}, " +
                      f"you provided {num}")
                print("-" * 35)
                continue
        except ValueError:
            print("YOU MUST ENTER A NUMBER")
            print("-" * 35)
            continue
        print("-" * 35)
        return num


def number_of_ships(name):
    """
    Let user select how many ships they would like to play
    in the game between 4 - 8.
    """
    return validate_data("Please select how many ships in the game between", +
                         4, 8, name)


def create_board(size):
    """
    This is the data model for the game.
    Creates a list and place O for each space in range of the user's
    selected board size.
    O represents water!
    It creates the board by storing the data using the size the user selected.
    Eventually it will store the player, computer and hidden board, along with
    all the ships, hits and misses.
    """
    return [["O" for count in range(size)] for count in range(size)]


def players_board(board, name):
    """
    Use's the create board function as the board argument.
    Get's the users name from the user function.
    Print's the board using a for loop through the list,
    and use * for a space between each O.
    """
    print(f"{name}'s Board:")
    for b in board:
        print(*b)


def computers_board(board):
    """
    Use's the create board function as the board argument.
    Print's computers board so the user knows which board it is.
    Loop through the board list and print with a space,
    in between the O using *.
    """
    print("Computers Board:")
    for b in board:
        print(*b)


def random_ships(size, ships, board):
    """
    Three aguements for the board size, amount of ships and
    the board it's self.
    '@' means ship
    Loop through the range of ships, so we know how many ships,
    to place on the board.
    Use randint to create a random row and column for the ship,
    to be placed on.
    Use a while loop to check that the coordinates,
    have not already been used before and if so add another random ship.
    """
    for ship in range(ships):
        ship_row, ship_column = randint(0, size - 1), randint(0, size - 1)
        while board[ship_row][ship_column] == "@":
            ship_row, ship_column = randint(0, size - 1), randint(0, size - 1)
        board[ship_row][ship_column] = "@"
    return ship


def players_guess(size, hidden):
    """
    This function allows the user to select a row and column,
    between 1 and the arguement size.
    Using a while loop with the try and except rule, it will
    contiune looping round until the user has selected the right
    numbers for their guess, no strings and checks if they have picked
    that guess before.
    """
    while True:
        try:
            print("-" * 35)
            row = int(input(f"Guess a row between 1 and {size}:\n"))
            if not (1 <= (row) <= size):
                print("PLEASE ENTER A VALID NUMBER!")
                continue
        except ValueError:
            print("PLEASE ENTER A NUMBER")
            continue
        print("-" * 35)
        try:
            column = int(input(f"Guess a column between 1 and {size}:\n"))
            if not (1 <= int(column) <= size):
                print("PLEASE ENTER A VALID NUMBER!")
                continue
        except ValueError:
            print("PLEASE ENTER A NUMBER")
            continue
        try:
            if hidden[(row) - 1][(column) - 1] == "X" or \
               hidden[(row) - 1][(column) - 1] == "-":
                print("You already picked those coordinates try again")
                continue
        except TypeError:
            print("something went wrong")
            continue
        return (row) - 1, (column) - 1


def computers_guess(size, board):
    """
    Function for computers guess, which will pick two random
    numbers between 0 and the size of the board - 1.
    The while loop checks the computer hasnt already
    picked those coordinates before and loops round if it has.
    """
    row, column = randint(0, size - 1), randint(0, size - 1)
    while board[row][column] == "X" or board[row][column] == "-":
        row, column = randint(0, size - 1), randint(0, size - 1)
    return row, column


def game(player, computer, hidden, size, ships, name):
    """
    When the game has begun this function will run.
    '-' means miss
    'X' means hit
    Intially it will allow the user to have a guess as well as the computer.
    Using the if, elif statements it will check if the user and computer
    either hit or missed a ship.
    The nested if, elif statements do further checks if a hit or miss has
    occured, until finally once all ships on one of the boards are hit
    using the count hits function, it will send you to the end game function.
    At end the end of each round the scores will be shown for both player
    and computer, and boards will be printed again.
    At the end of each round the player has the choice to quit the
    game entirely and can start with a new player.
    """
    global PLAYER_GAME_SCORE
    global COMPUTER_GAME_SCORE
    while True:
        row, column = players_guess(size, hidden)
        comp_row, comp_col = computers_guess(size, player)
        if computer[row][column] == "@":
            print("YOU SUNK MY BATTLESHIP!")
            print("-" * 35)
            hidden[row][column] = "X"
            if player[comp_row][comp_col] == "@":
                print("COMPUTER HIT YOU'RE SHIP!")
                print("-" * 35)
                player[comp_row][comp_col] = "X"
                if count_hits(hidden) == ships and count_hits(player) == ships:
                    print("GAME OVER")
                    print("WOW A DRAW")
                    print("-" * 35)
                    print(f"GAME SCORE, {name}: {PLAYER_GAME_SCORE}, " +
                          f"Computer: {COMPUTER_GAME_SCORE}")
                    print("-" * 35)
                    end_game(name, 1)
                elif count_hits(hidden) == ships:
                    PLAYER_GAME_SCORE += 1
                    print("GAME OVER")
                    print(f"YOU WIN, CONGRATULATIONS {name}!")
                    print("-" * 35)
                    print(f"GAME SCORE, {name}: {PLAYER_GAME_SCORE}, " +
                          f"Computer: {COMPUTER_GAME_SCORE}")
                    print("-" * 35)
                    end_game(name, 1)
                elif count_hits(player) == ships:
                    COMPUTER_GAME_SCORE += 1
                    print("GAME OVER")
                    print(f"You lost {name}, better luck next time")
                    print("-" * 35)
                    print(f"GAME SCORE, {name}: {PLAYER_GAME_SCORE}, " +
                          f"Computer: {COMPUTER_GAME_SCORE}")
                    print("-" * 35)
                    end_game(name, 1)
            elif count_hits(hidden) == ships:
                PLAYER_GAME_SCORE += 1
                print("GAME OVER")
                print(f"YOU WIN, CONGRATULATIONS {name}!")
                print("-" * 35)
                print(f"GAME SCORE, {name}: {PLAYER_GAME_SCORE}, " +
                      f"Computer: {COMPUTER_GAME_SCORE}")
                print("-" * 35)
                end_game(name, 1)
            elif player[comp_row][comp_col] == "O":
                player[comp_row][comp_col] = "-"
                print("Computer missed")
                print("-" * 35)
        elif computer[row][column] == "O":
            print("Sorry, you missed!")
            print("-" * 35)
            hidden[row][column] = "-"
            if player[comp_row][comp_col] == "@":
                print("COMPUTER HIT YOU'RE SHIP!")
                print("-" * 35)
                player[comp_row][comp_col] = "X"
                if count_hits(player) == ships:
                    COMPUTER_GAME_SCORE += 1
                    print("GAME OVER")
                    print(f"You lost {name}, better luck next time")
                    print("-" * 35)
                    print(f"GAME SCORE, {name}: {PLAYER_GAME_SCORE}, " +
                          f"Computer: {COMPUTER_GAME_SCORE}")
                    print("-" * 35)
                    end_game(name, 1)
            elif player[comp_row][comp_col] == "O":
                player[comp_row][comp_col] = "-"
                print("Computer missed")
                print("-" * 35)
        player_score = count_hits(hidden)
        computer_score = count_hits(player)
        print("After this round, the scores are:")
        print(f"{name}: {player_score}. Computer: {computer_score}")
        print("-" * 35)
        players_board(player, name)
        computers_board(hidden)
        end_game(name, 0)


def count_hits(board):
    """
    This function is to check how many hits are on a paticular board.
    It loops through each row and column and adds 1 to count,
    everytime it gets an X.
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def end_game(name, game_over):
    """
    End game function, will run once all ships have been sunk or at the end
    of each round.
    There are two if and elif statements which checks the input or if its
    the end of the game.
    If input is q the user can quit the game entirely and allows a new user
    to start a new game.
    The game over only happens when all ships have been sunk and the user
    can either start a new game or quit.
    """
    print("-" * 35)
    end = input("Press any key to continue or q to quit game!\n")
    if end == "q":
        print("-" * 35)
        restart()
    elif game_over == 1:
        print("-" * 35)
        main(name)


def restart():
    """
    This function is called when the user wishes to quit the game.
    It will re set everything and allow a new user to input their name.
    The game scores will be re set for next user.
    """
    global PLAYER_GAME_SCORE
    global COMPUTER_GAME_SCORE
    name = user()
    PLAYER_GAME_SCORE = 0
    COMPUTER_GAME_SCORE = 0
    main(name)


def main(name):
    """
    Main function to run the game
    """
    size = board_size(name)
    hidden = create_board(size)
    player = create_board(size)
    computer = create_board(size)
    ships = number_of_ships(name)
    random_ships(size, ships, player)
    random_ships(size, ships, computer)
    print("-" * 35)
    print("LETS BEGIN!!!")
    print(f"Board size: {size}. Number of ships: {ships}")
    print("TOP LEFT CORNER IS ROW:1, COL:1")
    print("'-': Is Miss, 'X': Is Hit, 'O': Is Water")
    print("-" * 35)
    players_board(player, name)
    computers_board(hidden)
    initialize(player, computer, hidden, size, ships, name)


def initialize(player, computer, hidden, size, ships, name):
    """
    This function is to start playing the game and allows the function
    to be taken out of the loop of the main function.
    """
    game(player, computer, hidden, size, ships, name)


restart()
