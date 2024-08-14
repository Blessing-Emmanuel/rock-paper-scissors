import random
import cv2
from tensorflow.keras.models import load_model
import numpy as np
import time


model = load_model('keras_model.h5')

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

    def get_prediction(self):
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        flag = False

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window

            if cv2.waitKey(1) & 0xFF == ord('g'):
                flag = True
                start = time.time()

            if flag:
                end = 5 - (time.time() - start)
                current_score = f"You: {self.user_score}, Computer: {self.computer_score}"
                cv2.putText(frame, str(int(end)), (350,238), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3, cv2.LINE_4)
                cv2.putText(frame, current_score, (31,445), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3, cv2.LINE_4)
                cv2.imshow('frame', frame)
                if end <= 0:
                    print(prediction)
                    if prediction[0][0] > 0.5:
                        user_choice ="rock"
                    elif prediction[0][1] > 0.5:
                        user_choice ="paper"
                    elif prediction[0][2] > 0.5:
                        user_choice = "scissors"
                    elif prediction[0][3] > 0.5:
                        flag = False
                        continue
                    break
            else:
                continue 

        cap.release() # After loop release cap object
        cv2.destroyAllWindows()
        return user_choice


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
            user_choice = self.get_prediction()
            self.get_winner(computer_choice, user_choice)

        if self.user_score > self.computer_score:
            print("You've won!!")
        elif self.user_score < self.computer_score:
            print("The computer won")
        else:
            print("It's a tie!")

def play_game():
    game = Game()

    while True:
        game.play_three_rounds()
        play_again = input("Would you like to play again? (y/n)").lower()
        if play_again != "y":
            break

play_game()