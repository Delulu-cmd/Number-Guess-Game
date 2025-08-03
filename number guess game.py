import random
import art
print(art.number_guess_logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
numbers = []
for number in range(2, 100):
    numbers.append(number)
actual_number = random.choice(numbers)
# print(actual_number)
if level == "easy":
    attempts = 10
else:
    attempts = 5

def number_guess(level_of_game):
    global attempts

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess > actual_number:
            print("Too high⬆️\nCheck again.")
        else:
            print("Too low!⬇️\nCheck again.")

        if user_guess == actual_number:
            return f"Voila!😘, you guessed it right, the number was {actual_number}."

        attempts -= 1

        if attempts == 0:
            return "You've run out of attempts, you lose."


print(number_guess(level))
