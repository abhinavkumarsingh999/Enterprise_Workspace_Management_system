from src.models.company import Company
from src.models.department import Department
from src.models.employee import Employee
from src.models.project import Project

from src.controllers.company_controller import CompanyController
from src.controllers.employee_controller import EmployeeController
from src.controllers.department_controller import DepartmentController
from src.controllers.project_controller import ProjectController


def main():

    print(" WEEK 3 : DYNAMIC STATE ENGINES & BUSINESS LOGIC ")

    company = Company(
        10001,
        "ABC Technologies"
    )

    ai_department = Department(
        1001,
        "Artificial Intelligence"
    )

    web_department = Department(
        1002,
        "Web Development"
    )

    company_controller = CompanyController(company)
    employee_controller = EmployeeController()
    department_controller = DepartmentController()
    project_controller = ProjectController()

    company_controller.add_department(ai_department)
    company_controller.add_department(web_department)

    department_controller.add_department(ai_department)
    department_controller.add_department(web_department)

    print("\nDepartments Created Successfully")

    employee1 = Employee(
        500001,
        "Abhinav Kumar Singh",
        21,
        "AI Engineer",
        ai_department,
        "Machine Learning Engineer",
        85000
    )

    employee2 = Employee(
        500002,
        "Rahul Kumar",
        24,
        "Backend Developer",
        web_department,
        "Software Engineer",
        70000
    )

    employee3 = Employee(
        500003,
        "Amit Sharma",
        26,
        "Data Scientist",
        ai_department,
        "Senior Data Scientist",
        95000
    )

    employee_controller.add_employee(employee1)
    employee_controller.add_employee(employee2)
    employee_controller.add_employee(employee3)

    company_controller.add_employee(
        "Artificial Intelligence",
        employee1
    )

    company_controller.add_employee(
        "Web Development",
        employee2
    )

    company_controller.add_employee(
        "Artificial Intelligence",
        employee3
    )

    print("Employees Added Successfully")

    project1 = Project(
        2000001,
        "Enterprise Workspace",
        6
    )

    project2 = Project(
        2000002,
        "AI Recruitment System",
        10
    )

    project_controller.add_project(project1)
    project_controller.add_project(project2)

    company_controller.add_project(project1)
    company_controller.add_project(project2)

    print("Projects Added Successfully")

    company_controller.assign_employee_to_project(
        2000001,
        employee1
    )

    company_controller.assign_employee_to_project(
        2000001,
        employee2
    )

    company_controller.assign_employee_to_project(
        2000002,
        employee3
    )

    print("Employees Assigned To Projects")

    print("\nSearching Employee By Name")

    employee = company_controller.search_employee_by_name(
        "Abhinav Kumar Singh"
    )

    print(employee)

    print("\nSearching Project")

    print(
        project_controller.find_project_by_title(
            "Enterprise Workspace"
        )
    )

    print("\nEmployees Sorted By Salary")

    for emp in employee_controller.sort_by_salary():

        print(
            emp.name,
            emp.salary
        )

    print("\nEmployees Sorted By Employee ID")

    for emp in employee_controller.sort_by_employee_id():

        print(
            emp.entity_id,
            emp.name
        )

    print("\nAverage Salary")

    print(employee_controller.average_salary())

    print("\nHighest Salary")

    print(employee_controller.highest_salary())

    print("\nLowest Salary")

    print(employee_controller.lowest_salary())

    print("\nEmployee Summary")

    employee_controller.employee_summary()

    print("\nDepartment Summary")

    department_controller.department_summary(101)

    print("\nProject Summary")

    project_controller.project_summary()

    print("\nCompany Summary")

    company_controller.company_summary()

    print("\nList Of Departments")

    company_controller.list_all_departments()

    print("\nList Of Projects")

    company_controller.list_all_projects()

    print("\nStatistics")

    print(
        "Departments :",
        company_controller.total_departments()
    )

    print(
        "Employees :",
        company_controller.total_employees()
    )

    print(
        "Projects :",
        company_controller.total_projects()
    )

    print(
        "Employees In Project :",
        company_controller.total_employees_in_project(201)
    )

    print(
        "Departments In Project :",
        company_controller.total_departments_in_project(201)
    )

    print("\nDemo Completed Successfully")


if __name__ == "__main__":
    main()