#string methods

#1:upper():print in uppercase
x="hyderabad"
print(x.upper())

#2: print in lowercase
x="CHENNAI"
print(x.lower())

#3: capitalize() the first character of a string
x="india"
print(x.capitalize())

#4: title() for capitaöizing the first character of each word in a string
x="good evening hyderabad"
print(x.title())

emps= "rahul,ajay,miller,amar,james,george,blake"
print(emps.title())

#5: replace(): for replacing a portion of a string
x="Java is Easy"
print(x.replace("Java","Python"))

y="Sachin is a good batsman"
print(y.replace("Sachin","Kolin"))

#6:Swapcase()- used for converting one case to another case
x="good evening hyderabad"
print(x.swapcase())

#7: count()--to count the no of occurences of a substring or a character
x="hello hello hello....how are you?"
print(x.count("hello"))
print(x.count("h"))

data='''1.Python is simple
2.Python is user-friendly
3.Python supports interactive mode
4.Python supports 89300 modules
5.Python has many built-in libraries
'''


#8. format(): for substitutions
x="{} is the captain of Indian Team"
print(x.format("Rohith"))

y="His name is {} and he is a {}"
print(y.format("Ajay","Doctor"))
print(y.format("Dhoni","cricketer"))


z="{} is the {} of {}"
print(z.format("sachin","player","India"))
print(z.format("Modi","PM","India"))
print(z.format("Rahul","Son","Rajiv"))

w="{},{},{} are the trending technologies"
print(w.format("datascience","cybersecurity","python"))

import datetime
x="Todays date and time is: {}"
print(x.format(datetime.datetime.now()))

import math
x="square root of {} is : {}"
y=16
z=math.sqrt(y)
print(x.format(y,z))




#8. split(9: if we split a string, we get a list

x="good morning hyderabad"
#print---hyderabad
y=x.split(" ")
print(y,type(y))
print(y[2])

#to count number of words in the string(data) above
y=data.split(" ")
print(type(y))
print("No of words=",len(y))

#ex:
emp="101,Ajay,90000,Manager"
#print ----name and designation
y=emp.split(",")
print(y,type(y))
print(y[1],y[3])

#strip(): for removing the blankspaces before and after the string
x="          Good evening Hyderabad           "
print(x,len(x))

y=x.strip()
print(y,len(y))

#lstrip():removes the left most spaces
z=x.lstrip()
print(z,len(z))

#rstrip():removes the left most spaces
w=x.rstrip()
print(w,len(w))




#find(): used to check whether a sub-string is available or not
#if found, it returns the 1st character index position of the substring  else it returns to -1
x="Python is easier than java and java is faster than python"
print(x.find("Java"))
print(x.find("Python"))
print(x.find("Hadoop"))

#rfind():rightmost occurence i.e the last occurence
print(x.rfind("Java"))

#startswith()
#endswith()

x="Python is easier than Java"
print(x.startswith("Python"))
print(x.endswith("Java"))

#join():Joins the strings of a collection
emps=["Ajay","Rohith","Miller","Blake"]

#convert this list to string
y=" ".join(emps)
print(y,type(y))

z=",".join(emps)
print(z,type(z))
      

#ex
date=["26","03","2024"]

y="-".join(date)
print(y)
z="/".join(date)
print(z)


#center():will center align the string using a character, if no character is specified then by default it takes space

#syntax: string.center(length,character)
#example
x="python"
y=x.center(30)
print(y)

#ex2
x="python"
y=x.center(50)
print(y)


#ex3
x="python"
y=x.center(30,"0")
print(y)

#ex4
x="good evening hyderabad"
y=x.center(20,"@")
print(y)

#ex5
x="good evening hyderabad"
y=x.center(40,"@")
print(y)


# isalpha(): it returns true if all the characters within the strings are alphabets
x="virat kohli"
print(x.isalpha())

city="hyderabad"
print(city.isalpha())

# isdecimal():it returns true if all the characters within the strings are numeric
date="27 03 2024"
print(date.isdecimal())

pi="3.14"
print(pi.isdecimal())

#do not leave space or use underscore
accountno="345678"
print(accountno.isdecimal())

account_no="345678"
print(account_no.isdecimal())


# isalnum() : it returns if all the characters within the string are either alphabets or numeric or both

city="hyderabad"
print(city.isalnum())

account_no="345678"
print(account_no.isalnum())

Pan="phgw345678"
print(Pan.isdecimal())


#partition(): it returns a tuple of 3 strings---- before match,match, after match
#
#

cities="PUNE MUMBAI CHENNAI"
print(cities.partition("MUMBAI"))
#op results
'''
('PUNE ', 'MUMBAI', ' CHENNAI')
before     match      after match
'''


#ex
cities="PUNE CHENNAI MUMBAI"
print(cities.partition("MUMBAI"))
#op results
'''
('PUNE CHENNAI ', 'MUMBAI',    '')
before match         match   after match
'''
#ex
cities="PUNE CHENNAI MUMBAI"
print(cities.partition("DELHI"))

#op results
'''
('PUNE CHENNAI MUMBAI', '',     '')
before match           match   after match

'''





      








