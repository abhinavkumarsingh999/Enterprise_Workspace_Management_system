import pytest

from src.models.department import Department
from src.models.employee import Employee
from src.controllers.employee_controller import EmployeeController


@pytest.fixture
def department():
    return Department(1, "Artificial Intelligence")


@pytest.fixture
def employee(department):
    return Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        department,
        "Greater Noida",
        80000
    )


@pytest.fixture
def controller():
    return EmployeeController()



# ADD EMPLOYEE

def test_add_employee(controller, employee):
    controller.add_employee(employee)

    assert controller.total_employees() == 1
    assert controller.find_employee_by_id(500001) == employee


# REMOVE EMPLOYEE

def test_remove_employee(controller, employee):
    controller.add_employee(employee)
    controller.remove_employee(500001)

    assert controller.total_employees() == 0
    assert controller.find_employee_by_id(500001) is None



# SEARCH BY ID

def test_find_employee_by_id(controller, employee):
    controller.add_employee(employee)

    result = controller.find_employee_by_id(500001)

    assert result == employee


# SEARCH BY NAME

def test_find_employee_by_name(controller, employee):
    controller.add_employee(employee)

    result = controller.find_employee_by_name("Abhinav Kumar Singh")

    assert result == employee



# SEARCH BY DESIGNATION

def test_find_employee_by_designation(controller, employee):
    controller.add_employee(employee)

    result = controller.find_employee_by_designation(
        "Greater Noida"
    )

    assert len(result) == 1
    assert result[0] == employee



# UPDATE SALARY

def test_update_salary(controller, employee):
    controller.add_employee(employee)

    controller.update_salary(500001, 100000)

    assert employee.salary == 100000



# UPDATE DESIGNATION

def test_update_designation(controller, employee):
    controller.add_employee(employee)

    controller.update_designation(
        500001,
        "Greater Noida West"
    )

    assert employee.designation == "Greater Noida West"



# UPDATE POSITION

def test_update_position(controller, employee):
    controller.add_employee(employee)

    controller.update_position(
        500001,
        "Senior AI Engineer"
    )

    assert employee.position == "Senior AI Engineer"



# UPDATE DEPARTMENT

def test_update_department(controller, employee):
    controller.add_employee(employee)

    new_department = Department(
        1002,
        "Data Science"
    )

    controller.update_department(
        500001,
        new_department
    )

    assert employee.department == new_department



# SORT BY SALARY

def test_sort_by_salary(controller, department):
    emp1 = Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        department,
        "Greater Noida",
        90000
    )

    emp2 = Employee(
        500002,
        "Rahul",
        24,
        "Data Scientist",
        department,
        "Delhi",
        60000
    )

    controller.add_employee(emp1)
    controller.add_employee(emp2)

    result = controller.sort_by_salary()

    assert result[0].salary == 90000



# SORT BY EMPLOYEE ID

def test_sort_by_employee_id(controller, department):
    emp1 = Employee(
            500001,
            "Abhinav Kumar Singh",
            21,
            "AI Engineer",
            department,
            "Greater Noida",
            90000
        )
    
    emp2 = Employee(
        500002,
        "Rahul",
        24,
        "Developer",
        department,
        "Delhi",
        60000
    )

    

    controller.add_employee(emp1)
    controller.add_employee(emp2)

    result = controller.sort_by_employee_id()

    assert result[0] == emp1
    assert result[1] == emp2

    assert result[0].entity_id == 500001
    assert result[1].entity_id == 500002



# FILTER BY DEPARTMENT

def test_filter_by_department(controller, department):
    controller.add_employee(employee := Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        department,
        "Greater Noida",
        90000
    ))

    result = controller.filter_by_department(
        "Artificial Intelligence"
    )

    assert len(result) == 1
    assert result[0] == employee


# AVERAGE SALARY

def test_average_salary(controller, department):
    controller.add_employee(Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        department,
        "Greater Noida",
        80000
    ))

    controller.add_employee(Employee(
        500002,
        "Rahul",
        24,
        "Developer",
        department,
        "Delhi",
        60000
    ))

    assert controller.average_salary() == 70000


# HIGHEST SALARY

def test_highest_salary(controller, department):
    emp1 = Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        department,
        "Greater Noida",
        80000
    )

    emp2 = Employee(
        500002,
        "Rahul",
        24,
        "Developer",
        department,
        "Delhi",
        95000
    )

    controller.add_employee(emp1)
    controller.add_employee(emp2)

    assert controller.highest_salary() == emp2


# LOWEST SALARY

def test_lowest_salary(controller, department):
    emp1 = Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        department,
        "Greater Noida",
        80000
    )

    emp2 = Employee(
        500002,
        "Rahul",
        24,
        "Developer",
        department,
        "Delhi",
        50000
    )

    controller.add_employee(emp1)
    controller.add_employee(emp2)

    assert controller.lowest_salary() == emp2