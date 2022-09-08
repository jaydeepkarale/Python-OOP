# Encapsulation & self encapsulation with properties
class Dba:
    """
    from encapsulationusingproperty import *
    d = Dba(1, 'Jayd', 'MSSQL')
    d = Dba(1, 'Jayd', 'MSSQL1')
    d = Dba(1, 'Jayd', 'MSSQL')
    d.technical_skill = 'IT'
    """
    TECHNICAL_SKILL = ['MSSQL', 'SQL', 'MYSQL']

    # technical skill here will follow the same validation logic as the technical_skill setter
    # this is called self encapsulation i.e. we get validation for free
    def __init__(self, employee_number, employee_name, technical_skill):
        self.employee_number = employee_number
        self.employee_name = employee_name
        # this validation only works when creating the instance
        # we can however reassign this attribute a new value after instance creation
        # if technical_skill not in Dba.TECHNICAL_SKILL:
        #     raise ValueError("!!! SKILL MISMATCH !!!")
        self.technical_skill = technical_skill

    @property
    def technical_skill(self):
        return self._technical_skill

    @technical_skill.setter
    def technical_skill(self, value):
        if value not in Dba.TECHNICAL_SKILL:
            raise ValueError(f"Cannot create DBA Employee with skillset {value}")
        self._technical_skill = value

