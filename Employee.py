class EmployeeManager:
    def __init__(self, filename):
        self.filename = filename
        self.employee = []
        self.load()

    def load(self):
        try:
            with open(self.filename ,  "r") as f:
                content = f.readlines()
                header = content[0].strip().split(",")
                for values in content[1:]:
                    value = values.strip().split(",")
                    self.employee.append(dict(zip(header,value)))
        except FileNotFoundError:
            print("Failed to load file")

    def get_active(self):
        for value in self.employee:
            if value["status"] == "active":
                print(value)

    def get_by_department(self, dept):
        for emp in self.employee:
            if emp["department"] == dept:
                print(emp)

    def add_employee(self, emp):
        header = list(self.employee[0].keys())
        values = emp.split(",")
        if len(values) != len(header):
            return 
        self.employee.append(dict(zip(header,values)))

    def save(self):
         try:
            with open(self.filename ,  "w") as f:
                header = list(self.employee[0].keys())
                f.write(",".join(header) + "\n")
                for emp in self.employee:
                    f.write(",".join(emp.values()) + "\n")
         except FileNotFoundError:
            print("Failed to load file")

    def get_by_salary_range(self, min_sal, max_sal):
        for emp in self.employee:
            if min_sal <= int(emp["salary"]) <= max_sal:
                print(emp)
    def remove_employee(self, ide):
        for emp in self.employee:
            if emp["id"] == str(ide):
                self.employee.remove(emp)
                print(f"Employee with id {ide} has been removed Sucessfully")
                return
        print(f"Employee with id {ide} not found")
        
    def update_employee(self, ide, field, new_value):
        for emp in self.employee:
            if emp["id"] == str(ide):
                emp[field] = new_value
                print(f"Employee with id {ide} has been updated Sucessfully")
                return
        print(f"Employee with id {ide} has not found")