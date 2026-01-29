import csv

class EmpManager:
    def __init__(self):
        self.file = "employees.csv"
        self.data = {} # dictionary to hold emps
        self.load()

    # read from csv file
    def load(self):
        try:
            with open(self.file, "r") as f:
                read = csv.DictReader(f)
                for row in read:
                    self.data[row["ID"]] = row
        except FileNotFoundError:
            pass    

    # save data to file
    def save(self):
        with open(self.file, "w", newline="") as f:
            heads = ["ID", "Name", "Position", "Salary", "Email"]
            write = csv.DictWriter(f, fieldnames=heads)
            write.writeheader()
            for row in self.data.values():
                write.writerow(row)

    def get_id(self, is_new=True):
        while True:
            emp_id = input("enter id: ")
            if not emp_id.isdigit():
                print("must be number")
            elif is_new and emp_id in self.data:
                print("id already there")
            elif not is_new and emp_id not in self.data:
                print("not found")
            else:
                return emp_id

    def get_name(self, name):
        while True:
            val = input(f"enter {name}: ")
            if not val.replace(" ", "").isalpha():
                print("invalid name")
            else:
                return val
            

    def get_sal(self):
        while True:
            val = input("enter salary: ")
            try:
                return float(val)
            except:
                print("invalid salary")

    def get_email(self):
        while True:
            email = input("enter email: ")
            if "@gmail.com" not in email:
                print("invalid email")
            else:
                return email
         
            
    # main functions
    def add(self):
        id = self.get_id(is_new=True)
        name = self.get_name("name")
        pos = self.get_name("position")
        sal = self.get_sal()
        mail = self.get_email()

        self.data[id] = {"ID":id, "Name":name, "Position":pos, "Salary":sal, "Email":mail}
        self.save()
        print("done.")

    def view(self):
        if not self.data:
            print("empty list.")
            return
        print("-" * 30)
        for emp in self.data.values():
            print(f"ID: {emp['ID']} | Name: {emp['Name']} | Pos: {emp['Position']} | Sal: {emp['Salary']}| Email: {emp['Email']}")
        print("-" * 30)
    
    def search(self):
        id = self.get_id(is_new=False)
        emp = self.data[id]
        print(f"ID: {emp['ID']} | Name: {emp['Name']} | Pos: {emp['Position']} | Sal: {emp['Salary']}| Email: {emp['Email']}")

    def update(self):
        id = self.get_id(is_new=False)
        emp = self.data[id]

        name = input(f"new name ({emp['Name']}): ")
        pos = input(f"new position ({emp['Position']}): ")
        sal = input(f"new salary ({emp['Salary']}): ")
        email = input(f"new email ({emp['Email']}): ")

        if name: emp["Name"] = name
        if pos: emp["Position"] = pos
        if sal:
             emp["Salary"] = float(sal)
        if email: emp["Email"] = email
        self.save()
        print("updated.")

    def delete(self):
        id = self.get_id(is_new=False)
        del self.data[id]
        self.save()
        print("deleted.")

# start
if __name__ == "__main__":
    app = EmpManager()
    while True:
        print("\n1.Add \n2.View \n3.Update \n4.Delete \n5.Search \n6.Exit")
        choose   = input("choose: ")
        if choose == "1": app.add()
        elif choose == "2": app.view()
        elif choose == "3": app.update()
        elif choose == "4": app.delete()
        elif choose == "5": app.search()
        elif choose == "6": break
        else: print("wrong choice")