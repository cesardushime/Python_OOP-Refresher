
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

# Subclass Developer
class Developer(Employee):
    raise_amount = 1.08

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.pro_lang = prog_lang

# Subclass Manager
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees
        # Checking if 'employees' list was provided
        if self.employees is None:
            # If not, a new empty list is created for this instance
            self.employees = []
        else:
            # If provided, the passed-in list of employees is used
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())
# Employee.set_raise_amount(1.05)

dev_1 = Developer('Diego', 'Raynman', 50000, 'Python')
dev_2 = Developer('Sam', 'Akhma', 34000, 'Java')
dev_3 = Developer('Andre', 'Lore', 32000, 'Kotlin')
dev_4 = Developer('Picaris', 'Baraka', 43000, 'JavaScript')
dev_5 = Developer('Batman', 'Beloris', 35000, 'Java')

manag_1 = Manager('Cesar', 'Analyst', 50000, [dev_1, dev_2])
manag_2 = Manager('TopManager', 'Senior', 50000, [dev_1, dev_2, dev_3, dev_4])

manag_1.add_emp(dev_5)
manag_2.remove_emp(dev_1)
manag_2.remove_emp(dev_2)

print(manag_2.print_emps())

# emp_str1 = 'John-Doe-70000'
# emp_str2 = 'Steve-Smith-30000'
# emp_str3 = 'Jane-Doe-90000'

# # using classmethod as an alternative constructor  
# new_emp1 = Employee.from_string(emp_str1)


# print(dev_1.fullName())
# print(dev_1.email)
# print(dev_1.pro_lang)


