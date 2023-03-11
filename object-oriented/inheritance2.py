class Employee:
    increase_s = 0.1
    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.salary = pay
        self.email_address = f"{first}{last}@gmail.com"
    def fullname(self):
        return f"{self.fname} {self.lname}"
    def change_inc(self, new_inc):
        self.increase_s = new_inc
    def salary_inc(self):
        self.salary += int(self.salary * self.increase_s)
        return self.salary

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print("employee already exists!")
    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print("Sorry! employee not found!!")
    def print_emp(self):
        for emp in self.employees:
            print(f"--{emp.fullname()}")

developer1 = Developer("ali", "barkhordar", 2000, "python")
developer2 = Developer("alex", "barbarian", 3000, "c++")

manager = Manager("reza", "raper", 10000)
print(manager.email_address)
manager.add_emp(developer1)
manager.add_emp(developer2)
manager.rem_emp(developer2)
manager.print_emp()

print(isinstance(developer1, Employee))
print(issubclass(Developer, Manager))
print(help(Developer))