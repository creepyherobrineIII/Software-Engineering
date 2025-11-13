# Iterables = Any object/collection that can return its elements one
#             at a time, allowing it to be iterated over in a loop


#Example
numbers =[1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#Example (with reverse)

for number in reversed(numbers):
    print(number, end=" - ")

#Example (with tuples)
numbers =(1, 2, 3, 4, 5)

for number in numbers:
    print(number)

#Sets
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits: #Cannot be reversed
    print(fruit)


#Strings
name = "John Smith"

for character in name:
    print(character, end=" ")

#Dictionaries
my_dictionary = {"A": 1, "B": 2, "C":3}

for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print(f"{key}: {value}")


