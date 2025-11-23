# Duck typing = Another to achieve polymorphism besides Inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car: #Doesn't explicit inherit Animal class, yet has the minimu requirements to be classified as an Animal
    alive = False

    def speak(self):
        print("HONK")


animals = [Dog(), Cat(), Car()] #Adding a Car Object results in an attribute error

for animal in animals:
    animal.speak()
    print(animal.alive)