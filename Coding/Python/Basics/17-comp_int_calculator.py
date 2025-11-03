principal = 0.00
rate = 0.00
time = 0

while principal <= 0:
   principal = float(input("Enter a principal amount: "))

   if principal <= 0:
      print("Principal amount cannot be less than or equal to zero")
    
while rate <= 0:
   rate = float(input("Enter the interest rate: "))

   if rate <= 0:
      print("Interest rate cannot be less than or equal to zero")
    
while time <= 0:
   time = int(input("Enter the time in years: "))

   if time <= 0:
      print("Time cannot be less than or equal to zero")
    

print(f"Your principal amount is {principal}")
print(f"The interest rate is {rate}")
print(f"The time in years of the investment is {time}")

#Calculate compounded interest
total = principal * pow((1 + rate/100), time) #(1 + rate/100)**time 
print(f"Balance after {time} year(s) is: R{total:,.2f}")


#Differnet method (allow zero values, breaking out of loops)
principal = 0.00
rate = 0.00
time = 0

while True:
   principal = float(input("Enter a principal amount: "))

   if principal < 0:
      print("Principal amount cannot be less than zero")
   else:
      break
    
while True:
   rate = float(input("Enter the interest rate: "))

   if rate < 0:
      print("Interest rate cannot be less than zero")
   else:
      break
    
while True:
   time = int(input("Enter the time in years: "))

   if time < 0:
      print("Time cannot be less than zero")
   else:
      break
    

print(f"Your principal amount is {principal}")
print(f"The interest rate is {rate}")
print(f"The time in years of the investment is {time}")

#Calculate compounded interest
total = principal * pow((1 + rate/100), time) #(1 + rate/100)**time 
print(f"Balance after {time} year(s) is: R{total:,.2f}")