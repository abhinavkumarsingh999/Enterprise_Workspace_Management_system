import pytest

from src.models.department import Department
from src.models.employee import Employee
from src.controllers.department_controller import DepartmentController


@pytest.fixture
def controller():
    return DepartmentController()


@pytest.fixture
def department():
    return Department(
        1001,
        "Artificial Intelligence"
    )


@pytest.fixture
def employee(department):
    return Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        department,
        "Machine Learning Engineer",
        80000
    )


def test_add_department(controller, department):
    controller.add_department(department)

    assert controller.total_departments() == 1
    assert controller.find_department_by_id(1001) == department


def test_remove_department(controller, department):
    controller.add_department(department)

    controller.remove_department(1001)

    assert controller.total_departments() == 0
    assert controller.find_department_by_id(1001) is None


def test_find_department_by_id(controller, department):
    controller.add_department(department)

    result = controller.find_department_by_id(1001)

    assert result == department


def test_find_department_by_name(controller, department):
    controller.add_department(department)

    result = controller.find_department_by_name(
        "Artificial Intelligence"
    )

    assert result == department


def test_add_employee(controller, department, employee):
    controller.add_department(department)

    controller.add_employee(
        1001,
        employee
    )

    assert len(department.employees) == 1
    assert department.employees[0] == employee


def test_remove_employee(controller, department, employee):
    controller.add_department(department)

    controller.add_employee(
        1001,
        employee
    )

    controller.remove_employee(
        1001,
        500001
    )

    assert len(department.employees) == 0


def test_total_employees(controller, department):
    controller.add_department(department)

    employee1 = Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        department,
        "Greater Noida",
        80000
    )

    employee2 = Employee(
        500002,
        "Rahul",
        23,
        "Developer",
        department,
        "Delhi",
        70000
    )

    controller.add_employee(1001, employee1)
    controller.add_employee(1001, employee2)

    assert controller.total_employees(1001) == 2


def test_average_salary(controller, department):
    controller.add_department(department)

    controller.add_employee(
        1001,
        Employee(
            500001,
            "Abhinav Kumar Singh",
            21,
            "AI Engineer",
            department,
            "Greater Noida",
            80000
        )
    )

    controller.add_employee(
        1001,
        Employee(
            500002,
            "Rahul",
            23,
            "Developer",
            department,
            "Delhi",
            60000
        )
    )

    assert controller.average_salary(1001) == 70000


def test_highest_salary(controller, department):
    controller.add_department(department)

    emp1 = Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        department,
        "ML Engineer",
        80000
    )

    emp2 = Employee(
        500002,
        "Rahul",
        23,
        "Developer",
        department,
        "Delhi",
        90000
    )

    controller.add_employee(1001, emp1)
    controller.add_employee(1001, emp2)

    assert controller.highest_salary(1001) == emp2


def test_lowest_salary(controller, department):
    controller.add_department(department)

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
        23,
        "Developer",
        department,
        "delhi",
        50000
    )

    controller.add_employee(1001, emp1)
    controller.add_employee(1001, emp2)

    assert controller.lowest_salary(1001) == emp2


def test_sort_by_salary(controller, department):
    controller.add_department(department)

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
        23,
        "Developer",
        department,
        "Delhi",
        60000
    )

    controller.add_employee(1001, emp1)
    controller.add_employee(1001, emp2)

    result = controller.sort_by_salary(1001)

    assert result[0] == emp1


def test_sort_by_age(controller, department):
    controller.add_department(department)

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
        25,
        "Developer",
        department,
        "Delhi",
        60000
    )

    controller.add_employee(1001, emp1)
    controller.add_employee(1001, emp2)

    result = controller.sort_by_age(1001)

    assert result[0] == emp1