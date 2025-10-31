# name = input("Enter your full name: ")
phone_number = input("Enter a phone number: ")

# result = len(name) #Includes whitespace
# result = name.find(" ") #0-Indexes string 
# result = name.rfind("i") #Finds last occurence, returns -1 if cannot find any
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha() #Checks if variable contains only alphabet letters(excluding special characters) 
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")



print(phone_number)

#Useful way to check string method documentation
# print(help(str)) 



# EXERCISE
username = input("Enter your username: ")

if len(username) > 12:
    print("Username should not have more than 12 characters")
elif not username.find(" ") == -1 :      # username.count(" ") > 0 (mine)
    print("Username should not have any spaces")
elif not username.isalpha():        # username.isalpha() == False (mine)
    print("Username should not contain any digits")
else:
    print(f"Welcome {username}")

