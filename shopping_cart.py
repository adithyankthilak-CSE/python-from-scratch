# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter food (q to quit): ")

    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("\n------ YOUR CART ------")

for i in range(len(foods)):
    print(f"{foods[i]} - ${prices[i]:.2f}")
    total += prices[i]

print("-----------------------")
print(f"Total: ${total:.2f}")