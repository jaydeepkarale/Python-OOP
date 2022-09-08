class Employee:

    @classmethod
    def create_employee_with_default_project(cls, employee_number, employee_name, **kwargs):
        return cls(employee_number, employee_name, employee_project=['Build Rockets'], **kwargs)

    def __init__(self, employee_number, employee_name, employee_project, **kwargs):
        self._employee_number = employee_number
        self._employee_name = employee_name
        self._employee_project = employee_project


# Inheritance of class methods
class Dba(Employee):
    """
    from employee import *
    d = Dba.create_employee_with_default_project(1, 'Jayd', technical_skill='MSSQL')

    # run this next
    d.technical_skill
    """
    TECHNICAL_SKILL = ['MSSQL', 'SQL', 'MYSQL']

    # base classes should have no knowledge of attributes of sub/inheriting classes.
    # hence use the **kwargs to pass on named attributes to constructors inherited from base classses
    def __init__(self, employee_number, employee_name, employee_project, *, technical_skill, **kwargs):
        super().__init__(employee_number, employee_name, employee_project,  **kwargs)
        if technical_skill not in Dba.TECHNICAL_SKILL:
            raise ValueError(f"Cannot create DBA Employee with skillset {technical_skill}")
        self._technical_skill = technical_skill

