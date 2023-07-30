from random import randint

def rps():

    rand_num = randint(0, 2)
    while True:
        if rand_num == 0:
            comp = "rock"
        elif rand_num == 1:
            comp = "paper"
        else:
            comp = "scissors"

        Player = input("make your move:\n").lower()

        if Player == comp:
            print("its a tie")
            play_again = input("Do you want to play again? (y/n) \n")
            if play_again == "y":
                rand_num = randint(1, 10)
                guess = None
            else:
                print("Thanks for playing!")
                break
        elif Player == "rock":
            if comp == "paper":
                print(f"comp played {comp}\ncomp wins")
            else:
                print(f"comp played {comp}\nplayer wins")
            play_again = input("Do you want to play again? (y/n) \n")
            if play_again == "y":
                rand_num = randint(1, 10)
                guess = None
            else:
                print("Thanks for playing!")
                break
        elif Player == "paper":
            if comp == "scissors":
                print(f"comp played {comp}\ncomp wins")
            else:
                print(f"comp played {comp}\nplayer wins")
            play_again = input("Do you want to play again? (y/n) \n")
            if play_again == "y":
                rand_num = randint(1, 10)
                guess = None
            else:
                print("Thanks for playing!")
                break
        elif Player == "scissors":
            if comp == "paper":
                print(f"comp played {comp}\nplayer wins")
            else:
                print(f"comp played {comp}\ncomp wins")
                play_again = input("Do you want to play again? (y/n) \n")
                if play_again == "y":
                    rand_num = randint(1, 10)
                    guess = None
                else:
                    print("Thanks for playing!")
                    break
        else:
            print("something went wrong")

rps()
