from random import randint


def new_game():
    print("Welcome to Ultimate Battleships\n")
    print("-" * 35)
    user_name = input("Please enter your name: \n")
    print("-" * 35)
    return user_name


def board_size(name):
    """
    Start a new game and get users name, board size and number of ships
    they want to use in the game
    """
    while True:
        try:
            size = int(input(f"{name} please select a board " +
                             "size between 5-10: \n"))
            if not (5 <= (size) <= 10):
                print("Please provide a number between 5-10, " +
                      f"you provided {size}")
                print("-" * 35)
                continue
        except ValueError:
            print("YOU MUST ENTER A NUMBER")
            print("-" * 35)
            continue
        print("-" * 35)
        return size


def number_of_ships(name):
    """
    Let user select how many ships they would like to play with between 4-8
    """
    while True:
        try:
            game_ships = int(input(f"{name} Please select how many " +
                                   "ships in the game between 4-8: \n"))
            if not (4 <= (game_ships) <= 8):
                print("Please provide a number between 4-8, " +
                      f" you provided {game_ships}")
                print("-" * 35)
                continue
        except ValueError:
            print("PLEASE ENTER A NUMBER")
            print("-" * 35)
            continue
        print("-" * 35)
        return game_ships


def create_board(size):
    """
    Create the board using the size the user selected.
    Create a list and place O for each space
    """
    return [["O" for count in range(size)] for count in range(size)]


def players_board(board, name):
    """
    Print the board using the create_board function and
    the randome_ships function.
    print the list elements in single lines with space
    """
    print(f"{name}'s Board:")
    for b in board:
        print(*b)
    return


def computers_board(board):
    print("Computers Board:")
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


def players_guess(size):
    while True:
        try:
            print("-" * 35)
            row = int(input(f"Guess a row between 1 and {size}:\n"))
            if not (1 <= (row) <= size):
                print("PLEASE ENTER A VALID ROW!")
                continue
        except ValueError:
            print("PLEASE ENTER A NUMBER")
            continue
        print("-" * 35)
        try:
            column = int(input(f"Guess a column between 1 and {size}:\n"))
            if not (1 <= int(column) <= size):
                print("PLEASE ENTER A VALID ROW!")
                continue
        except ValueError:
            print("PLEASE ENTER A NUMBER")
            continue
        print("-" * 35)
        return (row) - 1, (column) - 1


def computers_guess(size, board):
    row, column = randint(0, size - 1), randint(0, size - 1)
    while board[row][column] == "X" or board[row][column] == "-":
        row, column = randint(0, size - 1), randint(0, size - 1)
    return row, column


def game(player_board, computer_board, hidden_board, data, ships, name):
    row, column = players_guess(data)
    comp_row, comp_col = computers_guess(data, player_board)
    if hidden_board[row][column] == "X" or hidden_board[row][column] == "-":
        print("You already picked those coordinates try again")
        game(player_board, computer_board, hidden_board, data, ships, name)
    elif computer_board[row][column] == "@":
        print("YOU SUNK MY BATTLESHIP!")
        print("-" * 35)
        hidden_board[row][column] = "X"
        if count_hits(hidden_board) == ships:
            print("YOU WIN, CONGRATULATIONS")
            print("-" * 35)
            end_game()
        elif player_board[comp_row][comp_col] == "@":
            print("COMPUTER HIT YOU'RE SHIP!")
            print("-" * 35)
            player_board[comp_row][comp_col] = "X"
            if count_hits(player_board) == ships:
                print("GAME OVER YOU LOSE")
                print("-" * 35)
                end_game()
        elif player_board[comp_row][comp_col] == "O":
            player_board[comp_row][comp_col] = "-"
    elif computer_board[row][column] == "O":
        print("Sorry, you missed!")
        print("-" * 35)
        hidden_board[row][column] = "-"
        if player_board[comp_row][comp_col] == "@":
            print("COMPUTER HIT YOU'RE SHIP!")
            print("-" * 35)
            player_board[comp_row][comp_col] = "X"
            if count_hits(player_board) == ships:
                print("GAME OVER YOU LOSE")
                print("-" * 35)
                end_game()
        elif player_board[comp_row][comp_col] == "O":
            player_board[comp_row][comp_col] = "-"
    players_board(player_board, name)
    computers_board(hidden_board)
    game(player_board, computer_board, hidden_board, data, ships, name)


def count_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def end_game():
    input("Press any key to start a new game! \n")
    print("-" * 35)
    main()


def main():
    """
    Main function to run the game
    """
    name = new_game()
    data = board_size(name)
    hidden_board = create_board(data)
    player_board = create_board(data)
    computer_board = create_board(data)
    ships = number_of_ships(name)
    random_ships(data, ships, player_board)
    random_ships(data, ships, computer_board)
    print("-" * 35)
    print("LETS BEGIN!!!")
    print(f"Board size: {data}. Number of ships: {ships}")
    print("TOP LEFT CORNER IS ROW:1, COL:1")
    print("-" * 35)
    players_board(player_board, name)
    computers_board(hidden_board)
    game(player_board, computer_board, hidden_board, data, ships, name)


main()
