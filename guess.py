from random import randint
import time


def guessing_game():
    rand_num = randint(1, 10)
    tries = 3
    while True:
        try:
        
            guess = input("guess a number between 1 and 10:\n")
            guess = int(guess)
    
            if guess == rand_num:
                print("you win")
                play_again = input("Do you want to play again? (y/n) ")
                if play_again == "y":
                    rand_num = randint(1, 10)
                    guess = ""
                    guess = int(guess)
                else:
                    print("thanks for playing")
                    sleep(1.5)
                    break
                
            if guess < rand_num or guess > rand_num or guess == rand_num:
                tries = tries - 1
                if tries == 2:
                    print("2 tries left")
                elif tries == 1:
                    print("1 try left")
                else:
                    print("you lose")
                    sleep(1.5)
                    break
            if guess < rand_num:
                print("too low, try again")
            elif guess > rand_num:
                print("too high, try again")
            else:
                print("good job, you guessed correctly")
                play_again = input("Do you want to play again? (y/n) ")
                if play_again == "y":
                    rand_num = randint(1, 10)
                    guess = None
                else:
                    print("thanks for playing")
                    sleep(1.5)
                    break
                
        except (ValueError):
            print("Select a number")

name = input("Welcome enter your name\n")
ans = input(f"Would you like to play a game {name}? y/n:")
if ans == "y":
    guessing_game()
else:
    print("Goodbye")
