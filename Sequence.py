# # # #squences methods

text="Hello, world!"   #string
print(len(text))

tuple=(10,20,30,40,50)  #tuple
print(len(tuple))


dictionary={"name":"pooja","age":26,"city":"UK"}
print(len(dictionary))
print(dictionary)

set={1,2,3,4,5,6,77}  #set
print(len(set))

empty=[]
print(len(empty))

nested=[[1,2,3],[78,90,76],[78,90,0]]   #nested list
print(len(nested))


#numbers
numbers=[3,4,5,6,7,8,99,22,0,200]

#min & max sequence
print(min(numbers))
print(max(numbers))
print(sum(numbers))



print(sorted(numbers))   #sort is used for sorting 
sort=["a","d","c","b"]
print(sorted(sort))


#list- specific methods
fruits=["apple","banana"]
fruits.append("grapes")    #append method adds a single element to the end of a list
print(fruits)

a=[45,2,41,89,23,45,6,41]
print(a.count(45))  #the count() method returns the number of times a specified element appears in a list.


#the index() function is used to find the position of an element in a list
python=["data_science", "data_analyst","data_engineer"]
print(python.index("data_science"))


text="hello"
print(text.upper())
print(text.lower())
print(text.capitalize())

abhi= "hello, world!"
print(abhi.strip())  #The strip() function in Python is used to remove 
#leading and trailing characters from a string
print(abhi.replace("world", "Abhilash"))


words=["Hello", "world"]
print("".join(words))
print(words)

numbers=[0,1,2,3,4,5,6,7,8,9,10]
print(numbers[1:5])


igor=["da","de","ds"]  #reversing
print(igor[::-1])

data=[10,20,30,40,50]  #omitting start or stop
print(data[:3])
print(data[:0])
print(data[:2])

abc="python"  #string
print(abc[0:5])
print(abc[-3])   #negative slicing



