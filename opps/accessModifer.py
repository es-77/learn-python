print("Access Modifer in python")

class Student:
    def __init__(self):
        self.__name = "Emmanuel"
        self.age = 23



studend = Student()
# print(studend.name,studend.age) # its  print the value 

# check the method in class
print(studend.__dir__())

print(studend._Student__name)