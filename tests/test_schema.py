import pytest

from src.models.employee import Employee
from src.models.department import Department
from src.models.project import Project
from src.models.company import Company


def test_employee_creation() :
    employee = Employee(
        101,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        "Artifical Intelligence",
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
            105,
            "Rahul Kumar",
            17,
            "Developer",
            "Web Development",
            "Noida",
            50000
        )
        
def test_invalid_salary() :
    with pytest.raises(ValueError) :
        Employee(
            104,
            "Amit Singhal",
            30,
            "Software Engineer",
            "Web Development",
            "Delhi",
            -10000
        )
        
def test_department_add_employee() :
    department = Department(
        1009,
        "Artificial Intelligence"
    )
    
    employee = Employee(
        101,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        "Artificial Intelligence",
        "Greater Noida",
        80000
    )
    
    department.add_employee(employee)
    
    assert len(department.employees) == 1
    assert department.employees[0].name == "Abhinav"
    

def test_project_assignment():
    project = Project(
        50001,
        "Enterprise Workspace",
        2
    )
    
    employee = Employee(
        101,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        "Artificial Intelligence",
        "Greater Noida",
        80000
    )
    
    project.assign_employee(employee)
    assert len(project.employees) == 1
    
    
def test_company_structure() :
    company = Company("InternQ")
    
    department = Department(
       1009,
       "Enterprise Workspace",
       2 
    )
    
    company.add_department(department)
    company.add_project(project=Project)
    
    assert len(company.departments) == 1
    assert len(company.projects) == 1