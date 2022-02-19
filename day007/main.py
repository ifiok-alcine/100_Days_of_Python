from random import choice
from hangman_art import logo, stages
from hangman_words import word_list

correct_word = choice(word_list)
word_length = len(correct_word)
end_of_game = False
lives = 6

print(logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = correct_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in correct_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])