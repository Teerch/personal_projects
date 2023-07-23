import secrets
import string
import time


file_name = input("enter file name to save password in:\n")


while True:
    try:

        pw_length = int(input("Enter length of password greater than 7:\n"))

        def create_pw(pw_length):

            ucl = string.ascii_uppercase  # generate a random uppercase character
            lcl = string.ascii_lowercase  # generate a random lowercase character
            spc = string.punctuation  # generate a random special character
            nums = string.digits  # generate a random digit

            chars = ucl+lcl+spc+nums     # add all random characters
            pwd = ''
            pw_strong = False

            while not pw_strong:
                pwd = ''
                for i in range(pw_length):
                    pwd += ''.join(secrets.choice(chars))

                if (sum(char in spc for char in pwd) >= 3 and sum(char in nums for char in pwd) >= 4):
                    pw_strong = True

            return pwd

        print("your secure password is being created please wait a moment")
        time.sleep(4)

        pswd = create_pw(pw_length)
        pswd = bytes(create_pw(pw_length), "utf-8")
        with open(file_name, "wb") as file:
            file.write(pswd)

        print("your password has been created sucessfully")
        time.sleep(1)

        # print(f"your password is: \n{create_pw(pw_length)}")

        break
    except (ValueError):
        print("enter an integer number")
        time.sleep(1)
