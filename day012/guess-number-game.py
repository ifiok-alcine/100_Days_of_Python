from random import randint
from art import logo

chosen_number = randint(1, 100)
number_of_lives = 0
end_of_game = False


def compare_numbers(first_number, second_number):
    if first_number < second_number:
        return "Too high."
    else:
        return "Too low."


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    number_of_lives = 10
else:
    number_of_lives = 5

while not end_of_game:
    print(f"You have {number_of_lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if chosen_number == guess:
        end_of_game = True
        print(f"You got it! The answer was {chosen_number}.")
    else:
        number_of_lives -= 1
        if number_of_lives == 0:
            end_of_game = True
            print("You have run out of guess, you lose.")
        else:
            print(compare_numbers(chosen_number, guess))
            print("Guess again.")
