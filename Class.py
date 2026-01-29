import csv

class EmployeeManager:
    def __init__(self):
        self.filename = "employees.csv"
        self.employees = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.employees[row["ID"]] = row
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.filename, "w", newline="") as f:
            headers = ["ID", "Name", "Position", "Salary", "Email"]
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for emp in self.employees.values():
                writer.writerow(emp)

    def get_valid_id(self, new=True):
        while True:
            emp_id = input("Enter ID: ")
            if not emp_id.isdigit():
                print("ID must be a number.")
            elif new and emp_id in self.employees:
                print("ID already exists.")
            elif not new and emp_id not in self.employees:
                print("Employee not found.")
            else:
                return emp_id

    def get_valid_name(self, label):
        while True:
            value = input(f"Enter {label}: ")
            if value.replace(" ", "").isalpha():
                return value
            print(f"{label} must contain letters only.")

    def get_valid_salary(self):
        while True:
            value = input("Enter Salary: ")
            try:
                return float(value)
            except ValueError:
                print("Salary must be a number.")

    def get_valid_email(self):
        while True:
            email = input("Enter Email: ")
            if "@gmail.com" in email:
                return email
            print("Invalid email.")

    def add_employee(self):
        print("\nAdd Employee")

        emp_id = self.get_valid_id(new=True)
        name = self.get_valid_name("Name")
        position = self.get_valid_name("Position")
        salary = self.get_valid_salary()
        email = self.get_valid_email()

        self.employees[emp_id] = {
            "ID": emp_id,
            "Name": name,
            "Position": position,
            "Salary": salary,
            "Email": email
        }

        self.save_data()
        print("Employee added.")

    def view_all(self):
        if not self.employees:
            print("No employees found.")
            return

        print("-" * 50)
        for emp in self.employees.values():
            print(f"ID: {emp['ID']} | Name: {emp['Name']} | Position: {emp['Position']} | Salary: {emp['Salary']}")
        print("-" * 50)

    def search_employee(self):
        emp_id = self.get_valid_id(new=False)
        emp = self.employees[emp_id]

        print("-" * 50)
        print(f"ID: {emp['ID']}")
        print(f"Name: {emp['Name']}")
        print(f"Position: {emp['Position']}")
        print(f"Salary: {emp['Salary']}")
        print(f"Email: {emp['Email']}")
        print("-" * 50)

    def update_employee(self):
        emp_id = self.get_valid_id(new=False)
        emp = self.employees[emp_id]

        name = input(f"New Name ({emp['Name']}): ")
        position = input(f"New Position ({emp['Position']}): ")
        salary = input(f"New Salary ({emp['Salary']}): ")
        email = input(f"New Email ({emp['Email']}): ")

        if name:
            if name.replace(" ", "").isalpha():
                emp["Name"] = name
            else:
                print("Invalid name. Keeping old value.")

        if position:
            if position.replace(" ", "").isalpha():
                emp["Position"] = position
            else:
                print("Invalid position. Keeping old value.")

        if salary:
            try:
                emp["Salary"] = float(salary)
            except ValueError:
                print("Invalid salary. Keeping old value.")

        if email:
            if "@" in email:
                emp["Email"] = email
            else:
                print("Invalid email. Keeping old value.")

        self.save_data()
        print("Employee updated.")

    def delete_employee(self):
        emp_id = self.get_valid_id(new=False)
        del self.employees[emp_id]
        self.save_data()
        print("Employee deleted.")


if __name__ == "__main__":
    manager = EmployeeManager()

    while True:
        print("\n1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.view_all()
        elif choice == "3":
            manager.update_employee()
        elif choice == "4":
            manager.delete_employee()
        elif choice == "5":
            manager.search_employee()
        elif choice == "6":
            print("Bye.")
            break
        else:
            print("Invalid choice.")
