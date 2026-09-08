# Number Guessing Game

## Description
This is a simple Number Guessing Game that I built with Python.

When the game starts, the program chooses a random number between 1 and 100. The player needs to guess the correct number and has a maximum of 7 attempts.

After every guess, the game tells the player if the number is too high or too low until the player guesses correctly or runs out of attempts.
## Features
* The game chooses a random number between 1 and 100.
* The player has 7 attempts to guess the correct number.
* After every guess, the game tells the player if the number is too high or too low.
* The game validates the user’s input and doesn’t accept letters or numbers outside the range.
* Invalid inputs don’t count as an attempt.
* The game shows how many attempts are left.
* After the game ends, the player can choose if they want to play again.
* The play again input also accepts different formats like YES, Yes, or extra spaces.
## What I Learned
While working on this project, I learned how to use while loops and understand better how break and continue work.

I also learned how to create functions and use return to get a value back from a function. I practiced handling invalid inputs with try and except, so the program doesn’t crash when the user enters something wrong.

Another important thing I learned was how to split my code into different functions instead of putting everything inside one big loop. This made the code much easier to understand and work with.

I also practiced using .lower() and .strip() to make user input easier to handle.
## How to Run
Make sure Python is installed on your computer.

Open the terminal inside the project folder and run:

python3 game.py
## Future Improvements
On my next update I would make harder levels such as guessing a game from 1 to 1000 or even more.
