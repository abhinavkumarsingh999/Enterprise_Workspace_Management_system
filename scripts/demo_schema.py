from src.models.company import Company
from src.models.employee import Employee
from src.models.project import Project
from src.models.department import Department


def main() :
    # Create a company
    company = Company("InternQ")
    print(f"Company: {company.name}")

    # Create departments
    AI_dept = Department(name="Artificial Intelligence", company=company)
    web_dept = Department(name="Web Development", company=company)
    print(f"Departments: {AI_dept.name}, {web_dept.name}")
    
    # Add Departments to the company
    company.add_department(AI_dept)
    company.add_department(web_dept)

    # Create employees
    emp1 = Employee(
        "101",
        "Abhinav Kumar Singh", 
        21,
        "AI Engineer", 
        AI_dept, 
        "Greater Noida",
        80000
    )
    
    emp2 = Employee(
        "102",
        "Akshay Sharma", 
        25,
        "Frontend Developer",
        web_dept, 
        "Noida",
        50000
    )
    
    emp3 = Employee(
        "103",
        "Rohit singhal", 
        27,
        "AI Engineer", 
        AI_dept, 
        "Delhi",
        90000
    )
    
    emp4 = Employee(
        "104",
        "Rashi Singh", 
        21,
        "Frontend Developer", 
        web_dept, 
        "Gurgaon",
        60000
    )
    
    print(f"Employees: {emp1.name}, {emp2.name}, {emp3.name}, {emp4.name}")
    
    # Add Employees to their respective departments
    AI_dept.add_employee(emp1)
    AI_dept.add_employee(emp3)
    web_dept.add_employee(emp2)
    web_dept.add_employee(emp4)

    # Create projects
    proj1 = Project(
        "Enterprise Workspace Scaffolding",
        AI_dept,
        2
    )
    print(f"Projects: {proj1.name}")
    
    # Assign employees to projects
    proj1.assign_employee(emp1)
    proj1.assign_employee(emp3)
    
    # Add projects to company
    company.add_project(proj1)
    
    #Display company structure
    print("\nCompany Structure:")
    print(f"Company: {company.company_name}")
    
    print("\nDepartments:")
    for department in company.departments:
        print(f"  Department: {department.name}")
        for employee in department.employees:
            print(
                f" Employee ID : {employee.entity_id}\n"
                f" Name        : {employee.name}\n"
                f" Position    : {employee.position}\n"
                f" Designation : {employee.designation}\n"
                f" Salary      : {employee.salary}\n"
            )
        print("\nProjects:")
        
        for proj in company.projects:
            if proj.department == department:
                print(f"      - {proj.name}")
                print("        Assigned Employees:")
                for assigned_emp in proj.assigned_employees:
                    print(f"          - {assigned_emp.name} ({assigned_emp.position})")
                    
        print("Data Schema Demonstration Completed Successfully")
    
if __name__=="__main__":
    main()    