#Excercise for dictionaries

menu = {"pizza": 3.00,
        "nachos": 4.50, 
        "popcorn": 6.00, 
        "fries": 2.50, 
        "chips": 1.00, 
        "pretzel": 3.50, 
        "soda": 3.00, 
        "lemonade": 4.25}

cart = []
total = 0

#Showing user options on the menu
print("------------- MENU -------------")
for key, value in menu.items():
    print(f"{key:16}: ${value:.2f}")
print("--------------------------------")

#Getting user input
while True:
    food = input("Select an item (Press \"q\" to quit): ").lower()
    if food == "q":
        break
    elif (menu.get(food) is not None):
        cart.append(food)

for item in cart:
    total += menu.get(item)

print("--------------------------------")
print(f"You ordered the following items: ")

for item in cart:
    print(item, end=" ")

print()
print(f"Your total is: ${total:.2f}")