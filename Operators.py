#comparative operators

#1.equal to(==)
#2.not equal to(!=)
#3.greater than(>)
#4.lesser than(<)
#5.greater than or equal to(>=)
#6.less than or equal to(<=)

x=5
print(x==5)

y=5
print(y!=4)

a=5
print(a>5)

b=4
print(b<8)

Abilash=8
print("")

if Abilash>10:
    print("right one!")
else:
    print("wrong one!")

meaning=40
if meaning>20:
    print("right")
else:
    print("wrong")


number=3
if number % 2==0: #modules arithmetic data type
    print("the number is even")
else:
    print("the number is odd")

score=65
if score>=90:
    print("grade A")
elif score>=80:
    print("grade B")
elif score >70:
    print("grade C")
elif score>=60:
    print("grade D")
else:
    print("grade F")


Weather ="rainy"
if Weather=="sunny":
    print("lets go to the park")
elif Weather=="rainy":
    print("lets stay indoors and read and practice python")
else:
    print("lets check the weather forecast for plans")


 

#single condition---if/else
#multiple condition---if/elif/else

###Arithmetic operator (+,-,*,/,%,//,**)
#1:Arithmetic Operators: for performing arithmetic operations such as addition, subtraction
#multiplication,division(/),floor division(//),modulo division(%),exponent(**)
#division: returns quotient with decimals and floor division does without decima

a=10
b=20
result=a-b
print("subtractions:", result)

x=4
y=3
z=x*y
print("multiplication:",z)

x=10
y=4
add=x+y
print("sum=",add)

sub=x-y
print("diff=",sub)

mul=x*y
print("prod=",mul)

dtv=x/y
print("div=",dtv)

floordiv=x//y
print("floordiv=",floordiv)

moddiv=x%y
print("moddiv=",moddiv)

exp=x**y
print("exp=",exp)

print(10/3)
print(10//3)
print(10%3)
print(round(10/3,2))



x=75.67483
print(round(x,4))
print(round(x,3))
print(round(x,2))
print(round(x,1))
print(round(x))

#artihmetic operations on int and float
print(10+3.3)
print(10-3.3)
print(10*3.3)
print(10/3.3)
print(10//3.3)
print(10%3.3)
print(10**3.3)


#arithmetic operations on float and boolean
print(4.5+True)
print(4.5-True)
print(5*True)
print(True+True)


#arithmetic operations on string and int
#print("hello"+3)
print("hello"+"3")
print("hello"+str(3))
print("hello"*3)
print(3*"hello")

pooja=10
damilola=4
igor=pooja//damilola  #// floor division which gives us integer output
print("division:", igor)

#modules
ab=10
cd=2
r=ab%cd
print("modules:",r)


#exponentiation(**)
base=2  #3*3*3*3
exponent=4
rr=base**exponent
print("exponentiation:",rr)

#artihmetic operations on int and float
print(10+3.3)
print(10-3.3)
print(10*3.3)
print(10/3.3)
print(10//3.3)
print(10%3.3)
print(10**3.3)


#arithmetic operations on float and boolean
print(4.5+True)
print(4.5-True)
print(5*True)
print(True+True)


#arithmetic operations on string and int
#print("hello"+3)
print("hello"+"3")
print("hello"+str(3))
print("hello"*3)
print(3*"hello")
