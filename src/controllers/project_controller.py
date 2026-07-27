from src.models.project import Project
from src.models.employee import Employee


class ProjectController:
    """
    manages project objects and operations
    adding, removing, assigning employee, eliminating employee
    edit project details, finding, sorting, summary of project
    """
    
    def __init__(self) :
        self._projects = []
        
    # OPERATIONS
    def add_project(self, project : Project) :
        """
        Adding project to data collection.
        """
        if not isinstance(project, Project):
            raise TypeError("Only project object can be added")
        
        if self.find_project_by_id(project.entity_id):
            raise ValueError("project ID already exists")
        
        self._projects.append(project)
        
    def remove_project(self, project_id : int) :
        """
        removing projecy by using ID
        """
        project = self.find_project_by_id(project_id)
        
        if project is None:
            raise ValueError("Project can't be empty to be removed.")
        
        self._projects.remove(project)
        
    #UPDATION
    def update_project_title(self, project_id: int, title: str):
        """
        Update the title of a project.
        """
        project = self.find_project_by_id(project_id)

        if project is None:
            raise ValueError("Project not found.")

        if not title.strip():
            raise ValueError("Project title cannot be empty.")

        project.title = title
        
    def update_project_duration(self, project_id: int, duration: int):
        """
        Update the duration of a project.
        """
        project = self.find_project_by_id(project_id)

        if project is None:
            raise ValueError("Project not found.")

        if duration <= 0:
            raise ValueError("Project duration must be greater than 0.")

        project.duration = duration
        
    # SEARCH OPERATIONS
    def find_project_by_id(self, project_id : int):
        """
        SEARCH PROJECT BY PROJECT ID
        """
        for project in self._projects :
            
            if project.entity_id == project_id :
                return project
            
        return None
    
    def find_project_by_title(self, title : str):
        """
        SEARCH PROJECT BY PROJECT TITLE
        """
        for project in self._projects:
            if project.title.lower() == title.lower():
                return project
            
        return None
    
    # EMPLOYEE OPERATIONS ON PROJECT
    
    def assign_employee(self, project_id: int, employee: Employee):
        """
        Assign an employee to a project.
        """
        project = self.find_project_by_id(project_id)

        if project is None:
            raise ValueError("Project not found.")

        if not isinstance(employee, Employee):
            raise TypeError("Employee object required.")

        if employee not in project.employees:
            project.employees.append(employee)

    def remove_employee(self, project_id: int, employee_id: int):
        """
        Remove an employee from a project.
        """
        project = self.find_project_by_id(project_id)

        if project is None:
            raise ValueError("Project not found.")

        for employee in project.employees:
            if employee.entity_id == employee_id:
                project.employees.remove(employee)
                return

        raise ValueError("Employee not assigned to this project.")
    
    # SORTING OPEARTIONS
    
    def sort_by_duration(self):
        """
        Sort projects by duration.
        """
        return sorted(
            self._projects,
            key=lambda project: project.duration
        )

    def sort_by_title(self):
        """
        Sort projects alphabetically.
        """
        return sorted(
            self._projects,
            key=lambda project: project.title.lower()
        )
        
    # STATISTICS
    
    def total_projects(self):
        """
        Return number of projects.
        """
        return len(self._projects)

    def total_assigned_employees(self, project_id: int):
        """
        Return employee count for a project.
        """
        project = self.find_project_by_id(project_id)

        if project is None:
            raise ValueError("Project not found.")

        return len(project.employees)
    
    def total_departments_in_project(self, project_id):
        project = self.find_project_by_id(project_id)

        if project is None:
            raise ValueError("Project not found.")

        departments = set()

        for employee in project.employees:
            departments.add(employee.department.department_name)

        return len(departments)
    
    # GET OPERATIONS
    
    def get_all_projects(self):
        """
        Return all projects.
        """
        return list(self._projects)
    
    # SUMMARY
    
    def project_summary(self):
        """
        Display project summary.
        """
        print("\nProject Summary")

        for project in self._projects:
            print(f"Project ID : {project.entity_id}")
            print(f"Title      : {project.title}")
            print(f"Duration   : {project.duration} Months")

            print("Employees:")

            if project.employees:
                for employee in project.employees:
                    print(
                        f"   {employee.name} "
                        f"({employee.position})"
                    )
            else:
                print("   No employees assigned.")
                
        
        
        
        
        
    