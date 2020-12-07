import random
import sources_1.hangman.hangman_art as ha
import sources_1.hangman.hangman_words as hw


random_word : str = random.choice(hw.word_list)
print(f'the random word is: {random_word}')
len_of_letter = len(random_word)
hangman_list = ['_' for _ in range(len_of_letter)]

lives = 6

while '_' in hangman_list:
    letter = input('Enter a letter: ').lower()
    if letter not in random_word:

        lives -= 1
        print(ha.stages[lives])
        # print(lives)
    position = 0
    for l in random_word:
        if letter == l:
            hangman_list[position] = l
        position += 1
    print(hangman_list)
    if lives == 0:
        print("you lose!")
        break

if lives > 0:
    print("you win!")


