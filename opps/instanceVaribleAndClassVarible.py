print("instanceVaribleAndClassVarible.py")

class Employee:
    company = "apple"
    def __init__(self,name):
        self.name = name
        self.raise_ammount = 12

    def showDetails(self):
        print(f"the employee name is {self.name} and the company name is {self.company}")



employee = Employee('emmanuel')

employee.showDetails()

employee1 = Employee('saleem')
employee1.company = 'apple pak'

employee1.showDetails()
