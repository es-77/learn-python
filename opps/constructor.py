print("constructor in python")

class Student:
    def __init__(self,name,last,study):
        self.name = name
        self.last = last
        self.study = study
    
    def myInfo(self):
        return f"name is {self.name} last name is {self.last} my study {self.study}"


emmanuel = Student("Emmanuel","Saleem","bs/cs")

print(emmanuel.myInfo())

moon = Student("Moon","Saleem","master")

print(moon.myInfo())
