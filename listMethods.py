print("list methods")

names = ["name3","name4","name1","name2","name3","name3"]
print(names)
# appendValue = input("Enter name")
# if(len(appendValue) > 0):
#     names.append(appendValue)
#     print("value append ",names,end="\n")
# print("names")

# print(names.sort())
# print(names)
# print(names.sort(reverse=True))
# print(names)
# names.reverse()
# print(names)

# print(names.index("name3"))
# print(names.count("name3"))

copyName = names.copy()
# copyName[0] = "change value"
# print(copyName,end="\n")
# copyName.insert(0,123)
# print(copyName,end="\n")

newList = [1,2,3,4,5,6,7]
names.extend(newList)
print(names,end="\n")

