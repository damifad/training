#for loop statements: executes set of stmts for every element of collection object.
#all the stmts within the for loop should follow the indentation

x=[10,20,30,40,50]
for p in x:
    print(p)

for p in x:
    print(p,end=" ")  #for putting the numbers in a vertical line


#printing a msg for multiple times
x=[10,20,30,40,50]

for p in x:
    print("good evening!!!")


#to square each element of a list

x=[10,20,30,40,50]
for p in x:
    print(p*p) #or print (p**2)


#to compute the sum of list elements
x=[10,20,30,40,50]
tot_sum=0
for p in x:
    tot_sum=tot_sum+p
print("sum=",tot_sum)

#for loop on a string
x="python"
for p in x:
    print(p)


#printing each character for 3 times
for p in x:
    print(p*3)
#printing a msg for multiple times
for p in x:
    print("good evening!!")


