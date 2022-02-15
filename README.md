# Battleships

Battleships is a Python terminal mini game which runs on Heroku. It is based on the popular board game battleships more info on the board game version can be found here.

As the game was developed in Python for use in the terminal, it utilises the Code Institute Python Template to generate a "terminal" onto the page, making it available within a web browser.

Users compete against AI to try and shoot each others battleships, The first to destroy all battleships is the winner. There are 5 types of ships to destroy they are the 
carrier (takes 5 spaces on the board), battleship (takes 4 spaces on the board), cruiser (takes 3 spaces on the board), submarine (takes 3 spaces on the board) and the destroyer (takes 2 spaces on the board).

The player places their 5 ships on the board and the computer randomly chooses where he wants to put all his ships, Then we duel.

![readme hero image]()

## How To Play

- The player enters their name and jumps straight into the action.
- The player places their 5 ships on the board.
- When all ships have been placed on the board the battle begins the player guesses the co-ordinates of the computers ships and the computer guesses where the player placed     their ships. 
- The first to destroy all ships wins the game.

## Features
## Existing Features

- The Welcome Message

    - When a new game starts the welcome message is displayed.
    - The user is met with colour coded sections and ASCII art (Battleships Logo) for clarity. 
    - Within this the different types of ship are listed, as well as the: board size, total number of hits needed to win (17) and the different styles of marker.
    - It also contains the instructions in how to play the game.
    - The player is then prompted for name input, which complies to the validation checks listed. Input is repeated until a valid name is entered.

![readme hero image]()

- The Board
    - Once name input is validated, it is then used to create the player's board, which is displayed to them in the terminal. The user is prompted to place each ship in turn from smallest to largest (2-5), the ship size is displayed to them.
    - Orientation, row and then column inputs are requested for the ship location, all having validation checks on them. Before placement of the ships on the board, overlap and fit checks are ran on the input location for the ship, which must be passed else the user is prompted for input again.
    - Once a all of the inputs are entered and valid the ship is placed on the players board, their board is then printed to them with the placed ship for reference when placing the next. Once all ships are placed the computers ships are randomly placed on their board, following the same validation checks.

![readme hero image]()

- The Guess Board
    - Once the ships have been placed on each board the game play begins.
    - The player always goes first, their guess board is printed out to them for reference when entering a row and column, which must pass validation checks if not the user is prompted to enter valid data again. Once a valid input is entered the result of their attack is printed out to them before the guess board is updated and printed out to them again. The computers guess is printed out to the user alongside the computers board of where the player hit for reference to see where there shot landed. Validation checks prevent the user repeating already guessed spots on the board.
    - The sleep method of the time library and phase/line break is used to seperate and emphasize the individual turns. There is a countdown of two seconds before the computer makes their attack and the terminal is updated this also adds more suspense.

![readme hero image]()

- Ship Display
    - Ships that haven't been hit are displayed on the player's board as the at sign "@".
    - Letters are used for the column display and numbers for the rows, this allows for easy differentiation when inputting coordinates.
    - The markers that have been used give a good level of contrast and distinction between the different markers and what they represent.  "@" to represent ships, "-" for a miss and "X" for a hit.

![readme hero image]()

- Game Play Display
    - Feedback to the user is provided constantly throught all phases of the game.
    - All sequences are broken down to increase ease of use and clarity. The boards are updated appropriately as well as the hit counter incrementing when required.
    - A consistent use of the sleep method and phase/line breaks is also used throughout to increase ease of use and clarity.

![readme hero image]()

- Play Again
    - Once all the conditions of an end game have been met, which is a player either computer or user has hit the total hit count of 17, the turn sequence is broken out off, with a win or lose message being displayed.
    - The player is them prompted to play again, input validation is used here to ensure a Y or N is entered.
    - If the user inputs with a "y" then the game is started from the beginning, else the player is told goodbye and the program ends.

![readme hero image]()

## Features left to implement
*There are no features left to implement from the initial scope of my project, however I have some features that I would like to add in the future.*

- Print the Player Board and Computer Board side by side in the terminal, rather than on top of one another.
- Make a 2 player version of the game.
- Highlight the win or lose message with more effect.

## Testing
- Due to the nature of the project, testing has been implemented throughout the entire project mainly debugging through running the program in the terminal as well as debugging using the python debugger. This is shown by commits of refactoring code.
- Sections of code where developed before implementation to make sure it worked and also where run throught the PEP8 validator.
- Tested with invalid inputs: Such as using TypeErrors and ValueErrors, string instead of integers, out of bound inputs, same input twice.
- Tested in both Gitpod terminal and CI Heroku terminal.
- Limit testing has been conducted by myself, users and peers on slack through the peer-code-review channel, there is currently no reported issues that cause the game to break.

## Validator Testing

- HTML
    - Not within project scope.

- CSS
    - Not within project scope.

- JS
    - Not within project scope.

- Python
    - No errors were found when passing through the [PEP8 Validator tool](http://pep8online.com/)

- **Lighthouse**

    - Not within project scope.

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!