"""Hangman"""
import random
import hangman_words
from hangman_art import stages, logo

print(logo[0])
chosen_word = random.choice(hangman_words.words_list)
#Testing code
print(f'Pssst, the solution is: {chosen_word}')
end_of_game = False
display = []
word_lenght = len(chosen_word)
# Set 'lives' to equal 6.
lives = 6
for _ in range(len(chosen_word)):
    display += '_'
while end_of_game is False:
    guess = input('Guess a letter: ').lower()
    # Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #print(display)
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print('You lose!')
    #Join all the elements in the list turn it into a String.
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('You win!')
