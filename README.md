# ULTIMATE BATTLESHIPS

Ultimate Battleships is a python terminal game, which runs in the code institute mock terminal of Heroku.

The user gets to add their name, the board size and how many ships to play with. Once the game runs the user is up against a computer and whoever sinks all the battleships first wins. The user can play as many times as they like, a game score for the user and computer will be logged, until the user quits which will reset everything and allow a new user to start.

The Live link can be found here - https://ultimate-battleships.herokuapp.com/

![am-i-responsive](https://github.com/Huddy2022/Ultimate-Battleships/blob/main/assets/images/am-i-responsive.png)

## How to play

Battleships is a classic game where you guess coordinates and if your right hit a ship on the board, until all ships are gone.

In this version, the user will add their name, choose a board size between 5-10. Choose how many ships to be place on the board between 4-8 and will be up against a computer.

The player and the computer will have a go each round.

'@' displays on the players board to show where their ships are.
'O' means water
'-' means miss
'X' means Hit

The user will have a guess between 1 and the size of the board for row and column.

Once all ships have been destroyed on either the players board or the computers board the game is over and the user can decide if they want another game or to quit. 

## Features

- User can input their name.
- They can decided how big the board is each game, between 5-10.
- They can also decide how many ships on each game, between 4-8.
- The player cannot see where the computer ships are but can see their own ships.

![Input](https://github.com/Huddy2022/Ultimate-Battleships/blob/main/assets/images/Input.png)

- Input validation and error checking
 - Must enter a number for board size and number of ships.
 - Cannot enter numbers outside the recommended range.

![input_validator](https://github.com/Huddy2022/Ultimate-Battleships/blob/main/assets/images/Input-Validator.png)

- Play against a computer.
- logs if you miss or hit as well as the computer.
- Accepts user input.
- Maintains scores during the game.
- Maintains an overall game score, if user decides to have multiple games.

![scores](https://github.com/Huddy2022/Ultimate-Battleships/blob/main/assets/images/scores.png)

- Input validation and error checking
 - Cannot enter coordinates outside the size of the board
 - You must enter numbers
 - Cannot enter the same guess twice

![guess_validator](https://github.com/Huddy2022/Ultimate-Battleships/blob/main/assets/images/guess-validator.png)

## Future features

- Allow player to position ships themselves.
- Have ships larger than 1 x 1.

## Data model

- There are two functions which hold the data.
- The create_board function, is where the data is contained of the board size, number of ships and name.
- It is passed to either the players_board or the computers_board which holds the data for the game to run.

## Testing

I have manually tested this project by doing the following:
 - Passed the code through the CI python linter and confirmed there are no problems
 - Given invalid inputs: strings where integers are needed, out of bound inputs and same input twice for the following: board size, number of ships and player guess.
 - I have personally checked all the different sizes of boards and different number of ships on them to make sure the correct board size and number of ships have been placed correctly.
 - I have checked for each outcome of the game to see if the correct output arrives, if you win, lose or draw.
 - I have checked if you have multiple games that the game score correctly applies each time.
 - I have checked if you quit a game whether it’s the first game or an additional game that it restarts the score board and allows for a new user.
 - Tested in my local terminal and the Heroku terminal.

 ## Bugs

Solved Bugs:
 - I wanted to create a score board for each game once the game has finished if the user wanted to try multiple games. At first I created local variables in the game function, but they wouldn’t pass on to the next game. Eventually I used a global variable instead which can carry on the player and computer scores until someone restarts the overall game.
 - Initially I created a new game function which housed the inputs for the user name, board size and number of ships. Realized I couldn’t return the values I needed properly. So I created three functions instead for each one. I also had a try and except in the board size and number of ships, but decided to simplify the code by adding one more function to validate the data of these two functions and still pass the correct values back.
 - The random ships function I tried with various different methods until I found the for and while loop that is currently used. Also, even with the method I have now I didn’t understand why the coordinates where coming out wrong on the board until I realized the lists where zero indexed and added a - 1.
 - In the player guess function I couldn’t understand why it wasn’t checking the board if the same coordinates were being place and I originally had it working as an extra function in the game function. However, I realised it was zero indexing again and I added - 1, so it validated the guess correctly.
 - In the game function, there are a few if and elif statements to check both the player, computer and the hidden boards, but I struggled to figure out why count hits functions wasn’t checking when it was a draw. I realized the I placed the count hits function in the wrong area as the game was running.
 - Originally I created two functions to quit the game if a user wanted to quit completely and an end game when the original game was finished and a new one starting. I combined the two functions to simplify the code.

 ## Remaining Bugs

 - No bugs remaining.

 ## Validator testing
 
 - PEP8
  - No errors were returned from the pep8ci.herokuapp.com

![PEP8](https://github.com/Huddy2022/Ultimate-Battleships/blob/main/assets/images/CI_python_linter.png)

## Deployment

This project was deployed using the Code institutes mock terminal from Heroku.

 - Steps for deployment:
  - Clone this repository 
  - Create a new Heroku app
  - Set config vars key PORT and value 8000
  - Set the build packs to Python and NodeJS in that order
  - Link the Heroku app to the repository 
  - Click on deploy

## Credits

- Code institute for the deployment terminal 
- Love sandwiches from the code institute helped me with the validator try and except methods.
- This site help me with the code for the create board and print board functions https://bigmonty12.github.io/battleship
- This site helped me with the code for the random ships function and count hits function https://copyassignment.com/battleship-game-code-in-python/


