# Dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.", 
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}


#Dictionary Methods
print(capitals.get("USA")) #Returns value associated with key, returns "none" if no key is found

if capitals.get("Japan"): #Checking if key is in dictionary
    print("That capital exists")
else:
    print("That capital does not exist")

capitals.update({"Germany": "Berlin"}) #Can insert new K:V pair, or update K:V Pair
capitals.update({"USA": "Detroit"}) #Update example

capitals.pop("China") #Removes K:V pair from given key
capitals.popitem() #Removes latest K:V pair from dictionary

capitals.clear() #Clears dictionary

keys = capitals.keys() #Returns an object with all keys, iterable & resembles a list
for key in keys:
    print(key)


values = capitals.values() #Returns an object with all values, iterable & resembles a list

print(values)
print()

for value in values:
    print(value)

items = capitals.items() #Returns an object with all items from dictionary, resembles a 2D-list of tuples

for key, value in items:
    print(f"{key}: {value}")
