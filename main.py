import random

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
continue_game = True
heart = 6
your_guesses = []

from hangman_art import logo
print(logo)

for _ in range(word_length):
    display += "_"

while continue_game:
    guess = input("Guess a letter: ").lower()
    your_guesses += guess
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter



    if guess not in display:
        heart += -1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if guess in your_guesses:
        print(f"You've already guessed {guess}")
    print(f"{' '.join(display)}")
    from hangman_art import stages
    print(stages[heart])

    if heart == 0:
        continue_game = False
        print("You lose")

    if "_" not in display:
        continue_game = False
        print("You win!")




