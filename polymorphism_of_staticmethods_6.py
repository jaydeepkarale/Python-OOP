""" Polymorphism is the ability of methods to behave differently
based on different conditions such as instances they were called on & so on

Inherited methods are good candidates for providing polymorphic behavior
"""
class Employee:

    @staticmethod
    def _generate_cost_center(employee_number, employee_project, unique_id='EEIndia'):
        return f"{employee_number}--{employee_project}--{unique_id}"

    def __init__(self, employee_number, employee_name, employee_project):
        self.employee_number = employee_number
        self.employee_name = employee_name
        self.employee_project = employee_project
        # if you uncomment this then the cost ceter will be tagged to Employee class
        #self.cost_center = Employee._generate_cost_center(self.employee_number, self.employee_project)
        self.cost_center = self._generate_cost_center(self.employee_number, self.employee_project)


class HREmployee(Employee):
    """
    from employee import *
    h = HREmployee(2,'Shital','Plan Holiday')
    e = Employee(1,'Jaydeep','Build Rockets')
    """

    @staticmethod
    def _generate_cost_center(employee_number, employee_project,  unique_id='HRIIndia'):
        return f"{employee_number}--{employee_project}--{unique_id}"
