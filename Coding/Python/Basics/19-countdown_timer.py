import time
import math

#Creating a countdown timer (method 1)
my_time = int(input("Enter time in seconds: "))

for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)

print("TIME'S UP!")

#Creating a countdown timer (method 2)
my_time = int(input("Enter time in seconds: "))

for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

print("TIME'S UP!")

#Displaying a digital clock (with zero padding)
my_time = int(input("Enter time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = (math.floor(x / 60) % 60)
    hours = math.floor(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")