from src.controllers.project_controller import ProjectController
from src.models.project import Project
from src.models.employee import Employee
from src.models.department import Department


controller = ProjectController()


def project_menu():

    while True:

        print("PROJECT MANAGEMENT")

        print("1. Create Project")
        print("2. Remove Project")
        print("3. Find Project By ID")
        print("4. Assign Employee")
        print("5. Remove Employee")
        print("6. Update Project Title")
        print("7. Update Project Duration")
        print("8. Total Employees")
        print("9. Total Departments")
        print("10. Display All Projects")
        print("11. Back")

        choice = input("\nEnter Choice : ")

        try:

            if choice == "1":
                #CREATE PROJECT

                project = Project(
                    int(input("Project ID (7 digits): ")),
                    input("Project Title : "),
                    int(input("Duration (Months) : "))
                )

                controller.add_project(project)

                print("\nProject Created Successfully.")

            elif choice == "2":
                #REMOVE PROJECT

                project_id = int(input("Project ID (7 digits): "))

                controller.remove_project(project_id)

                print("\nProject Removed Successfully.")

            elif choice == "3":
                #FIND PROJECT BY ID

                project_id = int(input("Project ID (7 digits): "))

                project = controller.find_project_by_id(
                    project_id
                )

                print(project)

            elif choice == "4":
                #ASSIGN EMPLOYEE

                project_id = int(input("Project ID (7 digits): "))

                department = Department(
                    int(input("Department ID (4 digits): ")),
                    input("Department Name : ")
                )

                employee = Employee(
                    int(input("Employee ID (6 digits): ")),
                    input("Employee Name : "),
                    int(input("Age : ")),
                    input("Designation : "),
                    department,
                    input("Position : "),
                    float(input("Salary : "))
                )

                controller.assign_employee(
                    project_id,
                    employee
                )

                print("\nEmployee Assigned Successfully.")

            elif choice == "5":
                #REMOVE EMPLOYEE

                project_id = int(input("Project ID (7 digits): "))
                employee_id = int(input("Employee ID (6 digits): "))

                controller.remove_employee(
                    project_id,
                    employee_id
                )

                print("\nEmployee Removed Successfully.")

            elif choice == "6":
                #UPDATE PROJECT TITLE

                project_id = int(input("Project ID (7 digits): "))
                title = input("New Project Title : ")

                controller.update_project_title(
                    project_id,
                    title
                )

                print("\nProject Title Updated.")

            elif choice == "7":
                #UPDATE PROJECT DURATION

                project_id = int(input("Project ID (7 digits): "))
                duration = int(input("New Duration : "))

                controller.update_project_duration(
                    project_id,
                    duration
                )

                print("\nProject Duration Updated.")

            elif choice == "8":
                #TOTAL EMPLOYEES

                project_id = int(input("Project ID (7 digits): "))

                total = controller.total_employees(
                    project_id
                )

                print("\nTotal Employees :", total)

            elif choice == "9":
                #TOTAL DEPARTMENTS

                project_id = int(input("Project ID (7 digits): "))

                total = controller.total_departments(
                    project_id
                )

                print("\nTotal Departments :", total)

            elif choice == "10":
                #DISPLAY ALL PROJECTS

                projects = controller.get_all_projects()

                print()

                for project in projects:
                    print(project)

            elif choice == "11":
                #BACK

                break

            else:

                print("\nInvalid Choice.")

        except Exception as error:

            print("\nError :", error)

        input("\nPress Enter to continue...")