from words import words
import random
import string


def get_valid_word(list):
    word = random.choice(list)
    while '-' in word or ' ' in word:
        word = random.choice(list)
    return word.upper()


def printToy(num):
    if num == 6:
        print('''													  \n'''
              '''					        _________________			      \n'''
              '''					        |			      \n'''
              '''					        |			      \n''')
    elif num == 5:
        print('''													  \n'''
              '''					        _________________			      \n'''
              '''					        |			      \n'''
              '''					        |			      \n'''
              '''					_________________			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|_______________|			      \n''')
    elif num == 4:
        print('''													  \n'''
              '''					        _________________			      \n'''
              '''					        |			      \n'''
              '''					        |			      \n'''
              '''					_________________			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|_______________|			      \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n''')
    elif num == 3:
        print('''													  \n'''
              '''					        _________________			      \n'''
              '''					        |			      \n'''
              '''					        |			      \n'''
              '''					_________________			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|_______________|			      \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''				    |___________|             \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n''')
    elif num == 2:
        print('''													  \n'''
              '''					        _________________			      \n'''
              '''					        |			      \n'''
              '''					        |			      \n'''
              '''					_________________			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|_______________|			      \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''				    |___________|___________|             \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n''')
    elif num == 1:
        print('''													  \n'''
              '''					        _________________			      \n'''
              '''					        |			      \n'''
              '''					        |			      \n'''
              '''					_________________			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|_______________|			      \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''				    |___________|___________|             \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					       | |                         \n'''
              '''					      |                            \n'''
              '''					    |                          \n'''
              '''					   |                             \n'''
              '''					   |                             \n'''
              '''					   |                             \n'''
              '''					   |                             \n'''
              '''					   |                             \n'''
              '''					   |                             \n'''
              '''					___|                             \n'''
              '''	                                                  \n''')
    elif num == 0:
        print('''													  \n'''
              '''					        _________________			      \n'''
              '''					        |			      \n'''
              '''					        |			      \n'''
              '''					_________________			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|               |			      \n'''
              '''					|_______________|			      \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''				    |___________|___________|             \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					        |                         \n'''
              '''					       | |                         \n'''
              '''					      |   |                         \n'''
              '''					    |       |                         \n'''
              '''					   |         |                         \n'''
              '''					   |         |                         \n'''
              '''					   |         |                         \n'''
              '''					   |         |                         \n'''
              '''					   |         |                         \n'''
              '''					   |         |                         \n''')


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    # Getting user letter
    while len(word_letters) > 0 and lives > 0:

        printToy(lives)

        print('\nYou have', lives,
              'lives and you have used this letters: ', ' '.join(used_letters))

        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print("Letter is not in the word")

        elif user_letter in used_letters:
            print('Sorry you already used that character, please try again :)')

        else:
            print('Sorry wrong character :(, please try again')

    if lives == 0:
        printToy(lives)
        print('You died, sorry. The word was: ', word)
    else:
        print("Congratulations the word is: ", word)


hangman()
