import random

def get_guess():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < 1 or guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue

        return guess

def ask_play_again():
    while True:
        play_again = input("Would you like to play again? (yes/no) ").lower().strip()

        if play_again == "no" or play_again == "yes":
            return play_again
        else:
            print("Please enter yes or no.")

def play_game():
    attempts = 0
    secret_number = random.randint(1, 100)

    while True:
        guess = get_guess()
    
        print(f"You guessed: {guess}")
        attempts += 1
        remaining_attempts = max_attempts - attempts
    
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number after {attempts} attempts.")
            break
    
        if attempts >= max_attempts:
            print("Game over! You ran out of attempts.")
            print(f"The secret number was {secret_number}")    
            break
    
        print(f"The remaining attempts are: {remaining_attempts}")


max_attempts = 7

while True:
    play_game()

    play_again = ask_play_again()

    if play_again == "no":
        print("Thanks for playing my game!")
        break