 # Looping a work that will done repeatedly

#for and while loop

#while loop

#syntax while condition:
    #print
    #do  this next
'''   
i=1
while i<=10:
    print(i)
    i+=1
'''  
# continue in while is used to make the loop continue

n=2
while n <= 10:
    if n%2 == 0:
        n = n+1
        continue;
    print(n)
    n += 1

#Break statement Break the ongoin loop if condition not match

i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1

# Range ()
#if we give range lik from here to there(1-5) it will give the output
a=list(range(2,5)) #(5) 0,1,2,3,4 not 5 coz n-1 , (2,5) 2,3,4  
print(a)

# also has syntax (from value,des value,how to increment)
print(list(range(2,20,2)))

#----------------------------

# FOR loop
#syntax -- for var in var:
    # print (var)
# using range in for
for i in range(20):
    print(i)
