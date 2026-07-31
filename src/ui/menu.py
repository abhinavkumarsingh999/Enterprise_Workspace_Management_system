class Menu:
    
    @staticmethod
    def clear() :
        print("\n"*3)
        
    @staticmethod
    def header() :
        print("ENTERPRISE WORKSPACE MANAGEMENT SYSTEM")
        
    @staticmethod
    def main_menu() :
        Menu.clear()
        Menu.header()
        
        print("1. Employee Management")
        print("2. Department Management")
        print("3. Project Management")
        print("4. Company Management")
        print("5. Reports")
        print("6. Exit")
        
        return input("Enter your choice: ")
    
    @staticmethod
    def invalid_choice() :
        print("\nInvalid choice. Please try again with valid choice.")
        
    @staticmethod
    def press_enter() :
        input("\nPress Enter to continue...")
        