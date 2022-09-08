class Employee(object):

    # The init method is a special method use to `INITIALIZE` an object post creation
    # This is not a constructor because we  give it the argument `self` i.e. instance of a class
    # This means that the class is already created(using the __new__ static method) & the __init__ method receives just the instance
    # Further reading here https://stackoverflow.com/questions/28791639/initializer-vs-constructor
    def __init__(self, name, department):
        self.name = name
        self.department = department


e = Employee('JD','T')