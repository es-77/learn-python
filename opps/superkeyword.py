print("superkeyword.py")

# class Parent:
#     def showParentDetails(self):
#         print("im in parent class method")



# class ChildClass(Parent):
#     def tell(self):
#         print("child class call")


# chilClass = ChildClass()

# chilClass.showParentDetails()
class Parent:
    def __init__(self,name,id):
        self.name =name
        self.id =id

    def showParentDetails(self):
        print("im in parent class method")



class ChildClass(Parent):
    def __init__(self,name,id,lang,salary):
        super().__init__(name,id)
        self.lang =lang
        self.salary =salary

    def tell(self):
        print("child class call")


chilClass = ChildClass('emmanuel',12,'eng',120)
parentClass = Parent('emmanuel',12)

print(chilClass.name,chilClass.id,chilClass.salary,chilClass.lang)
print(parentClass.name,parentClass.id)

# chilClass.showParentDetails()
