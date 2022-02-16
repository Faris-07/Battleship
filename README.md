# Battleships

Battleships is a Python terminal mini game which runs on Heroku. It is based on the popular board game battleships more info on the board game version can be found here.

As the game was developed in Python for use in the terminal, it utilises the Code Institute Python Template to generate a "terminal" onto the page, making it available within a web browser.

Users compete against AI to try and shoot each others battleships, The first to destroy all battleships is the winner. There are 5 types of ships to destroy they are the 
carrier (takes 5 spaces on the board), battleship (takes 4 spaces on the board), cruiser (takes 3 spaces on the board), submarine (takes 3 spaces on the board) and the destroyer (takes 2 spaces on the board).

The player places their 5 ships on the board and the computer randomly chooses where he wants to put all his ships, Then we duel.

![readme hero image](/assets/images/Battleship-home-screen.png)

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

![Welcome message](/assets/images/Battleship-home-screen.png)
![Instructions](/assets/images/battleships-instructions.png)
![Name input](/assets/images/battleship-name.png)
![Start game](/assets/images/battleship-start-game.png)

- The Board
    - Once name input is validated, it is then used to create the player's board, which is displayed to them in the terminal. The user is prompted to place each ship in turn from smallest to largest (2-5), the ship size is displayed to them.
    - Orientation, row and then column inputs are requested for the ship location, all having validation checks on them. Before placement of the ships on the board, overlap and fit checks are ran on the input location for the ship, which must be passed else the user is prompted for input again.
    - Once a all of the inputs are entered and valid the ship is placed on the players board, their board is then printed to them with the placed ship for reference when placing the next. The computers ships are randomly placed on their board before the player places their ships, following the same validation checks.

![Player board](/assets/images/player-board.png)

![Player ship](/assets/images/place-ship.png)

![Player placed all ships](/assets/images/all-ships-placed.png)

- The Guess Board
    - Once the ships have been placed on each board the game play begins.
    - The player always goes first, their guess board is printed out to them for reference when entering a row and column, which must pass validation checks if not the user is prompted to enter valid data again. Once a valid input is entered the result of their attack is printed out to them before the guess board is updated and printed out to them again. The computers guess is printed out to the user alongside the computers board of where the player hit for reference to see where there shot landed. Validation checks prevent the user repeating already guessed spots on the board.
    - The sleep method of the time library and phase/line break is used to seperate and emphasize the individual turns. There is a countdown of two seconds before the computer makes their attack and the terminal is updated this also adds more suspense.

![Guess ship](/assets/images/guess-ship.png)
![Guess again](/assets/images/guess-again.png)

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

## Data Model
- The project uses the board class as my model. The game creates four boards the first to hold the players guesses the second to display the users board and the other two are the same but for the computers board.
- The board class stores the boards size (8), how many ships are on the board, the positions of the chosen ships on the board and information such as board type (player or computer board). 
- The board class also runs functions such as the place_ship function so the player and computer can enter valid ship positions and a hit_count function to count all the hit ships on the board.


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

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Battleships Game](https://battleships-7.herokuapp.com/)

### Project Deployment

To deploy the project through Heroku I followed these steps:
- Sign up / Log in to [Heroku](https://www.heroku.com/)
- From the main Heroku Dashboard page select 'New' and then 'Create New App'
- Give the project a name - I entered Battleships and select a suitable region, then select create app. The name for the app must be unique.
- This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the settings tab.
- This next step is required for creating the app when using the CI Python Deployment Template. If you created your own program without using the CI Template, you might not need to add a config var.
- In the config vars section select the reveal config vars button. This will display the current config vars for the app, there should be nothing already there.
- In the KEY input field input PORT all in capitals, then in the VALUE field input 8000 and select the Add button to the right.
- Next select the add buildpack button below the config vars section.
- In the pop-up window select Python as your first build pack and select save changes.
- Then repeat the steps to add a node.js buildpack.
- The order of the buildpacks is important, in the list Python should be first with Node.js second. If they are not in this order, you can click and drag them to rearrange.
- Next navigate back to the deploy tab using the submenu at the top of the page.
- In the deployment method section select the GitHub - Connect to GitHub button and follow the steps prompted if any to connect your GitHub account
- In the Connect to GitHub section that appears, select the correct account, and enter the name of the repository and select search.
- Once Heroku has located the repo select connect.
- This will connect the repo to the app within Heroku. Below the Apps Connected to Heroku section will be the Automatic Deploys section.
- In this section, confirm the correct branch of the repo is selected in the drop-down box, and then click the Enable Automatic Deploys button
- This will ensure whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app. If you prefer to do this manually you can utilise the manual deployment options further down. For this project I utilised the Automatic Deployment to enable me to check changes I made to the app as I developed it.
- Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

## Bugs
- Solved Bugs
    - A bug I came across was the players error message for when placing a ship which overlaps over existing ships or dosen't fit the board was being printed when it was the computers turn to place its ships. I fixed it by using a for loop in the players turn of the place_ship function to print the message therefore no message would be printed if the computers ship overlapped or did not fit the board. 

- Remaining Bugs
    - No bugs remaining.

## Credits
- A special thanks to my mentor Okwudiri Okoro.
- When researching on how to use colour in the terminal I came across Haoyi's Programming Blog which showed me how to implement colours in the terminal the link to the blog can be found [here](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html).
- When using the time library I referenced this [article](https://careerkarma.com/blog/python-time/) about the time sleep function.
