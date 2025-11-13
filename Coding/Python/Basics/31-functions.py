# Functions

def happy_birthday(name):
    print(f"Happy birthday to {name}")
    print("You are old!")
    print("Happy birthday to you")
    print()

happy_birthday("John")

#Functions with multiple parameters
def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} year(s) old!")
    print("Happy birthday to you")
    print()

happy_birthday("John", 20)
happy_birthday("Steve", 38)
happy_birthday("Peter", 24)

#Function to display an invoice

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


display_invoice("Jonathan Smith", 34.2567, "03/11")

#Functions with return statements

def add(x, y):
    a = x + y
    return a

def subtract(x, y):
    a = x - y
    return a

def multiply(x, y):
    a = x * y
    return a

def divide(x, y):
    a = x / y
    return a


print()
print(add(5,-21))
print(subtract(5,-21))
print(multiply(5,-21))
print(divide(5,-21))

#Function to create a full name

def create_name(first, last):
    first = first.capitalize()
    last= last.capitalize()
    return first + " " + last

full_name = create_name("jonathan", "smith")

print()
print(full_name)