from src.controllers.company_controller import CompanyController
from src.models.company import Company
from src.models.department import Department
from src.models.employee import Employee
from src.models.project import Project


company = Company(
    10001,
    "Enterprise Workspace"
)

controller = CompanyController(company)


def company_menu():

    while True:

        print("COMPANY MANAGEMENT")

        print("1. Add Department")
        print("2. Remove Department")
        print("3. Find Department")

        print("4. Add Employee")
        print("5. Remove Employee")
        print("6. Find Employee")
        print("7. Search Employee By Name")

        print("8. Add Project")
        print("9. Remove Project")
        print("10. Find Project By ID")
        print("11. Assign Employee To Project")

        print("12. Total Employees")
        print("13. Total Projects")
        print("14. Total Departments")
        print("15. Total Employees In Project")
        print("16. Total Departments In Project")

        print("17. Company Report")
        print("18. List All Projects")
        print("19. List All Departments")

        print("20. Back")

        choice = input("\nEnter Choice : ")

        try:

            if choice == "1":
                #ADD DEPARTMENT

                department = Department(
                    int(input("Department ID (4 digits): ")),
                    input("Department Name : ")
                )

                controller.add_department(department)

                print("\nDepartment Added Successfully.")

            elif choice == "2":
                #REMOVE DEPARTMENT

                department_id = int(input("Department ID (4 digits): "))

                controller.remove_department(department_id)

                print("\nDepartment Removed Successfully.")

            elif choice == "3":
                #FIND DEPARTMENT

                department_id = int(input("Department ID (4 digits): "))

                print(
                    controller.find_department(department_id)
                )

            elif choice == "4":
                #ADD EMPLOYEE

                department_id = int(input("Department ID (4 digits): "))

                department = controller.find_department(
                    department_id
                )

                employee = Employee(
                    int(input("Employee ID (6 digits): ")),
                    input("Name : "),
                    int(input("Age : ")),
                    input("Designation : "),
                    department,
                    input("Position : "),
                    float(input("Salary : "))
                )

                controller.add_employee(
                    department_id,
                    employee
                )

                print("\nEmployee Added Successfully.")

            elif choice == "5":
                #REMOVE EMPLOYEE

                employee_id = int(input("Employee ID (6 digits): "))

                controller.remove_employee(employee_id)

                print("\nEmployee Removed Successfully.")

            elif choice == "6":
                #FIND EMPLOYEE

                employee_id = int(input("Employee ID (6 digits): "))

                print(
                    controller.find_employee(employee_id)
                )

            elif choice == "7":
                #SEARCH EMPLOYEE BY NAME

                name = input("Employee Name : ")

                print(
                    controller.search_employee_by_name(name)
                )

            elif choice == "8":
                #ADD PROJECT

                project = Project(
                    int(input("Project ID (7 digits): ")),
                    input("Project Title : "),
                    int(input("Project Duration : "))
                )

                controller.add_project(project)

                print("\nProject Added Successfully.")

            elif choice == "9":
                #REMOVE PROJECT

                project_id = int(input("Project ID (7 digits): "))

                controller.remove_project(project_id)

                print("\nProject Removed Successfully.")

            elif choice == "10":
                #FIND PROJECT BY ID

                project_id = int(input("Project ID (7 digits): "))

                print(
                    controller.find_project_by_id(project_id)
                )

            elif choice == "11":
                #ASSIGN EMPLOYEES TO PROJECT

                project_id = int(input("Project ID (7 digits): "))
                employee_id = int(input("Employee ID (6 digits): "))

                employee = controller.find_employee(employee_id)

                controller.assign_employee_to_project(
                    project_id,
                    employee
                )

                print("\nEmployee Assigned Successfully.")

            elif choice == "12":
                #TOTAL EMPLOYEES

                print(
                    "\nTotal Employees :",
                    controller.total_employees()
                )

            elif choice == "13":
                #TOTAL PROJECTS

                print(
                    "\nTotal Projects :",
                    controller.total_projects()
                )

            elif choice == "14":
                #TOTAL DEPARTMENTS

                print(
                    "\nTotal Departments :",
                    controller.total_departments()
                )

            elif choice == "15":
                #TOTAL EMPLOYEES IN PROJECT

                project_id = int(input("Project ID (7 digits): "))

                print(
                    controller.total_employees_in_project(
                        project_id
                    )
                )

            elif choice == "16":
                #TOTAL DEPARTMENTS IN PROJECT

                project_id = int(input("Project ID (7 digits): "))

                print(
                    controller.total_departments_in_project(
                        project_id
                    )
                )

            elif choice == "17":
                #COMPANY REPORT

                return controller.company_report()


            elif choice == "18":
                #LIST ALL PROJECTS

                projects = controller.list_all_projects()

                print()

                for project in projects:
                    print(project)

            elif choice == "19":
                #LIST ALL DEPARTMENTS

                departments = controller.list_all_departments()

                print()

                for department in departments:
                    print(department)

            elif choice == "20":
                #BACK

                break

            else:

                print("\nInvalid Choice.")

        except Exception as error:

            print("\nError :", error)

        input("\nPress Enter to continue...")