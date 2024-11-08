class Employee():
    
    num_of_emps = 0
    raise_amount = 1.1
    
    def __init__(self, first, last, pay):
        # data unique to each instance, created using self
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"
        
        Employee.num_of_emps += 1
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    # class variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # Access class variable by either class or instance of the class (self)
        return self.pay

emp_1 = Employee('Diego', 'Raynman', 50000)
emp_2 = Employee('Sam', 'Akhma', 34000)



print(f'{emp_1.fullName()} got a raise from {emp_1.pay} to {emp_1.apply_raise()}')
print(f'{emp_2.fullName()} got a raise from {emp_2.pay} to {emp_2.apply_raise()}')

print("There are", Employee.num_of_emps, 'employees')
print(f"Total Pays for {Employee.num_of_emps} employees is {(emp_1.apply_raise() + emp_2.apply_raise()): ,}")