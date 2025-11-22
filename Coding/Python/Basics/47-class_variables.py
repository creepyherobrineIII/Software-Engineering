# Class Variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class


'''

#Example
class Car:

    wheels = 4 #Class variable

    def __init__(self, model, year):
        self.model = model
        self.year = year #Instance variables

# Keep above in block comment

'''
class Student:

    class_year = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 32)
student3 = Student("Squirdward", 55)
student4 = Student("Sandy", 27)

print(student1.name)
print(student1.age)
print(student1.class_year)

print(student2.name)
print(student2.age)
print(student2.class_year)

#Better practice to access class variables
print(Student.class_year)


print(Student.class_year)
print(Student.num_students)

#Better way to print class variables (preference)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
