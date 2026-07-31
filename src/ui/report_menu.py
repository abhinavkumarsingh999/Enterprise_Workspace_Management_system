from src.controllers.company_controller import CompanyController


def report_menu(controller: CompanyController):

    while True:

        print("REPORTS")

        print("1. Company Report")
        print("2. List All Departments")
        print("3. List All Projects")
        print("4. Total Employees")
        print("5. Total Departments")
        print("6. Total Projects")
        print("7. Employees In Project")
        print("8. Departments In Project")
        print("9. Back")

        choice = input("\nEnter Choice : ")

        try:

            if choice == "1":

                print("\n========== COMPANY REPORT ==========\n")

                return controller.company_report()

            elif choice == "2":

                print("\n========== DEPARTMENTS ==========\n")

                departments = controller.list_all_departments()

                if departments:

                    for department in departments:
                        print(department)

                else:

                    print("No departments available.")

            elif choice == "3":

                print("\n========== PROJECTS ==========\n")

                projects = controller.list_all_projects()

                if projects:

                    for project in projects:
                        print(project)

                else:

                    print("No projects available.")

            elif choice == "4":

                print(
                    "\nTotal Employees :",
                    controller.total_employees()
                )

            elif choice == "5":

                print(
                    "\nTotal Departments :",
                    controller.total_departments()
                )

            elif choice == "6":

                print(
                    "\nTotal Projects :",
                    controller.total_projects()
                )

            elif choice == "7":

                project_id = int(
                    input("Project ID : ")
                )

                total = controller.total_employees_in_project(
                    project_id
                )

                print(
                    "\nEmployees In Project :",
                    total
                )

            elif choice == "8":

                project_id = int(
                    input("Project ID : ")
                )

                total = controller.total_departments_in_project(
                    project_id
                )

                print(
                    "\nDepartments In Project :",
                    total
                )

            elif choice == "9":

                break

            else:

                print("\nInvalid Choice.")

        except Exception as error:

            print("\nError :", error)

        input("\nPress Enter to continue...")