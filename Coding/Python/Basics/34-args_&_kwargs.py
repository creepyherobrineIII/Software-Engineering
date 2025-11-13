# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#            * unpacking operator
#            1. Positional, 2.Default , 3. Keyword, 4. ARBITRARY (varying amount of arguments)

#Example 1
def add(*args): #*args type is a tuple ()
    total = 0
    for arg in args:
        total+= arg
    return total


print(add(1, 2, 3, 4))

#Can use different names for *args
#Eg: def add(*nums): for num in nums:

#Example 2
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr", "Spongebob","Harold", "Squarepants", "III")

#Kwargs
#Example

def print_address(**kwargs): #Kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    

print_address(apt="100",
              street="123 Fake St.", 
              city= "Detroit", 
              state="MI", 
              zip="54321")

#Exercise: Using both args and kwargs

def shipping_label(*args, **kwargs): #POSITONAL ARGS BEFORE KEYWORD ARGS
    for arg in args:
        print(arg, end=" ")
    print()

    if 'apt' in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif 'pobox' in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
              
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               pobox= "PO Box #100",
               street="123 Fake St.", 
               city= "Detroit", 
               state="MI", 
               zip="54321")