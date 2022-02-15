# Battleships

Battleships is a Python terminal mini game which runs on Heroku. It is based on the popular board game battleships more info on the baord game version can be found here.

Users compete against AI to try and shoot each others battleships, The first to destroy all battleships is the winner. There are 5 types of ships to destroy they are the 
carrier (takes 5 spaces on the board), battleship (takes 4 spaces on the board), cruiser (takes 3 spaces on the board), submarine (takes 3 spaces on the board) and the destroyer (takes 2 spaces on the board).

The player places their 5 ships on the board and the computer randomly chooses where he wants to put all his ships, Then we duel.

![readme hero image]()

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

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