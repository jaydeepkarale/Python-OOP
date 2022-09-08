""" Polymorphism is the ability of methods to behave differently
based on different conditions such as instances they were called on & so on

Inherited methods are good candidates for providing polymorphic behavior
"""
class Employee:

    @staticmethod
    def _generate_cost_center(unique_id='EEIndia'):
        return f"{unique_id}"

    def __init__(self):
        self.cost_center = Employee._generate_cost_center()



class HREmployee(Employee):
    """
    from employee import *
    h = HREmployee(2,'Shital','Plan Holiday')
    e = Employee(1,'Jaydeep','Build Rockets')
    """

    @staticmethod
    def _generate_cost_center(unique_id='HRIIndia'):
        return f"{unique_id}"
