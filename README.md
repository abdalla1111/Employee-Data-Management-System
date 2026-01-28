# Employee Data Management System

A Python CLI application to manage employee records with CSV persistence, supporting add, update, delete, search, and list operations.

## Features
- Add employee records with ID, Name, Position, Salary, and Email
- View all employees in a readable format
- Update employee details by ID
- Delete employee records by ID
- Search for an employee by ID
- Data is stored in `employees.csv` for persistence

## Technical Requirements
- Implemented using a single class `EmployeeManager`
- Uses Python dictionaries to store data in memory
- Reads/writes employee data to a CSV file
- Handles invalid input and basic validation (e.g., numeric salary)

## How to Use
1. Clone the repository:
```bash
git clone https://github.com/yourusername/employee-data-management.git
cd employee-data-management
TEST