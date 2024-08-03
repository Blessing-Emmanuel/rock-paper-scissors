import random
# import cv2
# from keras.models import load_model
# import numpy as np

class Game:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.options)

    def get_user_choice(self):
        while True:
            user_choice = input("Rock, paper or scissors?: ").lower()
            if user_choice in self.options:
                return user_choice
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_winner(self, computer_choice, user_choice):
        print(f"comp:{computer_choice}, user: {user_choice}")
        if computer_choice == user_choice:
            print("It's a tie!")
        else:
            win_conditions = {
                "rock" : "scissors",
                "scissors": "paper",
                "paper" : "rock"
            }

            if win_conditions[user_choice] == computer_choice:
                self.user_score += 1
                print("You won this round")
            else:
                self.computer_score += 1
                print("Computer won this round")

    def play_three_rounds(self):
        self.user_score = 0
        self.computer_score = 0

        for x in range(3):
            computer_choice = self.get_computer_choice()
            user_choice = self.get_user_choice()
            self.get_winner(computer_choice, user_choice)
            # print("That's one rpund up")

        if self.user_score > self.computer_score:
            print("You've won!!")
        elif self.user_score < self.computer_score:
            print("The computer won")
        else:
            print("It's a tie!")

def play_game():
    game_1 = Game()

    while True:
        game_1.play_three_rounds()

        play_again = input("Would you like to play again? (y/n)").lower()
        if play_again != "y":
            break

play_game()