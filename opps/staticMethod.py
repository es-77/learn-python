print("static method in pythod")


class Math:
    def __init__(self,num):
        self.num =num

    def addtonum(self,n):
        self.num = self.num +n

    @staticmethod
    def add(a,b):
        return a+b


# a = Math(1)
# print(a.num)
# a.addtonum(12)
# print(a.num)
# print(a.add(1,2))
print(Math.add(1,2))

