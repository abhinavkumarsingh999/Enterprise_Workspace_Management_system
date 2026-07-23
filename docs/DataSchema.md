# Data Schema Dicumentation

## Project Overview
This project demonstrate object-oriented data schema modeling for an enterprise workspace scaffolding.

It defines business entities such as Company, Department, Employee, and Project using Python classes with constructors, properties, validation and relationships.

# Project Structure
```
src/
|
|_models/
|   |_base.py
|   |_company.py
|   |_department.py
|   |_employee.py
|   |_project.py
|
|_validation/
|   |_validators.py
```

# Class Descriptions

## Base Entity

Parent class for all business entities.

### Attributes

- entity_id

### Responsibilities

- Stores a unique identifier
- Provides a common string representation

## Employee

Represents an employee in the organization.

### Attributes

|-------------------|------------------------------------|
| Attribute         |       Description                  |
|-------------------|------------------------------------|
|employee_id        |a unique ID assign to each employee |
|name               |name of an employee                 |
|age                |age of the employee                 |
|position           |position of employee in company     |
|department         |working field of employee           |
|designation        |address of employee                 |
|salary             |salary of employee per month        |
|-------------------|------------------------------------|


## Validation

- Name cannot be empty
- Age must be at least 18
- Salary must be greater than zero

## Department

represents a company department.

### Attributes

|-------------------|-----------------------------------------------|
| Attribute         |       Description                             |
|-------------------|-----------------------------------------------|
|department_id      |a unique ID assign to each department          |
|department_name    |name of department                             |
|employees          |list of employees working in that department   |
|-------------------|-----------------------------------------------|

### Methods
 - add_employee()
 - remove_employee()

## Project

Represent a company project.

### Attributes

|----------------|--------------------------------------------|
| Attribute      |       Description                          |
|----------------|--------------------------------------------|
|project_id      |a unique ID assign to each department       |
|title           |name of department                          |
|duration        |time taken to build the project             |
|employees       |list of employees working in the project    |
|----------------|--------------------------------------------|

### Methods
 - assign_employee()


## Company

Represents an organization.

### Attributes

|-------------------|---------------------------------------|
| Attribute         |       Description                     |
|-------------------|---------------------------------------|
|company_name       |name of company/organization           |
|departments        |list of department in the compny       |
|projects           |list of projects made by the company   |
|-------------------|---------------------------------------|

### Mathods
 - add_department()
 - add_project()


# Entity Reltionship

```
Company
    |___Department
    |       |_Employee
    |       |_Employee
    |       |_Employee
    |
    |___Projects
            |_Employee
            |_Employee
            |_Employee
```

# Validation Rules

|-------------------|--------------------------------------|
| Field             |       Description                    |
|-------------------|--------------------------------------|
|Name               |cannot be empty                       |
|Age                |must be at least 18 years old         |
|department Name    |cannot be empty                       |
|Project Title      |cannot be empty                       |
|Duration           |must be postive and not have decimals |
|Salary             |must be greater than zero             |
|-------------------|--------------------------------------|


# Example Usage

```python
company = Company("InternQ")

department = Department(1009, "Artificial Intelligence")

employee = Employee(
    101,
    "Abhinav Kumar Singh",
    21,
    "AI Engineer",
    "Artificial Intelligence",
    "Greater Noida",
    60000
)

department.add_employee(employee)

company.add_department(department)
```

---

# Testing

The project includes unit tests in:

```
tests/test_schema.py
```

The tests verify:

- Employee creation
- Department creation
- Project assignment
- Company relationships
- Validation rules

---

# Technologies Used

- Python 3.12
- Object-Oriented Programming (OOP)
- Pytest
- Modular Project Structure

---

# Learning Outcomes

This project demonstrates:

- Object-Oriented Programming
- Data Schema Modeling
- Class Relationships
- Constructors
- Encapsulation
- Properties
- Validation
- Unit Testing
- Modular Software Design
