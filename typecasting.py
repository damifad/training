

#typecasting:converting one datatype to other type
#for typecasting we have functions such as ---int(),floaat(),str(),bool()


#case1: converting a string into int
x="10"
print(x,type(x))

y=int(x)
print(y,type(y))


#ex2:hello cannot be converted into integer only numerical strings

#x="hello"
#print(x,type(x))

#y=int(x)
#print(y,type(y))


#case2: coverting a int to string

x=10
print(x,type(x))

y=str(x)
print(y,type(y))


#case 3: converting a int to float

x=10
print(x,type(x))

y=float(x)
print(y,type(y))


#case 4: convert a float into int
x=4.5
print(x,type(x))

y=int(x)
print(y,type(y))


#case5: converting a int to bool
#ex1
x=1
print(x,type(x))

y=bool(x)
print(y,type(y))

#2
x=29
print(x,type(x))

y=bool(x)
print(y,type(y))

#3
x=-7
print(x,type(x))

y=bool(x)
print(y,type(y))


#ex4
x=0.001
print(x,type(x))

y=bool(x)
print(y,type(y))



#case 6: converting a bool to int
x=True
print(x,type(x))

y=int(x)
print(y,type(x))

