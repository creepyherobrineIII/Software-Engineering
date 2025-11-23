# Static methods = A method that belongs to a class, rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

#Example
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    #Instance Method
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position): #Does not include 'self' arg because does not use anything from the class
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
    
print(Employee.is_valid_position("Cook")) #Static method: Only accessing class, do not to create instance of class
print(Employee.is_valid_position("Rocket Scientist"))

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info()) #Instance method: Access object, THEN call instance method
print(employee2.get_info())
print(employee3.get_info())