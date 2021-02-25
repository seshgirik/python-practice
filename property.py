class Employee:

    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        self.email = self.firstname + '.' + self.lastname + '@' + 'gmail.com'

    @property
    def set_email(self):
        return self.firstname + '.' + self.lastname + '@' + 'gmail.com'

    @property
    def fullname(self):
        return self.firstname + self.lastname

    @fullname.setter
    def fullname(self, name):
        self.firstname, self.lastname = name.split(' ')
        # return self.set_fullname

    @fullname.deleter
    def fullname(self):
        self.firstname = None
        self.lastname = None


rama = Employee(firstname='rama',lastname='krishna')
# rama.email = "seshgirik@gmail.com"
print(rama.email)
print(rama.fullname)

rama.firstname = 'sita'
print(rama.email)
print(rama.set_email)
rama.fullname = 'sita rama'
print(rama.fullname)
