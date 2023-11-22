print("Static method in python")

class Student:
    def __init__(self,name):
        self.name = name

    def showName(self):
        return self.name    

    @staticmethod
    def defaultName():
        return "emmanuel"

student = Student("my name")

# print(student.name) #that is worke

# call static method

# print(student.defaultName()) #also working