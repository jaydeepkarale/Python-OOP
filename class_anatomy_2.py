class EmployeeToDemoInit:
    next_employee_id = 1
    BASE_PAY = 1000
    LIST_OF_SKILLS_REQUIRED = ['DBA', 'DEV', 'QA']

    def __init__(self, name, years_of_experience, skill, location):
        self.name = name
        self.years_of_experience = years_of_experience
        self.skill = skill
        self.location = location
        self.employee_id = EmployeeToDemoInit.next_employee_id
        EmployeeToDemoInit.next_employee_id += 1

    # this is a regular method
    def calculate_employee_bonus(self):
        return EmployeeToDemoInit.BASE_PAY + EmployeeToDemoInit.BASE_PAY * .3

    @staticmethod
    def _calculate_bonus_on_base_pay():
        return EmployeeToDemoInit.BASE_PAY * .15

    @classmethod
    def create_employee_with_location(cls, name, years_of_experience, skill):
        return cls(name, years_of_experience, skill, location='India')

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, value):
        if value not in EmployeeToDemoInit.LIST_OF_SKILLS_REQUIRED:
            raise ValueError('Skills Do No Match')
        self._skill = value

