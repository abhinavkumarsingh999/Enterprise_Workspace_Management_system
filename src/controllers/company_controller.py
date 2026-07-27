from src.models.project import Project
from src.models.employee import Employee
from src.models.department import Department
from src.models.company import Company

class CompanyController:
    """
    central controller of company
    handles departments, employees and projects
    """
    
    def __init__(self, company : Company) :
        if not isinstance(company, Company):
            raise TypeError("Company Object required.")
        self.company = company
        
    # DEPARTMENT OPERATIONS
    
    def add_department(self, department: Department):
        """
        Adding a new department in company.
        """
        
        if not isinstance(department, Department):
            raise TypeError("Department object required.")

        if department in self.company.departments:
            raise ValueError("Department already exists.")

        self.company.departments.append(department)
        

    def remove_department(self, department_id: int):
        """
        removing a department from the company.
        """
        
        for department in self.company.departments:
            if department.entity_id == department_id:
                self.company.departments.remove(department)
                return

        raise ValueError("Department not found.")

    def find_department(self, department_name: str):
        for department in self.company.departments:
            if department.department_name.lower() == department_name.lower():
                return department

        return None
    
    #EMPLOYEE OPERATIONS
    def add_employee(self, department_name: str, employee: Employee):
        """
        Adding employee to department
        """
        
        department = self.find_department(department_name)

        if department is None:
            raise ValueError("Department not found.")

        department.add_employee(employee)

    def remove_employee(self, department_name: str, employee_id: int):
        department = self.find_department(department_name)

        if department is None:
            raise ValueError("Department not found.")

        for employee in department.employees:
            if employee.entity_id == employee_id:
                department.employees.remove(employee)
                return

        raise ValueError("Employee not found.")

    def find_employee(self, employee_id: int):
        for department in self.company.departments:
            for employee in department.employees:
                if employee.entity_id == employee_id:
                    return employee

        return None
    
    # PROJECT OPERATIONS
    
    def add_project(self, project: Project):
        """
        adding a new project
        """
        for existing_project in self.company.projects:
            if existing_project.entity_id == project.entity_id:
                raise ValueError("Project ID already exists.")
            if not isinstance(project, Project):
                raise TypeError("Project object required.")

        self.company.projects.append(project)

    def remove_project(self, project_id: int):
        """
        removing a project
        """
        
        for project in self.company.projects:
            if project.entity_id == project_id:
                self.company.projects.remove(project)
                return

        raise ValueError("Project not found.")

    def assign_employee_to_project(self,project_id: int,employee: Employee):
        """
        assigning employee to project
        """
        
        for project in self.company.projects:
            if project.entity_id == project_id:
                project.assign_employee(employee)
                return

        raise ValueError("Project not found.")
    
    #STATISTICS
    
    def total_employees_in_project(self, project_id: int):
        """
        Return the number of employees assigned to a project.
        """
        project = self.find_project_by_id(project_id)

        if project is None:
            raise ValueError("Project not found.")

        return len(project.employees)
    
    def total_departments_in_project(self, project_id: int):
        """
        Return the number of unique departments
        represented in a project.
        """
        project = self.find_project_by_id(project_id)

        if project is None:
            raise ValueError("Project not found.")

        departments = set()

        for employee in project.employees:
            # If employee.department is a Department object
            departments.add(employee.department.department_name)

            # If employee.department is a string instead, use:
            # departments.add(employee.department)

        return len(departments)

    def total_departments(self):
        return len(self.company.departments)
    
    def total_projects(self):
        return len(self.company.projects)

    def total_employees(self):
        count = 0

        for department in self.company.departments:
            count += len(department.employees)

        return count
    
    # SEARCH OPERATION
    def search_employee_by_name(self, name: str):
        for department in self.company.departments:
            for employee in department.employees:
                if employee.name.lower() == name.lower():
                    return employee

        return None
    
    
    def find_project_by_id(self, project_id: int):
        for project in self.company.projects:
            if project.entity_id == project_id:
                return project

        return None
    
    
    # SUMMARY
    def list_all_departments(self):
        """
        Display all departments.
        """

        if not self.company.departments:
            print("No departments available.")
            return

        print("\nDepartments")
        

        for department in self.company.departments:
            print(
                f"ID : {department.entity_id}"
            )
            print(
                f"Name : {department.department_name}"
            )
            print(
                f"Employees : {len(department.employees)}"
            )
    
    def list_all_projects(self):
        """
        Display all projects.
        """

        if not self.company.projects:
            print("No projects available.")
            return

        print("\nProjects")
        

        for project in self.company.projects:
            print(
                f"Project ID : {project.entity_id}"
            )
            print(
                f"Title      : {project.title}"
            )
            print(
                f"Duration   : {project.duration} Months"
            )
            print(
                f"Employees  : {len(project.employees)}"
            )
        
            
    def company_summary(self):
        print("COMPANY SUMMARY")

        print(f"Company Name : {self.company.company_name}")
        print(f"Departments  : {self.total_departments()}")
        print(f"Employees    : {self.total_employees()}")
        print(f"Projects     : {self.total_projects()}")

        print("\nDepartments")

        for department in self.company.departments:
            print(f"  {department.department_name}")
            print(f"     Employees : {len(department.employees)}")

        print("\nProjects")

        for project in self.company.projects:
            print(f"  {project.title}")
            print(f"     Duration : {project.duration} Months")
            print(f"     Employees: {len(project.employees)}")
    