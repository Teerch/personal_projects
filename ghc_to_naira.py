# ask the user if they want to convert their money to cidi's or naira
money = input("Are you converting to cidi or naira: \n").lower()

naira = "naira"
cidi = "cidi"
# check if the user chose cidi or naira
if money == naira :
    # if the user chose naira code to convert to naira
    c_price = input("Enter your money in cidi: \n")
    c_price = int(c_price)
    n_price = int(c_price*85)
    # print the calculated price
    print(f"Your money is #{n_price}")
    
elif money == cidi:
    # if the user chose cidi code to convert to cidi
    n_price = input("Enter your money in naira: \n")
    n_price = int(n_price)
    c_price = float(n_price/85)
    # print the calculated price
    print(f"Your money is ghc{c_price}")