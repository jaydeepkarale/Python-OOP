# Python scope resolution is done using the LEGB(LOCAL ENCLOSED GLOBAL BUILTIN)
# next_gpn is a class attribute & hence it's not available to the __init__ method directly
# and pycharm is kind enough to point that for us
class Employee:

    next_employee_number = 1

    def __init__(self, employee_name, department):
        self.employee_name = employee_name
        self.department = department
        self.employee_number = next_employee_number
        next_employee_number += 1


"""
We can access the next_gpn using two methods now
    a) the self keyword (not preferred method)
    b) the class name which is the preferred method because
       -- using self to reference a class attribute creates a confusion if it's a class attrib or an instance attrib
       -- if we use  self.next_employee_number = self.next_employee_number + 1 instead of next_gpn += 1 it creates a new instance attrib
          which is not something we want
       -- we can demonstrate the same by below example
        e = Employee1(1,'Jaydeep')
        e.employee_number
        e.next_employee_number
        Employee1.next_employee_number
"""


class Employee1:
    next_employee_number = 1

    def __init__(self, employee_name, department):
        self._employee_name = employee_name
        self.department = department
        self.employee_number = Employee1.next_employee_number
        Employee1.next_employee_number += 1
        # self.employee_number = self.next_employee_number
        # self.next_employee_number += 1

""" 
static methods are useful for utility methods
Methods where the object instances(self) are not referenced are
good candidates for static methods
Methods for mathematical calculations, conversions of units are good candidates for static methods
In the above example we saw that generating   
"""
class Employee:

    next_employee_number = 1

    @staticmethod
    def _generate_employee_number():
        employee_number = Employee.next_employee_number
        Employee.next_employee_number += 1
        return employee_number

    def __init__(self, employee_name, department):
        self.employee_name = employee_name
        self.department = department
        self.employee_number = self._generate_employee_number()


"""
Class methods exist to provide alternate initializers.
They help provide more APIs to consumers of the base class without breaking the 
implementors of existing users
"""
class Employee:

    # class methods best serve the purpose of providing alternate initializers
    @classmethod
    def create_employee_with_no_project(cls, employee_number, employee_name):
        return cls(employee_number, employee_name, employee_project=[])

    # class methods best serve the purpose of providing alternate initializers
    @classmethod
    def create_employee_with_default_project(cls, employee_number, employee_name):
        return cls(employee_number, employee_name, employee_project=['Build Rockets'])

    def __init__(self, employee_number, employee_name, employee_project):
        self.employee_number = employee_number
        self.employee_name = employee_name
        self.employee_project = employee_project
