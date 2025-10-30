age = int(input("Enter your age: "))

#Check if they are eligible for credit card applications

if age >=100:
    print("You are too old for a credit card") #Code after "if" needs to be indented
elif age >= 18:
    print("You are eligible") 
elif age < 0:
    print("You haven't been born") 
else: 
    print("You must 18+ to sign-up")

response = input("Would you like food? (Y/N): ")

if response == 'Y':
    print("Have some food!")
else:
    print("No food for you")

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}!")

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")


online = False

if online:
    print("The user is online")
else:
    print("The user is offline")
