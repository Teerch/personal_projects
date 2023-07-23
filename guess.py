from random import randint
import time


rand_num = randint(1, 10)
guess = None

while True:
    try:       
        guess = input("pick a number between 1 and 10\n")
        guess = int(guess)
        if guess < rand_num:
            print("too low")
        elif guess > rand_num:
            print("too high")
        else:
            print("you won")
            play_again = input("Do you want to play again? (y/n) \n")
            if play_again == "y":
                rand_num = randint(1, 10)
                guess = None
            else:
                print("Thanks for playing!")
                time.sleep(1.5)
                break
    except (ValueError):
        print("Select a number")