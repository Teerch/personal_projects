import string
import getpass
import time

def check_password_strength(password):
    lac=uac=nc=wc=scc=0
    for char in list(password):
        if char in string.ascii_lowercase:
            lac += 1
        elif char in string.ascii_uppercase:
            uac += 1
        elif char in string.digits:
            nc +=1
        elif char == " ":
            wc += 1
        else:
            scc += 1

    strength = 0

    if lac >= 1:
        strength += 1
    if uac >= 1:
        strength += 1
    if nc >= 1:
        strength += 1
    if wc >= 1:
        strength += 1
    if scc >= 1:
        strength += 1 

    
    if strength == 1:
        remarks = "That's a very bad password. change it as soon as possible"
    elif strength == 2:
        remarks = "Bad password change it to somether batter and stronger"
    elif strength == 3:
        remarks = "Good password but improvements can be made"
    elif strength == 4:
        remarks = "Strong password but can be better "
    else:
        remarks ="That's a very strong password "


    print("Your password has:-")
    print(f"{lac} lowercase letters")
    print(f"{uac} uppercase letters")
    print(f"{nc} digits")
    print(f"{wc} whitespaces")
    print(f"{scc} special characters")
    print(f"Password score: {strength}/5")
    print(f"Remarks: {remarks}")



print("===== Welcome to Password Strength Checker =====")
time.sleep(1)

while True:
    choice = input("Do you wantt to check a password's strength?  (y/n)").lower()
    if choice == "y":
        password = getpass.getpass("Enter the password:\n")
        check_password_strength(password)
    elif choice == "n":
        print("Exiting")
        time.sleep(2)
        break
    else:
        print("Invalid input...please try again")
    