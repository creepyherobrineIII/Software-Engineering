# default arguments = A default value for certain parameters
#                      Default is used when that argument is omitted
#                      Makes your functions more flexible, reduces # of arguements
#                      1. Positional, 2. DEFAULT, 3. Keyword, 4. Arbitrary


#Regular function with no default arguments
def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))

#Example with default arguments (which still accepts 2 more arguments)
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))

#Exercise: Count Up Timer
import time

def count(end, start=0): #Non-default arguments should come before default arguments
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(30, 15)