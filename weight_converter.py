weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/L): ").upper()

if unit == "K":
    weight = weight * 2.20462
    print(f"Your weight is {round(weight, 2)} lbs")
elif unit == "L":
    weight = weight / 2.20462
    print(f"Your weight is {round(weight, 2)} kg")
else:
    print("Invalid unit. Please enter K or L.")