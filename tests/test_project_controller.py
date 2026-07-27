import pytest

from src.models.department import Department
from src.models.employee import Employee
from src.models.project import Project
from src.controllers.project_controller import ProjectController


@pytest.fixture
def controller():
    return ProjectController()


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
        "Greater Noida",
        80000
    )


@pytest.fixture
def project():
    return Project(
        2000001,
        "Enterprise Workspace",
        2
    )


def test_add_project(controller, project):
    controller.add_project(project)

    assert controller.total_projects() == 1
    assert controller.find_project_by_id(2000001) == project


def test_remove_project(controller, project):
    controller.add_project(project)

    controller.remove_project(2000001)

    assert controller.total_projects() == 0
    assert controller.find_project_by_id(2000001) is None


def test_find_project_by_id(controller, project):
    controller.add_project(project)

    result = controller.find_project_by_id(2000001)

    assert result == project


def test_find_project_by_title(controller, project):
    controller.add_project(project)

    result = controller.find_project_by_title(
        "Enterprise Workspace"
    )

    assert result == project


def test_update_project_title(controller, project):
    controller.add_project(project)

    controller.update_project_title(
        2000001,
        "AI Enterprise Workspace System"
    )

    assert project.title == "AI Enterprise Workspace System"


def test_update_project_duration(controller, project):
    controller.add_project(project)

    controller.update_project_duration(
        2000001,
        12
    )

    assert project.duration == 12


def test_assign_employee(controller, project, employee):
    controller.add_project(project)

    controller.assign_employee(
        2000001,
        employee
    )

    assert len(project.employees) == 1
    assert project.employees[0] == employee


def test_remove_employee(controller, project, employee):
    controller.add_project(project)

    controller.assign_employee(
        2000001,
        employee
    )

    controller.remove_employee(
        2000001,
        500001
    )

    assert len(project.employees) == 0


def test_total_assigned_employees(controller, project, employee):
    controller.add_project(project)

    controller.assign_employee(
        2000001,
        employee
    )

    assert controller.total_assigned_employees(2000001) == 1


def test_sort_by_duration(controller):
    project1 = Project(
        2000001,
        "AI Recruitment",
        12
    )

    project2 = Project(
        2000002,
        "Enterprise Workspace",
        6
    )

    controller.add_project(project1)
    controller.add_project(project2)

    result = controller.sort_by_duration()

    assert result[0] == project2


def test_sort_by_title(controller):
    project1 = Project(
        2000001,
        "Zebra Project",
        6
    )

    project2 = Project(
        2000002,
        "AI Recruitment",
        8
    )

    controller.add_project(project1)
    controller.add_project(project2)

    result = controller.sort_by_title()

    assert result[0] == project2


def test_get_all_projects(controller):
    project1 = Project(
        2000001,
        "Project A",
        6
    )

    project2 = Project(
        202,
        "Project B",
        12
    )

    controller.add_project(project1)
    controller.add_project(project2)

    result = controller.get_all_projects()

    assert len(result) == 2