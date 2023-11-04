print( "match case statment")

inputValue = int(input("Enter number"))

match inputValue:
    case 0:
        print("value 0")
    case 1:
        print("value 0")
    case 2:
        print("value 2")
    case 3:
        print("value 3")
    case _:
        print("default value :",inputValue)


