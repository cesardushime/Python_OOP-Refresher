
class Employee():
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        # data unique to each instance, it's created using self
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
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'Not a working day'
        return "It's a working day"

class Developer(Employee):
    raise_amount = 1.08

    

# Employee.set_raise_amount(1.05)

dev_1 = Developer('Diego', 'Raynman', 50000)
dev_2 = Developer('Sam', 'Akhma', 34000)

# emp_str1 = 'John-Doe-70000'
# emp_str2 = 'Steve-Smith-30000'
# emp_str3 = 'Jane-Doe-90000'

# # using classmethod as an alternative constructor  
# new_emp1 = Employee.from_string(emp_str1)


print(dev_1.fullName())
print(dev_2.pay)
print(dev_1.apply_raise())
