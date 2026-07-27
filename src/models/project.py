from src.models.base import BaseEntity

"""
project ID is of 7 digit.
"""

class Project(BaseEntity):
    def __init__(self, project_id, title, duration) :
        super().__init__(project_id) # project id -> 50001
        
        self.title = title      #project name
        self.duration = duration    #project building tenure in months
        self.employees = []
        
    @property
    def title(self) :
        return self._title
    
    @title.setter
    def title(self, value) :
        if not value.strip() :
            raise ValueError("Project title connot be empty.")
        self._title = value
        
    @property
    def duration(self) :
        return self._duration
    
    @duration.setter
    def duration(self, value) :
        if value <=0 :
            raise ValueError("Duration cannot be negative or zero.")
        self._duration = value
        
    def assign_employee(self, employee) :
        if employee not in self.employees :
            self.employees.append(employee)
            
    def __str__(self) :
        return (
            f"Project("
            f"{self.title}, "
            f"Duration={self.duration} months"
        )
            
        
     