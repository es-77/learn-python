print("fileLineRead")

myFile = open('hellow\mytext2.txt','r')

while True:
    fileLine = myFile.readline()
    print(fileLine)
    if not fileLine:
        break
