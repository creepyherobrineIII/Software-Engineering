# collection = single "variable" used to store multiple variables
# List = [] ordered and changable, Duplicates OK
# Set = {} unordered and immutable, but add/remove OK. No duplicates, 
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#List example
fruits = ["apple", "orange", "banana", "coconut"]

#Universal methods
print(dir(fruits)) #Gives list of attributes then methods for object
print(help(fruits))
print(len(fruits))
print("apple" in fruits)
for fruit in fruits:
    print(fruit)

#List Methods
fruits[1] = "pineapple"
fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pineapple") #Inserts (adds) at the given index, not replacing
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("orange"))
print(fruits.count("orange")) #Counts occurances of given element

print(fruits) #displays whole list
print(fruits[:2]) #Displays first 2 items
print(fruits[::2])  #Displays every 2 items
print(fruits[::-1])  #Displays list in reverse


#Set example (cannot change values = immutable, removes duplicates)
fruits = {"apple", "orange", "banana", "coconut", "coconut"}


#Set Methods
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop() #Removes whatever element comes up first, mostly random
fruits.clear()


print(fruits)


# Tuple Example
fruits = ("apple", "orange", "banana", "coconut", "coconut")


#Tuple specific methods
print(fruits.index("apple"))
print(fruits.count("coconut"))
