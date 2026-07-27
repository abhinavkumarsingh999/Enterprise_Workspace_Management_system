from src.models.department import Department
from src.models.employee import Employee


class DepartmentController:
    """
    Controller class for managing Department objects.
    Provides business logic for department operations.
    """

    def __init__(self):
        self._departments = []

    # Department CRUD Operations

    def add_department(self, department: Department):
        """
        adding a department
        """
        
        if not isinstance(department, Department):
            raise TypeError("Only Department objects can be added.")

        if self.find_department_by_id(department.entity_id):
            raise ValueError("Department ID already exists.")

        self._departments.append(department)

    def remove_department(self, department_id: int):
        """
        removing a department
        """
        
        department = self.find_department_by_id(department_id)

        if department is None:
            raise ValueError("Department not found.")

        self._departments.remove(department)

    # Search Operations

    def find_department_by_id(self, department_id: int):
        
        for department in self._departments:
            if department.entity_id == department_id:
                return department

        return None

    def find_department_by_name(self, department_name: str):
        for department in self._departments:
            if department.department_name.lower() == department_name.lower():
                return department

        return None

    # Employee Operations

    def add_employee(self, department_id: int, employee: Employee):
        department = self.find_department_by_id(department_id)

        if department is None:
            raise ValueError("Department not found.")

        department.add_employee(employee)

    def remove_employee(self, department_id: int, employee_id: int):
        department = self.find_department_by_id(department_id)

        if department is None:
            raise ValueError("Department not found.")

        for employee in department.employees:
            if employee.entity_id == employee_id:
                department.employees.remove(employee)
                return

        raise ValueError("Employee not found.")


    # Get Operations
 
    def get_all_departments(self):
        return list(self._departments)

    
    # Statistics

    def total_departments(self):
        return len(self._departments)

    def total_employees(self, department_id: int):
        department = self.find_department_by_id(department_id)

        if department is None:
            raise ValueError("Department not found.")

        return len(department.employees)

    def average_salary(self, department_id: int):
        department = self.find_department_by_id(department_id)

        if department is None:
            raise ValueError("Department not found.")

        if not department.employees:
            return 0

        total = sum(emp.salary for emp in department.employees)

        return total / len(department.employees)

    def highest_salary(self, department_id: int):
        department = self.find_department_by_id(department_id)

        if department is None:
            raise ValueError("Department not found.")

        if not department.employees:
            return None

        return max(department.employees, key=lambda emp: emp.salary)

    def lowest_salary(self, department_id: int):
        department = self.find_department_by_id(department_id)

        if department is None:
            raise ValueError("Department not found.")

        if not department.employees:
            return None

        return min(department.employees, key=lambda emp: emp.salary)


    # Sorting

    def sort_by_salary(self, department_id: int, reverse=True):
        department = self.find_department_by_id(department_id)

        if department is None:
            raise ValueError("Department not found.")

        return sorted(
            department.employees,
            key=lambda emp: emp.salary,
            reverse=reverse
        )

    def sort_by_age(self, department_id: int):
        department = self.find_department_by_id(department_id)

        if department is None:
            raise ValueError("Department not found.")

        return sorted(
            department.employees,
            key=lambda emp: emp.age
        )

  
    # Summary

    def department_summary(self, department_id: int):
        department = self.find_department_by_id(department_id)

        if department is None:
            raise ValueError("Department not found.")

        print("Department Summary")

        print(f"Department ID   : {department.entity_id}")
        print(f"Department Name : {department.department_name}")
        print(f"Employees       : {len(department.employees)}")

        print("\nEmployee List")

        for employee in department.employees:
            print(
                f"{employee.entity_id} | "
                f"{employee.name} | "
                f"{employee.position} | "
                f"{employee.salary}"
            )