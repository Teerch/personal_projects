from cryptography.fernet import Fernet
import time


# generate our key
key = Fernet.generate_key()
# file name to save key as
fkey = input("enter name to save your key as: \n")
# writing key data to file
with open(fkey, "wb") as filekey:
    filekey.write(key)
print("creating your key")
time.sleep(2.5)
# reading key data from file to use
with open(fkey, "rb") as filekey:
    key = filekey.read()
# using the key data
fernet = Fernet(key)
print("key created successfully")


while True:
    try:
        # asking user to enter name of file to encrypt
        filename = input("Enter name or path of file to encrypt:\n")

        # reading what is in your file to encrypt and storing into the variable original 
        with open(filename, "rb") as file:
            original = file.read()

        # encrypting your file
        encrypted = fernet.encrypt(original)

        print("encrypting your file")
        time.sleep(5)

        # writing encrypted data back to file
        with open(filename, "wb") as encrypted_file:
            encrypted_file.write(encrypted)

        print("Your file has been encrypted successfully")
        time.sleep(2)
        break

    except (FileNotFoundError, NameError):
        print("enter a valid file name or path")
        time.sleep(2)
