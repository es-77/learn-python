print("getter and setter python")

class valueNum:
    def __init__(self,value):
        self.value = value

    def show(self):
        return f"the value of value {self.value}" 

    @property
    def showValue(self):
        return self.value
        
    @showValue.setter
    def setShowValue(self,setValue):
        self.value = setValue    

number = valueNum(123)
number.setShowValue = 100
print(number.show(),number.showValue)
