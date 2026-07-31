from src.controllers.employee_controller import EmployeeController
from src.models.employee import Employee
from src.models.department import Department

controller = EmployeeController()


def employee_menu() :
    
    while True :
        
        print("EMPLOYEE MANAGEMENT")
        
        print("1. Add Employee")
        print("2. Update Designation")
        print("3. Update Department")
        print("4. Update Position")
        print("5. Remove Employee")
        print("6. Search Employee by ID")
        print("7. Search Employee by Name")
        print("8. Search Employee by Designation")
        print("9. Display All Employees")
        print("10. Sort by Employee ID")
        print("11. Sort by Name")
        print("12. Sort by Salary")
        print("13. Back")
        
        
        choice = input("\nEnter your choice : ")
        
        try :
            if choice == "1" :
                #ADD EMPLOYEE
                employee_id = int(input("Enter Employee ID (6 digits) : "))
                name = input("Enter employee's name : ")
                age = int(input("Enter employee's age : "))
                designation = input("Enter address : ")
                
                department_id = int(input("Department ID( four digit) : "))
                department_name = input("Department name : ")
                
                department = Department(
                    department_id, department_name
                )
                
                position = input("Position : ")
                salary = float(input("Salary : "))
                
                employee = Employee(
                    employee_id, 
                    name, 
                    age, 
                    position, 
                    department, 
                    designation, 
                    salary
                )
                
                controller.add_employee(employee)
                
                print("\nEmployee added successfully.")
                
            elif choice == "2" :
                #UPDATE DESIGNATION
                
                employee_id = int(input("Enter Employee ID (6 digits): "))
                designation = input("Enter address : ")
                
                controller.update_designation(
                    employee_id,
                    designation
                )
                
                print("\nDesignation updated successfully.")
                
            elif choice == "3" :
                #UPDATE DEPARTMENT
                employee_id = int(input("Employee ID : (6 digits)"))

                department_id = int(input("Department ID (4 digits): "))
                department_name = input("Department Name : ")

                department = Department(
                    department_id,
                    department_name
                )

                controller.update_department(
                    employee_id,
                    department
                )

                print("\nDepartment updated successfully.")
                
            elif choice == "4" :
                #UPDATE POSITION
                employee_id = int(input("Employee ID (6 digits): "))
                position = input("New Position : ")

                controller.update_position(
                    employee_id,
                    position
                )

                print("\nPosition updated successfully.")

            elif choice == "5":
                #REMOVE EMPLOYEE

                employee_id = int(input("Employee ID (6 digits): "))

                confirm = input(
                    "Delete Employee? (Y/N): "
                ).upper()

                if confirm == "Y":

                    controller.remove_employee(employee_id)

                    print("\nEmployee removed successfully.")
                    
            elif choice == "6" :
                #SEARCH EMPLOYEE BY EMPLOYEE ID
                employee_id = int(input("Employee ID (6 digits): "))

                employee = controller.find_employee_by_id(
                    employee_id
                )

                print(employee)

            elif choice == "7":
                #SEARCH EMPLOYEE BY NAME

                name = input("Employee Name : ")

                employee = controller.search_employee_by_name(
                    name
                )

                print(employee)

            elif choice == "8":
                #SEARCH EMPLOYEE BY DESIGNATION

                designation = input("Designation : ")

                employees = controller.search_by_designation(
                    designation
                )

                for employee in employees:
                    print(employee)

            elif choice == "9":
                #DISPLAY ALL EMPLOYEES
                employees = controller.get_all_employees()
                
                if not employees :
                    print("\nno employees found.")
                    
                else :
                    for employee in employees :
                        print(employee)

            elif choice == "10":
                #SORT BY EMPLOYEE ID

                employees = controller.sort_by_employee_id()

                for employee in employees:
                    print(employee)

            elif choice == "11":
                #SORT BY EMPLOYEES NAME

                employees = controller.sort_by_name()

                for employee in employees:
                    print(employee)

            elif choice == "12":
                #SORT BY EMPLOYEES SALARY

                employees = controller.sort_by_salary()

                for employee in employees:
                    print(employee)
                    
            elif choice == "13" :
                #BACK
                break
            
            else :
                print("\nInvalid choice.")
                
        except Exception as error :
            print("\nError : ",error)
            
        input("\nPress Enter to continue...")
                    
                    
                
    
    