# A class in Python is created by using the keyword `class` followed by the name
# A class is a model representation of a real world entity
# For example we can use classes to represent an Employee, a car,
# an animal or basically anything that exists in the real world
class Employee:
    pass


# The naming convention of classes is each new word has to have it's first letter in caps
class ThisIsAlsoAClass:
    pass


# A class has instance attributes & class level attributes
# Instance attributes are defined inside the  __init__ method
# A class also has methods which determine the behavior of the objects of the classes
class EmployeeToDemoInit:

    # This is a class attrib since it's defined immediately after the class name
    # BASE_PAY is all caps because we want it to be a constant & hence the naming convention dictates it to be all caps
    BASE_PAY = 1000

    # name & department are instance attributes since they are defined within the __init__ method
    def __init__(self, name, department):
        self.name = name
        self.department = department

    # this is a method
    def calculate_employee_bonus(self):
        return EmployeeToDemoInit.BASE_PAY + EmployeeToDemoInit.BASE_PAY * .3


# objects are individual instances of a class
# each object has the following attributes
   # is unique
   # has a state
   # and behavior i.e. it's wrking which is nothing but the methods the class has

# object1 = EmployeeToDemoInit('Jaydeep', 'IT')
# print(object1.name)
# print(object1.calculate_employee_bonus())
#
#
# No two objects are equal & hence
# object2 = EmployeeToDemoInit('Vishal', 'HR')
# object3 = EmployeeToDemoInit('Vishal', 'HR')

# object4 = object2 will create equal objects i.e. copies

# del object2 will only delete object2 and object4 will prevail
