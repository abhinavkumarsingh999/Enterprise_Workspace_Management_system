from src.models.base import BaseEntity
from src.models.department import Department

"""
employee id is of 6 digit.
"""

class Employee(BaseEntity):
    """
    Represents an employee in the company.
    Inherits from BaseEntity to utilize common entity properties.
    """
    
    def __init__(self, employee_id, name, age, position, department, designation, salary):
        super().__init__(employee_id)  # Use empId as the unique identifier -> 101
        
        self.name = name
        self.age = age
        self.position = position
        self.department = department  # Reference to the Department object
        self.designation = designation  # Additional attribute for employee's designation
        self.salary = salary
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Employee name cannot be empty.")
        self._name = value
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value) :
        if value < 18 :
            raise ValueError("Employee age must ab at least 18.")
        self._age = value
        
    @property
    def position(self) :
        return self._position
    
    @position.setter
    def position(self, value):
        if not value.strip():
            raise ValueError("posiiton cannot be empty.")
        self._position = value
        
    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, value):
        if not isinstance(value, Department):
            raise TypeError("Department must be a object.")

        self._department = value
        
     
    @property
    def designation(self) :
        return self._designation
    
    @designation.setter
    def designation(self, value) :
        if not value.strip():
            raise ValueError("Designation cannot be empty.")
        self._designation = value
        
    @property
    def salary(self) :
        return self._salary
    
    @salary.setter
    def salary(self, value) :
        if value <= 0:
            raise ValueError("Salary cannot be greater than zero.")
        self._salary = value
        
    
    def __str__(self) :
        return (
            f"Employee(ID = {self.entity_id},"  # from base.py
            f"Name = '{self.name}',"
            f"Department='{self.department.department_name}', "
            f"Designation='{self.designation}', "
            f"Salary={self.salary})"
        ) 