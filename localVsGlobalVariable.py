print('localVsGlobalVariable.py')

x = "global variable x"

# def myFunction():
#     y = "local variable in function y"
#     x = "try to change value of x in function"
#     print(y,end="\n")
#     print(x,end="\n")
# change  globle variable value
def myFunction():
    y = "local variable in function y"
    global x
    x = "changed value of x in function"
    print(y,end="\n")
    print(x,end="\n")


print(x)
myFunction()    
print(x)