print("doc string")

def square(value=1):
    ''' this is the function doc string 
    '''
    return value**2
print(square(2))     
print(square.__doc__)        