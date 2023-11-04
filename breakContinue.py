print("brake continue loop")
colors = ["red","blue","green","yellow"]
for color in colors:
    if(color == "green"):
        break
    elif(color == "red"):    
        continue
    else:
        print(color,end="\n")                