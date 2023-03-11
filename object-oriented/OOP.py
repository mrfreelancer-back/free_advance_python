class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = f'{self.fname}{self.lname}@gmail.com'
    
    def fullname(self):
        return f'{self.fname} {self.lname}'
    
    def increase_salary(self, margin):
        self.salary += int(self.salary * margin)
        return self.salary
    
emp1 = Employee('ali', 'barkhordar', 2000)
emp2 = Employee('alex', 'butler', 3000)

print(emp1.fullname())
print(emp2.fullname())
print(emp1.increase_salary(0.7))
print(emp2.increase_salary(0.1))