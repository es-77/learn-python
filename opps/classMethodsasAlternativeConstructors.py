print("classMethodsasAlternativeConstructors.py")


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary

    @classmethod
    def fromString(cls,string):
        return cls(string.split('-')[0],string.split('-')[1])


e1 = Employee("emmanuel",1200)

print(e1.name,e1.salary)


passDataAsString = "saleem-1300"

e2 = Employee.fromString(passDataAsString)
print(e2.name,e2.salary)
