#for loop with list example
# number of looping is known


#write a program to compute the sum of first 5 natural number
'''
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)

#write program to read 10num from keyborad and find their sum and average

n=[]
for i in range(1,11):
    num=int(input("enter numbers:"))
    n.append(num)
print(n)
sum=0
for w in n:
    sum=sum+w
print("Sum is=",sum)
print("Average is=",sum/10)
'''
##### 
n=int(input("enter"))
for i in range(n+1):
    print("Number:", i, "Cube of", i, "is", i*i*i)
    

#Nested for loops
 
for i in range(1,3):
    print("Week:",i)
    for j in range(1,4):
        print("Day:",j)
    print("............")
    
    


for i in range(1,5):
    for j in range(1,i):
        print("*",end=" ")
    print("")

for i in range(1,6):
    for j in range(1,i):
        print(j,end="")
    print()
    

    
           