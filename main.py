import random

print("Welcome to my  number guessing game!", end="\n----------------------------------\n")
is_running = True
guess_count = 0
number = random.randint(0, 100)
print("I'm thinking of a number between 0 and 100. Can you guess how many tries it will take you to guess it?")

while is_running:
    try:
        guess = int(input("Enter your guess: "))
        if number == guess:
            guess_count += 1
            print(f"Congratulations! You guessed the number in {guess_count} tries.")
            break
        elif number > guess:
            print("Im thinking more higher")
        else:
            print("Im thinking more lower")
        guess_count += 1
    except ValueError:
        print("Please enter a valid number.")
        continue
    
print("Thanks for playing!")