import random
import string
import time


def hangman():

    word = random.choice(["superman", "batman", "wonderwoman", "flash",
                         "aquaman", "greenlantern", "martianmanhunter", "cyborg"])

    if word == "superman":
        print("hope of humanity")
    elif word == "batman":
        print("billonaire playboy and philantropist")
    elif word == "wonderwoman":
        print("demigod")
    elif word == "flash":
        print("fastest man alive")
    elif word == "aquaman":
        print("he controls 70% the earth")
    elif word == "greenlantern":
        print("this is his sector to protect")
    elif word == "martianmanhunter":
        print("the man from mars")
    else:
        print("half human half machine")

    letters = string.ascii_letters
    turns = 10
    guesses = ""

    while len(word) > 0:
        answer = ""

        for letter in word:
            if letter in guesses:
                answer = answer + letter
            else:
                answer = answer + "_" + " "
        if answer == word:
            print(answer)
            print("you win!")
            play_again = input("Do you want to play again? (y/n) \n")
            if play_again == "y":
                word = random.choice(["superman", "batman", "wonderwoman", "flash",
                                      "aquaman", "greenlantern", "martianmanhunter", "cyborg"])
                guesses = ""
                turns = 10
                answer = ""

                if word == "superman":
                    print("hope of humanity")
                elif word == "batman":
                    print("billonaire playboy and philantropist")
                elif word == "wonderwoman":
                    print("demigod")
                elif word == "flash":
                    print("fastest man alive")
                elif word == "aquaman":
                    print("he controls 70% the earth")
                elif word == "greenlantern":
                    print("this is his sector to protect")
                elif word == "martianmanhunter":
                    print("the man from mars")
                else:
                    print("half human half machine")

            else:
                print("Thanks for playing!")
                time.sleep(2)
                break

        guess = input(
            f"Pick a letter and guess the word... OR PRESS QUIT TO EXIT: {answer}\n ").lower()

        if guess == "quit" or guess == "q":
            break

        if guess in letters:
            guesses = guesses + guess
        else:
            guess = input("Enter a valid letter: ")
        if guess in word or guess not in word:
            turns = turns - 1

            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            elif turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("      o     ")
            elif turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("      o     ")
                print("      |     ")
            elif turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("      o     ")
                print("      |     ")
                print("     /      ")
            elif turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("      o     ")
                print("      |     ")
                print("     / \    ")
            elif turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("    \ o     ")
                print("      |     ")
                print("     / \    ")
            elif turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("    \ o /   ")
                print("      |     ")
                print("     / \    ")
            elif turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("    \ o /|  ")
                print("      |     ")
                print("     / \    ")
            elif turns == 1:
                print("1 turn left ")
                print("last breadths, save him!!")
                print("  --------  ")
                print("    \ o_|/  ")
                print("      |     ")
                print("     / \    ")
            else:
                print("you failed  ")
                print("you let a kind man die")
                print("  --------  ")
                print("      o_|   ")
                print("     /|\    ")
                print("     / \    ")
                print(f"the word was {word}")
                play_again = input("Do you want to play again? (y/n) \n")
                if play_again == "y":
                    word = random.choice(["superman", "batman", "wonderwoman", "flash",
                                          "aquaman", "greenlantern", "martianmanhunter", "cyborg"])
                    guesses = ""
                    turns = 10
                    answer = ""

                    if word == "superman":
                        print("hope of humanity")
                    elif word == "batman":
                        print("billonaire playboy and philantropist")
                    elif word == "wonderwoman":
                        print("demigod")
                    elif word == "flash":
                        print("fastest man alive")
                    elif word == "aquaman":
                        print("he controls 70% the earth")
                    elif word == "greenlantern":
                        print("this is his sector to protect")
                    elif word == "martianmanhunter":
                        print("the man from mars")
                    else:
                        print("half human half machine")

                else:
                    print("Thanks for playing!")
                    time.sleep(2)
                    break


name = input("enter your name:")
print(f"welcome {name}")
print("------------------")
print("guess the name in less than 10 attempts")
print("hint:")

hangman()
