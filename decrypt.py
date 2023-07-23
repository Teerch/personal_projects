from cryptography.fernet import Fernet, InvalidToken
import time

while True:
    try:
        # asking user to enter name of file where key was stored
        fkey = input("input file name or path of key data: \n")

        print("retrieving your key data")
        time.sleep(2)

        # import pdb; pdb.set_trace()
        # reading the key data and store it into the key variable
        with open(fkey, "rb") as filekey:
            key = filekey.read()

        # using the key data
        fernet = Fernet(key)

        print("key data successfully retrieved")
        time.sleep(1)

        # asking user to input filename of encrypted data
        filename = input("input name or path of encrypted file:\n")

        # opening, read encrypted data and store it into encrypted variable
        with open(filename, "rb") as encrypted_file:
            encrypted = encrypted_file.read()

        print("decrypting your file please wait")
        time.sleep(5)

        # decrypting the encrypted data and store into decrypted variable
        decrypted = fernet.decrypt(encrypted)

        # writing decrypted data back to file
        with open(filename, "wb") as dec_file:
            dec_file.write(decrypted)

        print("your file has been decrypted successfully")
        time.sleep(1.7)
        break
    except (FileNotFoundError, NameError):
        print("enter a valid file name or path")
        time.sleep(1)
    except InvalidToken:
        print("wrong key\n enter the correct key file name or path")
        time.sleep(1)
