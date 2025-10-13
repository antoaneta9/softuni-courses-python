import random

computer_choice = random.randint(1, 100)
my_choices = []
game_on = True
while game_on:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == computer_choice:
        my_choices.append(guess)
        print("Correct!")
        game_on = False
    elif guess < computer_choice:
        my_choices.append(guess)
        print('Your guess is too low')
        continue
    elif guess > computer_choice:
        my_choices.append(guess)
        print('Your guess is too high')
        continue
    else:
        print('Enter valid input!')
        game_on = False
