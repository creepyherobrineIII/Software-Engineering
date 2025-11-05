#Number Guessing game
import random

lowest_bound = 1
highest_bound = 300

answer = random.randint(lowest_bound, highest_bound)

guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number betwwen {lowest_bound} and {highest_bound}")
print("============================================")



while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_bound or guess > highest_bound:
            print("Your guess is not within the range")
            print(f"Please select a number betwwen {lowest_bound} and {highest_bound}")
        elif guess < answer:
            print("Too low! Try again")
            print(f"Please select a number betwwen {lowest_bound} and {highest_bound}")
        elif guess > answer:
            print("Too high! Try again")
            print(f"Please select a number betwwen {lowest_bound} and {highest_bound}")
        elif guess == answer:
            print(f"Correct! The answer was {answer}")
            print(f"You had {guesses} guess(es)")
            is_running = False
    else:
        print("Invalid input. Not a number")
        print(f"Please select a number betwwen {lowest_bound} and {highest_bound}")