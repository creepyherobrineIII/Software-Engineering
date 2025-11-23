# Decorator = A function that extends the behaviour of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decoration

#             @add_sprinkles
#             get_ice_cream("vanilla")


#Precede base function with modifier function
def add_sprinkles(func):
    def wrapper(): #Necessary to prevent the decorator from executing the base function
        print("You add sprinkles")
        func()
    return wrapper

def add_fudge(func):
    def wrapper():
        print("You add fudge")
        func()
    return wrapper

@add_sprinkles
@add_fudge  #Can add more than one decorator function {order matters}
def get_ice_cream():
    print("Here is your ice cream")

get_ice_cream()

#Example with arguements

def add_sprinkles(func):
    def wrapper(*args, **kwargs): #Adding *args, **kwargs is necessary to accept arguments in the base function
        print("*You add sprinkles*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge 
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")

get_ice_cream("vanilla")