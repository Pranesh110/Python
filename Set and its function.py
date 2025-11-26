# Sets and all unorderd and index DT
# comes with set([]) or {}
# if we print value it will come unorderd not in same order we valued 
# so changing the value by index is not possible as it stores the value will get change

n={1,2,3,4,"ram","jam"}
print(n)
print(type(n))

# now to add in set but cannot change

n.add('sara')
print(n)

#to add another var in one var
a={1,2,'ram'}
b={3,4}
a.update(b)
print(a)

#to remove value in set
a.remove(3) #if data is there it will remove if not it will throw error
print(a)
a.discard('Ram') # discard is for it will remove if it exsist if not it wont give any error also wont remove anything as its not there
print(a)

a.pop() #to reomb=ve the last index value but cannot know what last value is removed
# del for to delete whole value in that var


### In set Duplicate value will automatically removed 

#now SET functions like UNION,INTERSECTION,SYM diff,Difference
#union join the value
#intersection can get common value in sets
#sysdifferen not common

a={1,2,3}
b={3,4,5}
a.intersection(b)
print(a)
c=a.union(b)
print(c)
c=a.intersection(b)
print(c)
c=a.symmetric_difference(b)
print(c)

# to store in a var itself
a.intersection_update(b)
print(a)
a.symmetric_difference_update(b)
print(a)

#subset(one set data is avai in another set) and superset(all data same as another set)
c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)

