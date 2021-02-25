
class Employee:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def emp_raise(self, raiseval):
        self.raiseval = raiseval


class Developer(Employee):
    def __init__(self,fname, lname , age , lang):
        super().__init__(fname, lname, age)
        self.lang = lang


class Manager(Employee):

    def __init__(self, fname, lname, age, emplist=None):
        super().__init__(fname, lname, age)
        self.report_emplist = emplist or []

    def add_emp(self, emp):
        if emp not in self.report_emplist:
            self.report_emplist.append(emp)
            # print(self.report_emplist)
            print(f'added ')

    def remove_emp(self, emp):
        if emp in self.report_emplist:
            self.report_emplist.remove(emp)

    def reporting_emps(self):
        # print(self.report_emplist)
        for emp in self.report_emplist:
            print(f'emp name is {emp.fname}')


dev1 = Developer('rama', 'krishna', 30, 'python')
dev2 = Developer('sita', 'ram', 30, 'java')

print(dev1.lang)

manager1 = Manager('laxman', 'rao', 40, None)
print(manager1.reporting_emps())
manager1.add_emp(dev1)
manager1.add_emp(dev2)

manager1.reporting_emps()
manager1.remove_emp(dev2)
manager1.reporting_emps()

print(isinstance(manager1, Employee))
print(isinstance(manager1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))