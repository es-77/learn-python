print("inherienance in python")

class A:
    def name(self):
        return "class a"

class B(A):
    def details(self):
        return "my class b" 

a = A()
print(a.name())
b = B()
print(b.name()) 
print(b.details()) 
