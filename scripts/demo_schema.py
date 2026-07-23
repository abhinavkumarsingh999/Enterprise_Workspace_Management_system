from src.models.company import Company
from src.models.employee import Employee
from src.models.project import Project
from src.models.department import Department


def main() :
    # Create a company
    company = Company(name="Tech Innovators Inc.")
    print(f"Company: {company.name}")

    # Create departments
    dept1 = Department(name="Artificial Intelligence", company=company)
    dept2 = Department(name="Web Development", company=company)
    print(f"Departments: {dept1.name}, {dept2.name}")
    
    # Add Departments to the company
    company.add_department(dept1)
    company.add_department(dept2)

    # Create employees
    emp1 = Employee(empId="101",name="Abhinav Kumar Singh", position="AI Engineer", department=dept1)
    emp2 = Employee(empId="201",name="Akshay Sharma", position="Data Scientist", department=dept2)
    emp3 = Employee(empId="202",name="Charlie Brown", position="Frontend Developer", department=dept2)
    emp4 = Employee(empId="102",name="Simran Singh", position="AI Engineer", department=dept1)
    print(f"Employees: {emp1.name}, {emp2.name}, {emp3.name}, {emp4.name}")
    
    # Add Employees to their respective departments
    dept1.add_employee(emp1)
    dept1.add_employee(emp4)
    dept2.add_employee(emp2)
    dept2.add_employee(emp3)

    # Create projects
    proj1 = Project(name="Enterprise Workspace Scaffolding", department=dept1)
    print(f"Projects: {proj1.name}")
    
    # Assign employees to projects
    proj1.assign_employee(emp1)
    proj1.assign_employee(emp2)
    
    # Add projects to company
    company.add_project(proj1)
    
    #Display company structure
    print("\nCompany Structure:")
    print(f"Company: {company.name}")
    
    print("\nDepartments:")
    for dept in company.departments:
        print(f"  Department: {dept.name}")
        for emp in dept.employees:
            print(f"      - {emp.name} ({emp.position})")
        print("    Projects:")
        for proj in company.projects:
            if proj.department == dept:
                print(f"      - {proj.name}")
                print("        Assigned Employees:")
                for assigned_emp in proj.assigned_employees:
                    print(f"          - {assigned_emp.name} ({assigned_emp.position})")
    
    