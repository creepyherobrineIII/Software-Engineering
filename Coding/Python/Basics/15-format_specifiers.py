#format specifiers = {value:flags} format a value based on what flags are inserted

#Used in context of f-strings

# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = alllocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 30000.14159
price2 = -9870.65
price3 = 1200.34

#Decimal points
print(f"Price 1 is ${price1:.3f} ")
print(f"Price 2 is ${price2:.3f} ")
print(f"Price 3 is ${price3:.3f} ")

#Additional spaces
print(f"Price 1 is ${price1:9} ")
print(f"Price 2 is ${price2:9} ")
print(f"Price 3 is ${price3:09} ") #Adding a zero before the number zero-pads the additional spaces

#Justifying the spaces
print(f"Price 1 is ${price1:>9} ") #Right justify
print(f"Price 2 is ${price2:<9} ") #Left justify
print(f"Price 2 is ${price2:^9} ") #Center align
print(f"Price 3 is ${price3:>09} ") #Zero-padding still works for this


#Showing signs (with plus sign)
print(f"Price 1 is ${price1:+} ") 
print(f"Price 2 is ${price2:+} ") 
print(f"Price 3 is ${price3:+} ") 

#Space before psotive numbers
print(f"Price 1 is ${price1: } ") 
print(f"Price 2 is ${price2: } ") 
print(f"Price 3 is ${price3: } ") 

#Thousands seperator (changing price values)
print(f"Price 1 is ${price1:,} ") 
print(f"Price 2 is ${price2:,} ") 
print(f"Price 3 is ${price3:,} ") 

#Mixing flags
print(f"Price 1 is ${price1:,.2f} ") 
print(f"Price 2 is ${price2:^,} ") 
print(f"Price 3 is ${price3:>11,} ") 
