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

import exe36

result = exe36.pi
result = exe36.square(3)
result = exe36.cube(3)
result = exe36.circunference(3)
result = exe36.area(3)

print(result)