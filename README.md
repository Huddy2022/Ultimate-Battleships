# ULTIMATE BATTLESHIPS

Ultimate Battleships is a python terminal game, which runs in the code insitute mock terminal of Heroku.

The user gets to add their name, the board size and how many ships to play with. Once the game runs the user is up against a computer and whoever sinks all the battleships first wins. The user can play as many times as they like, a a game score for the user and computer will be logged, until the user quits which will re set everything and allow a new user to start.

The Live link can be found here -

## How to play

Battleships is a classic game where you guess coordinates and if your right hit a ship on the board, until all ships are gone.

In this version, the user will add their name, choose a board size between 5-10. Choose how many ships to be place on the board between 4-8 and will be up against a computer.

The player and the computer will have a go each round.

'@' displays on the players board to show where their ships are.
'O' means water
'-' means miss
'X' means Hit

The user will have a guess bettween 1 and the size of the board for row and column.

Once all ships have been destoryed on either the players board or the computers board the game is over and the user can decide if they want another game or to quit. 

## Features

- User can input their name.
- They can decided how big the board is each game, between 5-10.
- They can also decide how many ships on each game, between 4-8.
- The player cannot see where the computer ships are but can see their own ships.

![Input]()

- Input validation and error checking
 - Must enter a number for board size and number of ships.
 - Cannot enter numbers outside the recommended range.

![input_validator]()

- Play against a computer.
- logs if you miss or hit as well as the computer.
- Accepts user input.
- Maintains scores during the game.
- Maintains a overall game score, if user decides to have multiple games.

![scores]()

- Input validation and error checking
 - Cannot enter coordinates outside the size of the board
 - You must enter numbers
 - Cannot enter the same guess twice

![scores_validator]()

## Future features

- Allow player to position ships themselves.
- Have ships larger than 1 x 1.

## Data model

- The create_board function, is where the data is contained of the board size, number of ships and name.
- It is passed to either the players_board or the computers_board which holds the data for the game to run.

