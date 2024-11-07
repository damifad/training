#while-else: if while condition becomes false then ctrl goes back to else block

x=1
while(x<=10):
    print("hello")
    x=x+1
else:
    print("Good evening!!!")
print("end")



#while-else and break

x=1
while(x<=10):
    print("hello")
    if(x==5):
        break
        print("hi")
    x=x+1
else:
    print("Good evening!!!")
print("end") 


