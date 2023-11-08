print("mapFilterReducer.py")

def cub(x):
    return x * x * x


listNum = [1,2,3,4,5,6,7,8,9]

# map
# numCubs =  list(map(cub,listNum))
# print(numCubs) 

# def greterNum(num):
#     return num > 2

# # filter
# numCubs =  list(filter(greterNum,listNum))
# print(numCubs) 


# reducer 
from functools import reduce
def sumFun(x,y):
    return x+y


sumNum = reduce(sumFun,listNum)

print(sumNum)
