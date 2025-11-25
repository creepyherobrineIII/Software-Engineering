# Python writing files (.txt, .json, .csv)
# Can be relative and absolute paths 
import os


#'with' statement also closes file once it's done
# (file path, mode)
# 'w': write, 'x': create & write (if file does not exist), 'a': append
# 'r': read

'''

txt_data = "I like lasagna!"

file_path = "output.txt"

#Text files
#Example with 'w' and 'x'
#'w' overwrites a file
try:
    with open(file=file_path, mode="x") as file: 
        file.write(txt_data)
        print(f"Text file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

#Example with 'a'
try:
    with open(file=file_path, mode="a") as file: 
        file.write("\n" + txt_data)
        print(f"Text file '{file_path}' was edited")
except FileExistsError:
    print("That file already exists")

#Example with collection(s)

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

try:
    with open(file=file_path, mode="w") as file: 
        for employee in employees:
            file.write(employee + "\n")
        
        print(f"Text file '{file_path}' was edited")
except FileExistsError:
    print("That file already exists")

#JSON File (Made of Key:Value pairs)

import json

file_path = 'output.json'

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

try:
    with open(file=file_path, mode="w") as file: 
        json.dump(employee, file, indent=4) #'indent': Self explanitory
        print(f"Json File '{file_path}' was edited/created")
except FileExistsError:
    print("That file already exists")
'''
#CSV Files
import csv

employees = [["Name", "Age", "Job"], 
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27 , "Scientist"]]

file_path = 'output.csv'

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)

        for row in employees:
            writer.writerow(row)
        
        print(f"CSV File '{file_path}' was edited/created")
except FileExistsError:
    print("That file already exists")