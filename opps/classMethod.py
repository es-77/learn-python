print("classMethod.py")


class Employee:
    companyName = "apple"
    def show(self):
        print(f"the company name is {self.companyName}")

    def changeCompanyName(cls,newCompanyName):
        cls.companyName = newCompanyName
        # fixchange this
    @classmethod
    def changeCompanyName(cls,newCompanyName):
        cls.companyName = newCompanyName


employee = Employee()

employee.show()

employee1 = Employee()
employee1.changeCompanyName("my company")
print(Employee.companyName)
