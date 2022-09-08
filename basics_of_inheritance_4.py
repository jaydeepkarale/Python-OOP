"""
Python unlike Java support multiple inheritance.
Inheritance is indicated by stating the name of the base class within parenthesis
By default the initializers of base classes will not be called & a call needs
to be made via the super() keyword
"""


class A:
    def __init__(self):
        print("Class A initializer")

# Class B inherits from class A and since the __init__ is missing it will use the A class init
class B(A):
    pass

# Class C inherits from A but it has it's own init method & hence call to A init will not be made implicitly
class C(A):
    def __init__(self):
        print("Class C initializer")

# Class D inherits from A & it has it's own init method. A call to A's init has been done explicity using  super()
class D(A):
    def __init__(self):
        super().__init__()
        print("Class D initializer")


""" In case of multiple inheritance """
class Mom:
    def talk(self):
        print("Mom can talk")

class Dad:
    def talk(self):
        print("Dad can talk")

class Child(Mom, Dad):
    pass
# More reading on MRO
# https://stackoverflow.com/questions/41356378/python-multiple-inheritance-calling-base-class-function