import os, json, csv

#Plain text file

file_path = "output.txt"

try:
    with open(file_path, "r") as file: #"with" closes file automatically because it encloses the open function
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

#JSON file

file_path = "output.json"

try:
    with open(file_path, "r") as file: #"with" closes file automatically because it encloses the open function
        content = json.load(file)
        print(content) #Accessing a value, given the key: content["name"], content["job"]
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

#CSV file

file_path = "output.csv"

try:
    with open(file_path, "r") as file: #"with" closes file automatically because it encloses the open function
        reader = csv.reader(file)
        for line in reader:
            print(line) # To access columns: line[0]
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")