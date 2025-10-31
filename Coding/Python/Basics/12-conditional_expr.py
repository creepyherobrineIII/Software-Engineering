#Conditional expression (tenary operator)

num = 5
a = 6
b = 7
age = 14
temp = 19 # Celsius
user_role = "Guest"

# print("Positive" if num > 0 else "Negative")
# result = "Even" if num % 2 == 0 else "Odd"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "Hot" if temp > 20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)

