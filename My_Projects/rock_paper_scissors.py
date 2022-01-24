import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

print()
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit the game: ")
    if user_input.lower() == 'q':  # we convert user's output all to lower case
        break   # if the user don't want to play we skip all the while loop and only will show the print

    if user_input not in options:  # in this line if the user has entered something else, the programm will kepp asking him the same question 
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print('Computer picked ', computer_pick, '.')

    if user_input == 'rock' and computer_pick == 'scissors':
        print('You won!')
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print('You won!')
        user_wins += 1

    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You won!')
        user_wins += 1

    else:
        print('You lost!')
        computer_wins += 1

print('You won', user_wins, 'times.')
print('The computer won', computer_wins, 'times.')
print('Goodbye! :)')