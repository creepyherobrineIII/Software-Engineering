#Example with relative file paths
import os

file_path = "Exercise-59/text.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print(f"That is a file")
    elif os.path.isdir(file_path):
        print(f"That is a directory") #Used when using absolute pathing

else:
    print("The location does not exist")