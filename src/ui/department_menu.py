from src.controllers.department_controller import DepartmentController
from src.models.department import Department
from src.models.employee import Employee


controller = DepartmentController()


def department_menu():

    while True:

        print("DEPARTMENT MANAGEMENT")

        print("1. Add Department")
        print("2. Remove Department")
        print("3. Find Department")
        print("4. Add Employee")
        print("5. Remove Employee")
        print("6. Total Employees")
        print("7. Average Salary")
        print("8. Highest Salary")
        print("9. Lowest Salary")
        print("10. Sort Employees by Salary")
        print("11. Sort Employees by Age")
        print("12. Department Summary")
        print("13. Display All Departments")
        print("14. Back")

        choice = input("\nEnter your choice : ")

        try:

            if choice == "1":
                # ADD DEPARTMENT

                department_id = int(input("Department ID (4 digits) : "))
                department_name = input("Department Name : ")

                department = Department(
                    department_id,
                    department_name
                )

                controller.add_department(department)

                print("\nDepartment added successfully.")

            elif choice == "2":
                #REMOVE DEPARTMENT

                department_id = int(input("Department ID (4 digits): "))

                confirm = input(
                    "Remove Department? (Y/N): "
                ).upper()

                if confirm == "Y":

                    controller.remove_department(department_id)

                    print("\nDepartment removed successfully.")

            elif choice == "3":
                #FIND DEPARTMENT

                department_id = int(input("Department ID (4 digits): "))

                department = controller.find_department_by_id(
                    department_id
                )

                print(department)

            elif choice == "4":
                #ADD EMPLOYEE TO DEPARTMENT

                department_id = int(input("Department ID (4 digits): "))

                employee = Employee(

                    int(input("Employee ID (6 digits): ")),

                    input("Employee Name : "),

                    int(input("Age : ")),

                    input("Designation : "),

                    controller.find_department_by_id(
                        department_id
                    ),

                    input("Position : "),

                    float(input("Salary : "))
                )

                controller.add_employee(
                    department_id,
                    employee
                )

                print("\nEmployee added successfully.")

            elif choice == "5":
                #REMOVE EMPLOYEE FROM DEPARTMENT

                department_id = int(input("Department ID (4 digits): "))
                employee_id = int(input("Employee ID (6 digits): "))

                controller.remove_employee(
                    department_id,
                    employee_id
                )

                print("\nEmployee removed successfully.")

            elif choice == "6":
                #TOTAL EMPLOYEE IN A DEPARTMENT

                department_id = int(input("Department ID (4 digits): "))

                total = controller.total_employees(
                    department_id
                )

                print("\nTotal Employees :", total)

            elif choice == "7":
                #AVERAGE SALARY

                department_id = int(input("Department ID (4 digits): "))

                average = controller.average_salary(
                    department_id
                )

                print("\nAverage Salary :", average)

            elif choice == "8":
                #HIGHEST SALARY

                department_id = int(input("Department ID (4 digits): "))

                employee = controller.highest_salary(
                    department_id
                )

                print("\nHighest Salary Employee")
                print(employee)

            elif choice == "9":
                #LOWEST SALARY

                department_id = int(input("Department ID (4 digits): "))

                employee = controller.lowest_salary(
                    department_id
                )

                print("\nLowest Salary Employee")
                print(employee)

            elif choice == "10":
                #SORT EMPLOYEES BY SALARY

                department_id = int(input("Department ID (4 digits): "))

                employees = controller.sort_by_salary(
                    department_id
                )

                print()

                for employee in employees:
                    print(employee)

            elif choice == "11":
                #SORT EMPLOYEES BY AGE

                department_id = int(input("Department ID (4 digits): "))

                employees = controller.sort_by_age(
                    department_id
                )

                print()

                for employee in employees:
                    print(employee)

            elif choice == "12":
                #DEPARTMENT SUMMARY

                department_id = int(input("Department ID (4 digits): "))

                summary = controller.department_summary(
                    department_id
                )

                print("\nDepartment Summary\n")

                for key, value in summary.items():
                    print(f"{key} : {value}")

            elif choice == "13":
                #DISPLAY ALL DEPARTMENT
                departments = controller.get_all_departments()
                
                if not departments :
                    print("\nNo Department found.")
                    
                else :
                    for department in departments:
                        print(department)

            elif choice == "14":
                #BACK
                break

            else:

                print("\nInvalid Choice.")

        except Exception as error:

            print("\nError :", error)

        input("\nPress Enter to continue...")