# keyword arguments = an arguments preceded by an identifier
#                     helps with readability 
#                     order of arguments doesn't matter
#                     1. Positional, 2.Default , 3. KEYWORD, 4. Arbitrary


#Function with positional arguments 
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr.", "Spongebob", "Squarepants")

#Function with keyword arguments 
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

#Postional arguments should come BEFORE a keyword argument
hello("Hello", title="Mr.", first="Spongebob", last="Squarepants") 

for x in range(1, 11):
    print(x, end=" ") #"end" is a keyword argument. Cool innit?

print("1", "2", "3", "4", "5", sep="-")

#Exercise: Generate phone number with certain arguments

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)


