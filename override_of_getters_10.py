# Overriding of GETTERS is easier & can save us many lines of code
class Employee:

    BASE_PAY = 100
    BASE_BONUS = 50

    def __init__(self, employee_number, employee_name, job_specific_bonus):
        self._employee_number = employee_number
        self._employee_name = employee_name
        self._job_specific_bonus = job_specific_bonus

    @property
    def pay(self):
        return self._job_specific_bonus + Employee.BASE_PAY + Employee.BASE_BONUS


# Inheritance of GETTER properties
class Dba(Employee):
    """
    from employee import *
    d = Dba(2, 'Vijay', 20,)

    # run this next
    d.pay

    """
    BASE_TAX = 10

    @property
    def pay(self):
        return self._job_specific_bonus + Employee.BASE_PAY + Employee.BASE_BONUS - Dba.BASE_TAX

    # @property
    # def pay(self):
    #     return {super().pay - Dba.BASE_TAX}
