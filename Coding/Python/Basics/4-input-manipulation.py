#Tutorial on user input and input manipulation
name = input("What is your name?: ")
age = int(input("How old are you: ")) #Can typecast input

age += 1


print(f"\nHello {name}! Pleasure to meet you \n")
print("HAPPY BIRTHDAY\n")
print(f"You are {age} years old \n")


#Exercise 1 Rectangle Area Calc
length = float(input("What is the length of the rectangle?: "))
width = float(input("\nWhat is the width of the rectangle?: "))

print(f"\nThe area of the rectangle is: {length * width}cm²\n") #Add squared: NumLock + Alt(Hold) + 0178


#Exercise 2 Shopping Cart Program
item = input("What item would you like to buy: ")
price = float(input("\nPrice of item?: "))
quantity = int(input(f"\nHow many {item}(s) would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}(s)")
print(f"Your total is: {total}")