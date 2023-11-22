print("dirDict.py")

x = [1,2,3,4,5,6,7]

# print(dir(x))
# print(x.__add__)


class Person:
    def __init__(self,name,age,salary):
        self.name =name
        self.age =age
        self.salary =salary


# p =Person("emmanuel",12,1200)

# print(p.__dict__)


print(help(Person))
