# Number Guessing Game

## Overview
The **Number Guessing Game** is a simple Python console application where players try to guess a randomly generated number between 0 and 100. The program provides hints to help the player narrow down their guesses and tracks the number of attempts taken to guess the correct number.

## Features
- Random number generation in the range 0 to 100.
- Input validation to handle non-numeric entries.
- Feedback on whether the guess is too high or too low.
- Keeps track of the number of attempts.
- Option to replay the game after each round.

## How to Play
1. Run the script in a Python environment.
2. The program will generate a random number between 0 and 100.
3. The player is prompted to guess the number:
   - If the guess is too low, the program will prompt: `I'm thinking more higher`.
   - If the guess is too high, the program will prompt: `I'm thinking more lower`.
4. When the correct number is guessed, the program will display the total number of attempts.
5. After guessing the correct number, the player can choose to play again or exit the game.

## Prerequisites
- Python 3.x installed on your system.

## How to Run
1. Copy the Python code into a `.py` file (e.g., `number_guessing_game.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `.py` file.
4. Run the script using the command:
   ```bash
   python number_guessing_game.py
   ```

## Example Gameplay
```
Welcome to my number guessing game!
----------------------------------
I'm thinking of a number between 0 and 100. Can you guess how many tries it will take you to guess it?
Enter your guess: 50
I'm thinking more higher
Enter your guess: 75
I'm thinking more lower
Enter your guess: 65
Congratulations! You guessed the number in 3 tries.
Do you want to play again? (y/n): n
Thanks for playing!
```

## Customization
- **Range of Numbers**: Modify the `random.randint(0, 100)` line to adjust the range.
- **Exit Condition**: Customize the `Do you want to play again?` prompt to suit your needs.

## Acknowledgments
- This project was created to practice Python programming and basic game logic.