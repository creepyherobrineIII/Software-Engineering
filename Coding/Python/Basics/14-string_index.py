#Can index multiple points [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) #Only uses start index

print(credit_number[0:4]) #End index is exclusive 
#credit_number[:4] also works; assumes starting index is 0

print(credit_number[5:9])
print(credit_number[5:]) #Assumes you need the whole string from the starting index onwards

#Can also use negative indexing
print(credit_number[-1]) #Outputs = 6
print(credit_number[-4]) #Outputs = 3

#Stepping over characters, need double colon
print(credit_number[::2]) # outputs every 2nd character in string

#Getting last 4 characters from string
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#Reversing a string
credit_number = credit_number[::-1]

print(credit_number)
