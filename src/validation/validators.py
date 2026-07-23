def validate_name(name: str) :
    # Validation of person's or company's name
    if not isinstance(name, str) :
        raise ValueError("Name must be string.")
    
    if not name.strip() :
        raise ValueError("name cannot be empty.")
    
    return True


def validate_age(age: int) :
    #Validation of employe age
    if not isinstance(age, int) :
        raise ValueError("Age nust be an integer and not have decimal")
    
    if age < 18 :
        raise ValueError("Employee's age must be at least 18 years old.")
    
    return True

def validate_salary(salary: float) :
    # Validation of employee salary
    if salary <= 0 :
        raise ValueError("Salary cannot be negative or zero.")
    
    return True

def validate_department(name: str) :
    # Validation of department name
    if not name.strip() :
        raise ValueError("Departmen name cannot be empty.")
    
    return True

def validate_project_title(title: str) :
    # Validation of project title
    if not title.strip() :
        raise ValueError("Project's title cannot be empty.")
    return True

def validate_duration(duration: str) :
    # Validation project duration
    if duration < 0 :
        raise ValueError("Duration must be greater than zero.")
    
    return True