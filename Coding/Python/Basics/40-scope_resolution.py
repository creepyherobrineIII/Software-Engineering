# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

'''

#Example (Local)
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b) #Cannot access variables in other functions 

func1()
func2()

#Example (Enclosed)
def func1():
    x = 1
    
    def func2():
        print(x) #Uses variable from super function/ enclosed 
    func2()


func1()

#Example (Global)
def func1():
    print(x)

def func2():
    print(x) 


x = 3

func1()
func2()


'''
from math import e

def func1():
    print(e)

e = 3

func1() #Uses global version before the built in version

