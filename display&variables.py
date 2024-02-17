#----------DISPLAY / PRINT OPERATION-----------
a=10
b=20
c=30
# print in same line
print(a,b,c)

# print in different line
print(a)
print(b)
print(c)

# add seperator 
print(a,b,c,sep='@')
print(a,b,c,sep='-')


#-------------VARIABLES--------------

a=10
b=20
print(a)
print(A)
print(b) #as variable is not declared it shows "NAME ERROR"

# memory allocation in variables
a=10
b=20
print(a)
print(b)

# Assinging one variable value to another variable
   #example:1
a=100
a=b
print(a)
print(b)
   #example:2
A=22
a=A
print(a)
print(A)

# variable reinitialization
   #example:1
a=100
b=200
a=b
c=500
a=b
b=c
print(a)
print(b)
print(c)
   #example:2
a=1000
b=2000
c=3000
a=b
b=c
c=7000
e=b
f=c
a=b
b=e
f=a
print(a)
print(b)
print(c)
print(e)
print(f)
