#Lists
foods = []
prices = []
total = 0.00

while True:
    food = input("Enter a food to buy (press \"q\" to quit): ")

    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: R"))
        foods.append(food)
        prices.append(price)

print()
print("----- YOUR CART -----")

for food in foods:
    print(food)

for price in prices:
    total += price

print("---------------------")
print()
print(f"Tour total is: R{total:.2f}")
print()