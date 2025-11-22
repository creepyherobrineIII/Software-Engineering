from script1 import *

def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script 2")
    favourite_food("ramen noodles") #Calling function from Script 1
    favourite_drink("Pepsi")
    print("Goodbye")

# If we wanted to import script 2's functionality without running the 
# the main block of code, here's what we can do:

if __name__ == '__main__':
    main()