# Module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program into reusable seperate files


'''

#Examples
#Method 1
import math

print(f"{math.pi:.5f}")

#Method 2 (with an alias)
import time as t

print(t.altzone)

#Method 3 (can result in naming conflicts)
from math import pi
print(pi)

'''

import Additional_Files.Exercise_39.exe39 as exe39

result = exe39.pi
result = exe39.square(3)
result = exe39.cube(3)
result = exe39.circunference(3)
result = exe39.area(3)

print(result)