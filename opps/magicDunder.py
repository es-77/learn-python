print("magicDunder.py")

class Person:
    def __init__(self,name):
        self.name = name

    # def __myNameLen__(self):
    #     i=0
    #     for i in self.name:
    #         i = i+1  
    #     return i  

    def __len__(self):
        i = 0
        for key in self.name:
            i = i + 1
        return i
    def __str__(self):
        return f"this is object of {self.name}"

    def __repr__(self):
        return f"if uper str not defin this will run {self.name}"
    def __call__(self):
        return f"call method run {self.name}"        


# person = Person('name')
# # print(len(person))
person = Person('name')
print(person)

person1 = Person('Emmanuel')
print(person1)
print(repr(person1))
print(person1())