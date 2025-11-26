#Tuple is immutable values cannnot be change 
# can insert any value lik int str boolean and float

# ()

a=(1,'ram',22.2,True)
print(a)
print(type(a))
#slicing
print(a[0])

print(a[-1])
print(a[0:3])
print(a[::-1])

# If want to change value in tuple make it has list and change

name=("ram","shayam")
b=list(name)
print(b)
b.append("jam")
print(b)
print(type(b)) # now its list
#then to change it has tuple
name=tuple(b)
print(name)
print(type(name))

#if it is a single value inside ()tuple means it wont take it has tuple
# so put , in the value

a=(1)
print(type(a))
b=(1,2)
print(type(b))

#Function
print(dir(b))
#len
#del to delete entire value in var
#count
print(b.count(1))
#search value where the  index is
print(b.index(1))
#to concardinate value in tuple
a=(1,2)
b=(3,4)
c=a+b
print(c)
#to make nested tuple
c=(a,b)
print(c)  #((1,2), (3,4))
print(c[0][1])




