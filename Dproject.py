import random

# Generate a random target number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess_input = input("Enter your guess: ")
    
    # Make sure the user entered a valid number
    if not guess_input.isdigit():
        print("Please enter a valid whole number.")
        continue
    
    guess = int(guess_input)
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break