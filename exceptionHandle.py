print('exception handle')

# inputValue = input('enter the number:')
# try:
#     i = 1
#     for i in range(10):
#         print(f"{inputValue} x {i +1} = {(int(inputValue) * (i+1))}")
# except Exception as e:
#     print(e)        

# print('end program')    

# input wrong enter through error

try:
    num = int(input('Enter a number :'))
    print("you enter a number : ",num)
except:
    print("enter wrong number")

print("program end")