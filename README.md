<h1 align="center">Battleships</h1>

View my live project [here](https://battleships-mkm-f442ab38425d.herokuapp.com/)

Battleships is a Python terminal game which run in the Code Institute mock terminal on Heroku.

Battleships is a board game in which the player tries to destroy the other players ships first.

## How to play

Battleships is a board game that uses a grid that can vary in size. 

Each player has a set amount of ships they place on their grid (ships can also vary in size and shape), hidden from the other player.

Each player takes a turn to guess a row and column to take a shot.

If they hit the other players ship they mark it as hit and vice versa.

The player to destroy all the other's ships, wins. 

### My Version

In my version, the player plays against the computer on a 5x5 grid.

Each player has 4 ships that occupy one space and are randomly placed.

The player can see their own placement of his ships marked with '@'

Whenever the player guesses, their hits will be marked with 'X' and misses with 'O' on the computers board and vice versa.

The player keeps guessing until they hit all the computers ships or vice versa.

## Features

### Existing Features
 - 5x5 board grid.
 - input for player name.
 - Randomly places ships for player and computer.
 - The computer ships are hidden from the player.
 ![image of player name input and both boards](assets/images/input-grid.png)
 - Icons to notify hits and misses as well as text.
 ![image of hit and miss icons and text saying player/computer hit/missed](assets/images/hit.png)
 ![image of hit and miss icons and text saying player/computer hit/missed](assets/images/miss.png)
 - Invalid inputs
    - Player must enter a number
    - Player must enter a number between 0-4
    - Player must not guess the same spot
 ![image of invalid inputs](assets/images/invalid.png)
 ![image of invalid inputs](assets/images/previous-guess.png)
### Future Features
 - Player and Computer scores to keep track of who is winning.
 - Various grid sizes that the player can choose from.
 - Various ship sizes and shapes
 - Choice of placement for the players ships.