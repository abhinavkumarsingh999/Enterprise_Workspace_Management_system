import pytest

from src.models.employee import Employee
from src.models.department import Department
from src.models.project import Project
from src.models.company import Company

AI_department = Department(
    1001,
    "Artificial Intelligence"
)

Web_department = Department(
    1002,
    "Web Development"
)    
    
def test_employee_creation() :
    employee = Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        AI_department,
        "Greater Noida",
        80000
    )
    
    assert employee.name == "Abhinav Kumar Singh"
    assert employee.age == 21
    assert employee.salary == 80000
    assert employee.designation == "Greater Noida"
    
def test_invalid_age() :
    with pytest.raises(ValueError) :
        Employee(
            500002,
            "Rahul",
            17,
            "Developer",
            Web_department,
            "Noida",
            50000
        )
        
def test_invalid_salary() :
    with pytest.raises(ValueError) :
        Employee(
            500004,
            "Amit Singhal",
            30,
            "Software Engineer",
            Web_department,
            "Delhi",
            -10000
        )
        
def test_department_add_employee() :
    department = Department(
        1001,
        "Artificial Intelligence"
    )
    
    employee = Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        AI_department,
        "Greater Noida",
        80000
    )
    
    department.add_employee(employee)
    
    assert len(department.employees) == 1
    assert department.employees[0].name == "Abhinav Kumar Singh"
    

def test_project_assignment():
    project = Project(
        2000001,
        "Enterprise Workspace",
        2
    )
    
    employee = Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        AI_department,
        "Greater Noida",
        80000
    )
    
    project.assign_employee(employee)
    assert len(project.employees) == 1
    
    
def test_company_structure() :
    company = Company(
        10001,
        "InternQ"
        )
    
    department1 = Department(
       1003,
       "Enterprise Workspace" 
    )
    
    project = Project(
        2000001,
        "Enterprise Workspace",
        2
    )
    
    company.add_department(department1)
    company.add_project(project=project)
    
    assert len(company.departments) == 1
    assert len(company.projects) == 1