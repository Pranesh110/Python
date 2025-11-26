#List
# Sequence and Mutable(can change value)

#can do list slicing

a=[1,2,3,4,5]
print(a)
print(type(a))
a[1]=33  #change value
print(a)

#slicing

print(a[0]) #we  can get value from that list
print(a[0:2])
print(a[::-1])
print(a[:-1])

#we can store string value and int value and float value inside list

n=[1,True,2.5,"RAM"]
print(n)
print(type(n))
print(type(n[0]))
print(type(n[1]))
print(type(n[2]))
print(type(n[3]))

#can do nested list
test=[2,3,[33,44],5]
print(type(test[2]))
#to get value in nested list
print(test[2][1])

#----------------------------------------------------

#list Function

a=["ram","shayam","jam"]
print(a)
#.clear() #to clear value is var
print(a)

n=['test']
b=n.copy() # to copy value from a to b
print(b)


print(a.count("ram"))  # to count how many times the value occur in list

# to find first occurence of value in index
print(a.index("jam"))

#to find length of the list
print(len(a))


# to find highest value and lowest value in list
print(max(a))
print(min(a))


b=[1,2,3,4,5,6,6,6,7,8]
print(b)
# to remove value in list base on INDEX use POP
# to remove value in list based on value use remove but only first occurence

b.pop(1)
b.remove(6)
print(b)

#to add value in the list use append
name=['test','joke']
name.append('ram')
print(name)

#  to extend value with another var
joke=[1,2]
dad=[67,77]

joke.extend(dad)
print(joke)

# to insert a value in particular index

jim=[22,33,44,55]
jim.insert(1,89)
print(jim)

# to sort by asscending
v=[22,54,3,41]
v.sort()
print(v)

# to do reverse sort

f=[2,4,3,1,11,4]
f.sort(reverse=True)
print(f)

# to sort the word by length

name=["raeee","jjjj","testre"]
name.sort(key=len)
print(name)