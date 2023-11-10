print("decorator in python")

def greet(fx):

    def startEndMessage(*args, **kwargs):
        print("function start")
        fx(*args, **kwargs)
        print("function end")

    return  startEndMessage

def sum(a,b):
    print(a+b) 

greet(sum)(1,3)

# def name():
#     print("Emmanuel")
    
# decorated_name = greet(name)
# decorated_name()

@greet
def name():
    print("Emmanuel")

# Invocation of the decorated function
name()