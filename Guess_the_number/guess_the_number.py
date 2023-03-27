import random


def guess_the_number(x):
    print(f"Welcome in my guess a number game.\
 It is about to guess the number between 1 and {x}.")
    number = random.randint(1, x)
    guess = 0
    while number != guess:
        guess = int(input("Select a number: "))
        if number > guess:
            print("Your number is too small, Try again!")

        elif number < guess:
            print("Your number is too big, Try again!")

    else:
        print("Correct! It is: ", number)


# guess_the_number(1000)


def computer_guess(x):
    print(f"""
           Welcome to my game, where computer is going to guess your secret number. 
                   Please Select your secret number between 1 - {x}
           """)
    low = 1
    high = x
    feedback = input("are you ready? ")
    while feedback.capitalize() != "C":
        guess = random.randint(low, high)

        print(f"\nIs your number {guess}?\n")

        feedback = input(
            'My number is... Select:(C)- for Correct / (H)- for Higher / (L)- for Lower: ')
        if feedback.capitalize() == "L":
            high = guess - 1
        elif feedback.capitalize() == "H":
            low = guess + 1

    print(f"Yay! Your number is {guess}")


computer_guess(100)
