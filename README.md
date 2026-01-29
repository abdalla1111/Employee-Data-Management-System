# Employee Data Management System

A Python command-line application (CLI) for managing employee records with CSV file persistence.

## Features
- Add employee records (ID, Name, Position, Salary, Email)
- View all employees in a readable table format
- Update employee details by ID
- Delete employee records by ID
- Search for an employee by ID
- Persistent storage using `employees.csv`
- Input validation (numeric ID & salary, alphabetic names, email format)

## Technical Details
- Implemented using a single class: `EmployeeManager`
- Uses Python dictionaries for in-memory storage
- Uses the built-in `csv` module for file handling
- Menu-driven CLI interface

## Project Structure
