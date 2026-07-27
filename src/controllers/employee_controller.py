from src.models.employee import Employee
from src.models.department import Department

class EmployeeController:
    ''' manage employee objects
    build logics - add, remove, searching, finding
    and calculating employee data'''
    
    def __init__(self) :
        self._employees = []
        
    # OPERATIONS
    
    def add_employee(self, employee : Employee) :
        """ 
        Adding employee to data.
        """
        
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee objects can be added.")

        if self.find_employee_by_id(employee.entity_id):
            raise ValueError("Employee ID already exists.")

        self._employees.append(employee)
        
    def remove_employee(self, employee_id: int):
        """
        Remove employee using employee ID.
        """
        employee = self.find_employee_by_id(employee_id)

        if employee is None:
            raise ValueError("Employee not found.")

        self._employees.remove(employee)

    def update_salary(self, employee_id: int, salary: float):
        """
        Update salary of an employee.
        """
        employee = self.find_employee_by_id(employee_id)

        if employee is None:
            raise ValueError("Employee not found.")

        employee.salary = salary
        
    def update_designation(self, employee_id: int, designation: str):
        """
        Update designation of an employee.
        """
        employee = self.find_employee_by_id(employee_id)

        if employee is None:
            raise ValueError("Employee not found.")

        employee.designation = designation
        
    def update_department(self, employee_id: int, department: Department):
        """
        Update department of an employee.
        """
        employee = self.find_employee_by_id(employee_id)

        if employee is None:
            raise ValueError("Employee not found.")

        if not isinstance(department, Department):
            raise TypeError("Department object required.")

        employee.department = department
        
    def update_position(self, employee_id: int, position: str):
        """
        Update position of an employee.
        """
        employee = self.find_employee_by_id(employee_id)

        if employee is None:
            raise ValueError("Employee not found.")

        employee.position = position
        
        
    # SEARCHING OPERATIONS
    
    def find_employee_by_id(self, employee_id: int):
        """
        Find employee using ID.
        """
        for employee in self._employees:
            if employee.entity_id == employee_id:
                return employee

        return None

    def find_employee_by_name(self, name: str):
        """
        Find employee using name.
        """
        for employee in self._employees:
            if employee.name.lower() == name.lower():
                return employee

        return None
    
    def find_employee_by_designation(self, designation: str):
        """
        find employee using designation
        """
        total_employees =[]
        for employee in self._employees:
            if employee.designation.lower() == designation.lower():
                total_employees.append(employee)
            
        return total_employees
        
    
    # GET OPERATIONS
    
    def get_all_employees(self):
        """
        Return all employees.
        """
        return list(self._employees)

    def total_employees(self):
        """
        Return total employee count.
        """
        return len(self._employees)
    
    
    # SORTING OPERATIONS
    
    def sort_by_salary(self, reverse=True):
        """
        Sort employees by salary.
        """
        return sorted(
            self._employees,
            key=lambda emp: emp.salary,
            reverse=reverse
        )

    def sort_by_age(self):
        """
        Sort employees by age.
        """
        return sorted(
            self._employees,
            key=lambda emp: emp.age
        )

    def sort_by_name(self):
        """
        Sort employees alphabetically.
        """
        return sorted(
            self._employees,
            key=lambda emp: emp.name.lower()
        )
        
    def sort_by_employee_id(self):
        """
        Sort employees by id
        """
        return sorted(
            self._employees,
            key=lambda emp: emp.entity_id
        )
        
        
    # FILTERING OPERATIONS
    
    def filter_by_department(self, department_name):
        """
        Return employees belonging to a department.
        """
        filtered = []

        for employee in self._employees:
            if employee.department.department_name.lower() == department_name.lower():
                filtered.append(employee)

        return filtered
    
    # STATISTICS
    
    def average_salary(self):
        """
        Calculate average salary.
        """
        if not self._employees:
            return 0

        total = sum(emp.salary for emp in self._employees)

        return total / len(self._employees)

    def highest_salary(self):
        """
        Return employee with highest salary.
        """
        if not self._employees:
            return None

        return max(
            self._employees,
            key=lambda emp: emp.salary
        )

    def lowest_salary(self):
        """
        Return employee with lowest salary.
        """
        if not self._employees:
            return None

        return min(
            self._employees,
            key=lambda emp: emp.salary
        )
        
    # SUMMARY
    
    def employee_summary(self):
        """
        Print employee summary.
        """
        print("\nEmployee Summary")
        print("-" * 40)

        for employee in self._employees:
            print(
                f"{employee.entity_id} | "
                f"{employee.name} | "
                f"{employee.position} | "
                f"{employee.salary}"
            )
    