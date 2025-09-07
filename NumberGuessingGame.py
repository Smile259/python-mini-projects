import random

print("Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 10.Can you guess it?")

num = random.randint(1,10)

guess = None

while guess != num:
    guess = int(input("Enter your guess: "))

    if guess < num:
        print("Your guess is too low! Try again")
    elif guess > num:
        print("Your guess is too high! Try again")
    else:
        print("Correct! You guessed the number!")

print("Thanks for playing")