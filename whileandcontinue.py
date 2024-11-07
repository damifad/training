#continue:it skips the current iteration and continues with the next iteration

x=0
while(x<10):
    x=x+1
    if(x<=5):
        continue
        print("hi")
    print(x,"hello")
print("end")


x=0
while(x<10):
    x=x+1
    if(x==5):
        continue
        print("hi")
    print(x,"hello")
print("end")



#while break and continue
while(True):
    username=input("enter the username:")
    if(username!="vijay"):
        continue
    password=input("hello...vijay!!!...please enter your password:")
    if(password=="python"):
        break
print("login successful!!!")
