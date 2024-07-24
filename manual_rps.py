import random

options = ['rock', 'paper', 'scissors']

def get_computer_choice():
    random_option = random.choice(options)
    return random_option

def get_user_choice():
    user_option = input("Rock, paper or scissors?: ")
    return user_option

def get_winner(computer_choice, user_choice):
    if computer_choice.lower() == user_choice.lower():
        print("It's a tie!")
    elif computer_choice.lower() == 'rock' and user_choice.lower() == 'paper':
        print("You won")
    elif computer_choice.lower() == 'rock' and user_choice.lower() == 'scissors':
        print("You've lost")
    elif computer_choice.lower() == 'paper' and user_choice.lower() == 'rock':
        print("You've lost")
    elif computer_choice.lower() == 'paper' and user_choice.lower() == 'scissors':
        print("You won")
    elif computer_choice.lower() == 'scissors' and user_choice.lower() == 'rock':
        print("You won")
    elif computer_choice.lower() == 'scissors' and user_choice.lower() == 'paper':
        print("You've lost")
    else:
        print("Invalid option. It's between rock, paper or scissors.")

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

game_1 = play()
print(game_1)