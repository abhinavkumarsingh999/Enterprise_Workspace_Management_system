from src.models.base import BaseEntity

"""
department ID is of 4 digit.
"""

class Department(BaseEntity) :
    
    def __init__(self, department_id, department_name) : #id-> 1001
        super().__init__(department_id)
        
        self.department_name = department_name
        self.employees = []
        
        
    @property
    def department_name(self) :
        return self._department_name
    
    @department_name.setter
    def department_name(self, value) :
        if not value.strip() :
            raise ValueError("Department name cannot be empty.")
        self._department_name = value
        
    def add_employee(self, employee) :
        self.employees.append(employee)
        
    def remove_employee(self, employee) :
        if employee in self.employees :
            self.employees.remove(employee)
            
    
    def __str__(self) :
        return (
            f"Department("
            f"{self.department_name}, "
            f"Employees={len(self.employees)})"
        )