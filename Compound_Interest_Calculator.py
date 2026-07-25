# Compound Interest Calculator

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: $"))
    if principal <= 0:
        print("Principal cannot be less than or equal to 0.")
    else:
        break

while True:
    rate = float(input("Enter the annual interest rate (%): "))
    if rate <= 0:
        print("Rate cannot be less than or equal to 0.")
    else:
        break

while True:
    time = float(input("Enter the time (years): "))
    if time <= 0:
        print("Time cannot be less than or equal to 0.")
    else:
        break

total = principal * pow((1 + rate / 100), time)

print(f"\nThe total amount after {time} years is ${total:.2f}")