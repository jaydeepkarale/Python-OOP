# Leveraging properties to add more properties
class Dba:
    """
    from employee import *
    d = DBAEmployee2.create_employee_with_default_project(1, 'Jayd', technical_skill='MSSQL',experience_in_years=4)

    # run this next
    d.experience_in_months
    d.experience_in_years

    # run this next
    d.experience_in_years = 6 to demonstrate cannot set experience greater than 5 years

    # run this next
    d.experience_in_months = 72 to demonstrate cannot set experience greater than 5 years & we get validation of years free

    """
    TECHNICAL_SKILL = ['MSSQL', 'ORACLE', 'MYSQL']
    MIN_EXPERIENCE_IN_YEARS = 5

    # technical skill here will follow the same validation logic as the technical_skill setter
    # this is called self encapsulation i.e. we get validation for free
    def __init__(self, technical_skill, experience_in_years):
        self.technical_skill = technical_skill
        self.experience_in_years = experience_in_years

    @property
    def technical_skill(self):
        return self._technical_skill

    @technical_skill.setter
    def technical_skill(self, value):
        if value not in Dba.TECHNICAL_SKILL:
            raise ValueError(f"Cannot create DBA Employee with skillset {value}")
        self._technical_skill = value

    @property
    def experience_in_years(self):
        return self._experience_in_years

    @experience_in_years.setter
    def experience_in_years(self, value):
        if value < Dba.MIN_EXPERIENCE_IN_YEARS:
            raise ValueError("Experience cannot be less than 5 years")
        self._experience_in_years = value

    @staticmethod
    def convert_experience_from_months_to_years(months):
        return months//12

    @staticmethod
    def convert_experience_from_years_to_months(years):
        return years * 12

    @property
    def experience_in_months(self):
        return self.convert_experience_from_years_to_months(self.experience_in_years)

    @experience_in_months.setter
    def experience_in_months(self, value):
        self.experience_in_years = self.convert_experience_from_months_to_years(value)

