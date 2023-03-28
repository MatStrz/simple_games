from words import words
import random
import string


def get_valid_word(list):
    word = random.choice(list)
    while '-' in word or ' ' in word:
        word = random.choice(list)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # Getting user leter
    while len(word_letters) > 0:
        
        print('\nYou have used this letters: ', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '_' for letter in  word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('Sorry you already used that character, please try again :)')

        else:
            print('Sorry wrong character :(, please try again')
    
    print("Congratulations the word is: ", word)


hangman()
