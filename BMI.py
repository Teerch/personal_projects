# app to check your BMI

# tell user to enter height and weight details
height = input("Enter your height in metres: \n")
height = float(height)
weight = input("Enter your weight in kg: \n")
weight = int(weight)

# calculate BMI
BMI = weight/(height*height)

# check if the user is obese, overweight, normal, underweight
while True:
        
    if BMI > 30:
        print(f"{BMI}: You are Obese")
    elif BMI < 30 and BMI >= 25:
        print(f"{BMI}: You are Overweight")
    elif BMI < 25 and BMI >= 18.5:
        print(f"{BMI}: You are Normal")
    else:
        print(f"{BMI}: You are Underweight")
        break