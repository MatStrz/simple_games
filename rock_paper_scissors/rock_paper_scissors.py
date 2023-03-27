import random


def play():
    player = input(
        "Please select: 'r' - for Rock, 'p' - for Paper, 's' - for Scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return 'it\'s a tie'

    if is_win(player, computer):
        return "You Won"

    return "You Lose"


def is_win(player, oponent):
    if (player == 'r' and oponent == 's') or (player == 's' and oponent == 'p')\
            or (player == 'p' and oponent == 'r'):
        return True



play_again = ""

while play_again.capitalize() != 'N':
    print(play())
    play_again = input("Do you want to play again? (N)- for 'No', any key for 'Yes' ")
    