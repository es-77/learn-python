print('Finally key word')

def myFun():
    try:
        num = int(input('enter number : '))
        return 1
    except Exception as e:
        return 0
    finally:
        print("this allway run after return")        


print(myFun())    