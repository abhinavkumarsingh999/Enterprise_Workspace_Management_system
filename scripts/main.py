from src.ui.menu import Menu
from src.ui.employee_menu import employee_menu
from src.ui.department_menu import department_menu
from src.ui.project_menu import project_menu
from src.ui.company_menu import company_menu
from src.ui.report_menu import report_menu

from src.models.company import Company
from src.controllers.company_controller import CompanyController

company = Company(
    10001,
    "Enterprise Workspace"
)

company_controller = CompanyController(company)

def main() :
    while True:
        
        choice = Menu.main_menu()
        
        if choice == "1" :
            employee_menu()
            
        elif choice == "2" :
            department_menu()
            
        elif choice == "3" :
            project_menu()
            
        elif choice == "4" :
            company_menu()
            
        elif choice == "5" :
            report_menu(company_controller)
            
        elif choice == "6" :
            print("Thanks for using Enterprise Workspace Management System.")
            break
        
        else :
            Menu.invalid()
            Menu.press_enter()
            

if __name__ == "__main__" :
    main()
            