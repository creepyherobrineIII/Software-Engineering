#Example 1
name = input("Enter your name: ")

while name == "":
    print("Your did not enter your name.")
    name = input("Enter your name: ") #Exit strategy

print(f"Hello {name}")

#Example 2
age = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

#Example 3 (with logical operators)

food = input("Enter a food that you like (enter q to quit): ")

while not food == "q":
   print(f"You like {food}")
   food = input("Enter another food that you like (enter q to quit): ")

print("Bye") 

#Example 4 (with logical operators)

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
   print(f"{num} is not in the range")
   num = int(input("Enter a number between 1 and 10: "))

print(f"Your number is {num}") 
