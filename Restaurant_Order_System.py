menu =  {
    "burger": 120,
    "pizza": 250,
    "french fries": 90,
    "sandwich": 80,
    "pasta": 180,
    "fried rice": 150,
    "chicken biryani": 220,
    "veg biryani": 180,
    "noodles": 140,
    "grilled chicken": 280,
    "coke": 40,
    "coffee": 60,
    "tea": 30,
    "milkshake": 90,
    "ice cream": 70,
    "brownie": 110
 }
cart=[]
total = 0
for key,value in menu.items():
    print(f"{key:40}: {value:.2f}")
while True:
    food = input("What food do you like? ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print(f"{total:.2f}")
