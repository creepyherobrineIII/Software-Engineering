friends = 10

#ASDM operations
#friends = friends + 1 #friends = 0
#friends += 1
#friends = friends - 2
#friends -= 2
#friends = friends * 3 #friends = 5
#friends*= 3
#friends = friends / 2 
#friends /= 2

#Exponents
#friends = friends ** 2 
#friends**= 2

#Modulus
reminder = friends % 3 #friends = 10

print(reminder)

x = 3.14
y = 4
z = 5 

# result = round(x) #x=3.14
# result = abs(y) #y=-4
# result = pow(y, 3) #y=4
#result = max(x, y, z) 

result = min(x, y, z)
print(result)

#Math class functions
import math

x = 9.9

#print(math.pi)
#print(math.e)
#result = math.sqrt(x) #x = 9
#result = math.ceil(x) #x = 9.1

result = math.floor(x) #x = 9.9
print(result)


radius = float(input("Enter radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference of the circle is {round(circumference, 1)} units")

radius = float(input("Enter radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is {round(area, 2)} units^2")

print("Lets find the length of a triangle's hypoteneuse using the Pythagoras theorum:")

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

c = math.sqrt((pow(a, 2) + pow(b, 2)))

print(f"The length of the hypoteneuse is {round(c, 4)} units")