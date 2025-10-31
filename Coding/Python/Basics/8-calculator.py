operator = input("Enter an operator (+ - * /):")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

operation = 0

if operator == '+':
    operation = round(num1 + num2, 2)
elif operator == '-':
    operation = round(num1 - num2, 2)
elif operator == '*':
    operation = round(num1 * num2, 2)
elif operator == '/':
    operation = round(num1 / num2, 2)
else:
    operation = "invalid operator"

print(operation)