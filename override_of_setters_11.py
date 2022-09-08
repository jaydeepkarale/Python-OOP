class Employee:

    BASE_PAY = 100
    BASE_BONUS = 50

    def __init__(self, employee_number, employee_name, job_specific_bonus, **kwargs):
        self.employee_number = employee_number
        self.employee_name = employee_name
        self.job_specific_bonus = job_specific_bonus

    # @property
    # def pay(self):
    #     return self.job_specific_bonus + Employee.BASE_PAY + Employee.BASE_BONUS

    @property
    def pay(self):
        return self._calc_pay()

    def _calc_pay(self):
        return self.job_specific_bonus + Employee.BASE_PAY + Employee.BASE_BONUS


class Dba(Employee):

    MIN_EXPERIENCE_IN_YEARS = 5
    BASE_TAX = 10

    def __init__(self, employee_number, employee_name, job_specific_bonus, *, experience_in_years, **kwargs):
        super().__init__(employee_number, employee_name, job_specific_bonus, **kwargs)
        self.experience_in_years = experience_in_years

    # @property
    # def pay(self):
    #     return {super().pay - Dba.BASE_TAX}

    def _calc_pay(self):
        return super()._calc_pay() - Dba.BASE_TAX

    @property
    def experience_in_years(self):
        return self._experience_in_years

    @experience_in_years.setter
    def experience_in_years(self, value):
        if value < Dba.MIN_EXPERIENCE_IN_YEARS:
            raise ValueError("Experience cannot be less than 5 years")
        self._experience_in_years = value


# class SeniorDBA(Dba):
#
#     MAX_EXPERIENCE_IN_YEARS = 10
#
#     # Pycharm already complains about the experience property not being available within this scope
#     # We can solve this problem by calling the experience_in_years on Dba.experience_in_years but it makes the setter wordy
#     # also we have duplicated the check for minimum experience
#     @experience_in_years.setter
#     def experience_in_years(self,value):
#         if not(
#             Dba.MIN_EXPERIENCE_IN_YEARS
#             <=
#             value
#             <= SeniorDBA.MAX_EXPERIENCE_IN_YEARS
#         ):
#             raise ValueError("!!! EXPERIENCE DOES NOT MATCH")
#         self.experience_in_years = value

"""
this problem can be solved by instead not overriding getters & settter at all
& instead having an additional level of delegation
"""
# class SeniorDBA(Dba):
#
#     MAX_EXPERIENCE_IN_YEARS = 10
#
#     # Pycharm already complains about the experience property not being available within this scope
#     # We can solve this problem by calling the experience_in_years on Dba.experience_in_years but it makes the setter wordy
#     # also we have duplicated the check for minimum experience
#     @Dba.experience_in_years.setter
#     def experience_in_years(self, value):
#         if not(
#             Dba.MIN_EXPERIENCE_IN_YEARS
#             <=
#             value
#             <= SeniorDBA.MAX_EXPERIENCE_IN_YEARS
#         ):
#             raise ValueError("!!! EXPERIENCE DOES NOT MATCH")
#         self.experience_in_years = value
