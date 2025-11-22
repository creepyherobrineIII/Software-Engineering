# Multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# Multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal: #Multilevel inheritance
    def __init__(self, name):
        self.name = name

    
    def eat(self):
        print(f"{self.name} is eatiing")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #Multiple inheritance
    pass

rabbit = Rabbit("Buggs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()

rabbit.eat()
rabbit.sleep()
#So on so forth...