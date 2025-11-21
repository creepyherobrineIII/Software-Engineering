# List comprehensions = A concise way to create lists in python
#                       Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]

#Example (with tradtional loop)

doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)


#Example (with list comprehension)

doubles = [x * 2 for x in range(1, 11)]

print(doubles)

#Exercise 1:

triples = [y * 3 for y in range(1, 11)]
sqaures = [z * z for z in range (1, 11)]

print(sqaures)

#Exercise 2: Strings

fruits = ["apple", "orange", "banana", "coconut"]

uppercase_fruits = [fruit.upper() for fruit in fruits]

fruit_chars = [fruit[0] for fruit in fruits]

print(uppercase_fruits)
print(fruit_chars)

#Example with conditions
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if not (num % 2 == 0)]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

#Exercise 

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)
