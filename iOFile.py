print("iOFile.py")

# opem and read file 

# myFile = open('hellow\mytext.txt','r')
# text = myFile.read()
# print(text)
# myFile.close()

#  create file 
# myFile = open('hellow\mytext2.txt','w')
# myFile.close()

#  write text in file
# myFile = open('hellow\mytext2.txt','w')
# myFile.write("Emmanuel is good boy")
# myFile.close()

#  append text in file
myFile = open('hellow\mytext2.txt','a')
myFile.write("\n Emmanuel is good boy")
myFile.close()