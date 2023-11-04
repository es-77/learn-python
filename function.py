print("function ")
def sum(value1,value2):
    return value1+value2

def tableWrite(tableNameInt):
    i=1
    while(i <= 10):
        print(tableNameInt ,"x", i ,"=", tableNameInt*i,"\n")
        i = i+1

# print(sum(12,12),end="\n")    
# print(sum(12,13),end="\n")    
# print(sum(12,14),end="\n")    
tableName = int(input("Enter table 2,3,4 one value"))
tableWrite(tableName)