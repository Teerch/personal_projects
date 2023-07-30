money = input("Are you converting to dollar or naira: \n").lower()

naira = "naira"
dollar = "dollar"

if money == naira :
    d_price = input("Enter your money in dollars: \n")
    d_price = int(d_price)
    n_price = int(d_price*762)

    print(f"Your money is #{n_price}")

elif money == dollar:
    n_price = input("Enter your money in naira: \n")
    n_price = int(n_price)
    d_price = float(n_price/762)
    
    print(f"Your money is ${d_price}")