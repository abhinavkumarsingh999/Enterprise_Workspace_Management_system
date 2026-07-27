from src.models.base import BaseEntity


class Company(BaseEntity) :
    def __init__(self, company_id,company_name) :
        super().__init__(company_id)
        
        self.company_name = company_name
        self.departments = []
        self.projects = []
        
        
    @property
    def company_name(self) :
        return self._company_name
    
    @company_name.setter
    def company_name(self, value) :
        if not value.strip() :
            raise ValueError("company name canno be empty.")
        self._company_name = value
        
    def add_department(self, department) :
        if department not in self.departments:
            self.departments.append(department)
            
    def remove_department(self, department):
        if department in self.departments:
            self.departments.remove(department)
        
    def add_project(self, project) :
        if project not in self.projects:
            self.projects.append(project)
            
    def remove_project(self, project):
        if project in self.projects:
            self.projects.remove(project)
        
    def get_department(self, department_name) :
        for department in self.departments :
            if department.department_name == department_name :
                return department
            
        return None
    
    def __str__(self) :
        return (
            f"Company(ID={self.entity_id},"
            f"Name='{self.company_name}'"
            f"Departments = {len(self.departments)}"
            f"Projects = {len(self.projects)})"
        ) 