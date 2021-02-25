

class Employee:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Testing(Employee):
    pass


sesh = Testing('rama',10)
print(sesh.name)

print(help(Testing))
