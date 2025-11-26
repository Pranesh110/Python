# while loop
# number of looping is unknown
'''
i=0
while i==0:   #first loop i=0 is true so it will print
    print(i)
    i=1;     #for secn loop i=1 it will check condition it is false so loop will stop
'''
#if only ondition fail the loop will stop

#print num from 1 to 5 using while 
'''
i=1
while i<=5:
    print(i)
    i=i+1
'''    
#print the followinng number series 10,20..200
'''
i=10
while i<=200:
    print(i,end=",")
    i= i+10
'''    
#print first natural num 10 in reverse order
'''
i=10
while i<=10:
    print(i,end=",")
    if i==1:
        break;
    i= i-1
'''
#write a prog to find factorial of a number
'''
i=int(input("enter:"))
fact=1
while i>1:
    fact= fact*i
    i= i-1
print(fact)
'''  

    