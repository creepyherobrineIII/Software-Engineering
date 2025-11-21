# Membership Operators = used to test whether a value or variable is 
#                        found in a sequence (string, list, tuple, set,
#                        or dictionary)
#                        1. in
#                        2. not in

#Example (with string)

word = "APPLE"

letter = input("Guess a letter in the secret word").upper()

#In Example
if letter in word:
    print(f"There is an {letter} in the secret word")
else:
    print(f"{letter} was not in the word.")

#Not In Example
if letter not in word:
    print(f"{letter} was not in the word.")
else:
    print(f"There is an {letter} in the secret word")

#Example (with set [sets & tuples behave the same])

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found.")


#Example (with dictionaries)

grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

#Another Example
email = "johnsmaith@yahoo.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
