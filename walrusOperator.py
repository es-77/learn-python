print("walrusOperator.py")

# a = True
# # a = False

# print(a:=False)
numbers = [1,2,3,4,5]

# # Use the correct condition for the while loop
# while len(numbers) > 0:
#     # Pop only once in each iteration
#     popped_number = numbers.pop()
#     print("Emmanuel", popped_number)



# while (num := len(numbers)) > 5:
#     popped_number = numbers.pop()
#     print("Emmanuel", popped_number, num)


foods = list()

# while (True):
#     food = input("Enter your food list : ")

#     if(food == "okay"):
#         break

#     foods.append(food)    


# print(foods)

while (food := input("enter your food : ")) != "okay":
    foods.append(food)


print(foods)