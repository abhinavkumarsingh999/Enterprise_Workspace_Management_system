import pytest

from src.models.company import Company
from src.models.department import Department
from src.models.employee import Employee
from src.models.project import Project
from src.controllers.company_controller import CompanyController


@pytest.fixture
def company():
    return Company(
        10001,
        "InternQ"
    )


@pytest.fixture
def controller(company):
    return CompanyController(company)


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


@pytest.fixture
def project():
    return Project(
        2000001,
        "Enterprise Workspace",
        2
    )


def test_add_department(controller, department):
    controller.add_department(department)

    assert controller.total_departments() == 1
    assert controller.find_department("Artificial Intelligence") == department


def test_remove_department(controller, department):
    controller.add_department(department)

    controller.remove_department(1001)

    assert controller.total_departments() == 0


def test_find_department(controller, department):
    controller.add_department(department)

    result = controller.find_department(
        "Artificial Intelligence"
    )

    assert result == department


def test_add_employee(controller, department, employee):
    controller.add_department(department)

    controller.add_employee(
        "Artificial Intelligence",
        employee
    )

    assert len(department.employees) == 1
    assert department.employees[0] == employee


def test_remove_employee(controller, department, employee):
    controller.add_department(department)

    controller.add_employee(
        "Artificial Intelligence",
        employee
    )

    controller.remove_employee(
        "Artificial Intelligence",
        500001
    )

    assert len(department.employees) == 0


def test_find_employee(controller, department, employee):
    controller.add_department(department)

    controller.add_employee(
        "Artificial Intelligence",
        employee
    )

    result = controller.find_employee(500001)

    assert result == employee


def test_search_employee_by_name(controller, department, employee):
    controller.add_department(department)

    controller.add_employee(
        "Artificial Intelligence",
        employee
    )

    result = controller.search_employee_by_name(
        "Abhinav Kumar Singh"
    )

    assert result == employee


def test_add_project(controller, project):
    controller.add_project(project)

    assert controller.total_projects() == 1
    assert controller.find_project_by_id(2000001) == project


def test_remove_project(controller, project):
    controller.add_project(project)

    controller.remove_project(2000001)

    assert controller.total_projects() == 0


def test_find_project_by_id(controller, project):
    controller.add_project(project)

    result = controller.find_project_by_id(2000001)

    assert result == project


def test_assign_employee_to_project(
    controller,
    department,
    employee,
    project
):
    controller.add_department(department)
    controller.add_project(project)

    controller.add_employee(
        "Artificial Intelligence",
        employee
    )

    controller.assign_employee_to_project(
        2000001,
        employee
    )

    assert len(project.employees) == 1
    assert project.employees[0] == employee


def test_total_employees(controller, department):
    controller.add_department(department)

    employee1 = Employee(
        500001,
        "Abhinav",
        21,
        "AI Engineer",
        department,
        "ML Engineer",
        80000
    )

    employee2 = Employee(
        500002,
        "Rahul",
        23,
        "Developer",
        department,
        "Backend Engineer",
        70000
    )

    controller.add_employee(
        "Artificial Intelligence",
        employee1
    )

    controller.add_employee(
        "Artificial Intelligence",
        employee2
    )

    assert controller.total_employees() == 2


def test_total_projects(controller):
    controller.add_project(
        Project(
            2000001,
            "Project A",
            6
        )
    )

    controller.add_project(
        Project(
            202,
            "Project B",
            8
        )
    )

    assert controller.total_projects() == 2


def test_total_departments(controller):
    controller.add_department(
        Department(
            1,
            "AI"
        )
    )

    controller.add_department(
        Department(
            2,
            "Data Science"
        )
    )

    assert controller.total_departments() == 2


def test_total_employees_in_project(
    controller,
    department,
    employee,
    project
):
    controller.add_department(department)
    controller.add_project(project)

    controller.add_employee(
        "Artificial Intelligence",
        employee
    )

    controller.assign_employee_to_project(
        2000001,
        employee
    )

    assert controller.total_employees_in_project(2000001) == 1


def test_total_departments_in_project(
    controller,
    department,
    employee,
    project
):
    controller.add_department(department)
    controller.add_project(project)

    controller.add_employee(
        "Artificial Intelligence",
        employee
    )

    controller.assign_employee_to_project(
        2000001,
        employee
    )

    assert controller.total_departments_in_project(2000001) == 1