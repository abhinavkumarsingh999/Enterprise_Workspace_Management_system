class Company :
    def __init__(self, company_name) :
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
        self.departments.append(department)
        
    def add_project(self, project) :
        self.projects.append(project)
        
    def get_department(self, department_name) :
        for department in self.departments :
            if department.department_name == department_name :
                return department
            
        return None
    
    def __str__(self) :
        return (
            f"Company("
            f"Departments = {len(self.departments)}"
            f"Projects = {len(self.projects)})"
        ) 