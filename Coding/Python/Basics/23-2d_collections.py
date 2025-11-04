#2D Lists (2D Tuples are also possible)

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrot", "potato"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

#print(groceries) #Can be used to display all elements of 2d-list
#print(groceries[1][1]) #Used to print specific elements from nested list

print()

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

#Exercise (2D Keypad for phone) (using tuples because: (1)tuples are faster & ordered)

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()