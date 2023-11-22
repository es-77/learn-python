print('multipleInheritance.py')

class Employee:
    def __init__(self,name):
        self.name = name
    def showNameDetails(self):
        return f"the name of employee is {self.name}"


class StudentClass:
    def __init__(self,className):
        self.className = className

    def showClassDetails(self):
        return f"this the class details {self.className}"    


class EmployeeClass(Employee,StudentClass):
    def __init__(self,name,className):
        self.name = name
        self.className = className

    def fullDetails(self):
        return F"{super().showNameDetails()} and {super().showClassDetails()}"    


employeeClass = EmployeeClass("emmanuel","A")

# print(employeeClass.fullDetails())
print(EmployeeClass.mro())
