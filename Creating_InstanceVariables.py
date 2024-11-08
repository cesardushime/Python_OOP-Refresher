class Employee():
    def __init__(self, first, last, pay):
        # data unique to each instance, created using self
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Diego', 'Raynman', 50000)
emp_2 = Employee('Sam', 'Akhma', 34000)


# instance variables

print(emp_1.fullName())
print(Employee.fullName(emp_2))