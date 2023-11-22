print("methodOverriding.py")

class Parent:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def arear(self):
        return self.x * self.y    
    def myMethod(self):
        return "my method parent"


class Child(Parent):
    def childMethod(self):
        return "child method run"

    def circleArear(self):
        return  3.14 * super().arear()   



child = Child(2,2)

print(child.arear())
print(child.circleArear())