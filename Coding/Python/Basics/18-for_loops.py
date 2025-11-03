#Regular For Loop
for counter in range(1, 11): #Excluding last number in range
    print(counter)


#Reserved countdown
for counter in reversed(range(1, 11)): #Excluding last number in range
    print(counter)


print("HAPPY NEW YEAR!")

#Jumping in for-loop
for counter in range(1, 11, 2): #Excluding last number in range
    print(counter)

#Iterating through strings
credit_card = "1234-5678-9012-3456"

for x in credit_card: 
    print(x)

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
       break   #Breaks out of for-loop and stops loop
    else:
        print(x)

