#Functions

#A function has statements to do we will call the the function if we need that jof need to done

#def is the function
'''
def painter():
    print("hi")
painter()
'''
#here def is func so inside painter we have print
#at end we will pain painter name of fun to call to do the things insied that function
'''
def test():
    i=10
    while i<=200:
        print(i,end=",")
        i= i+10
test()
'''

#create a fun add() sub() mul() and get input
'''
def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()

def sub():
    a=int(input())
    b=int(input())
    print(a-b)
sub()

def mul():
    a=int(input())
    b=int(input())
    print(a*b)
mul()
'''


# get a int from user and pss it to function called findpassorfail() func print number is even or odd
'''
x=int(input("Enter number:"))

def passorfail():
    if x%2==0:
        print("The number is even")
    else:
        print("The number is odd")
passorfail()
'''
#or 

#we can give value while calling the function
#that value is stored in one variable

#-in last we call function passorfail() here in the bracket we are givning value

#that value will store in var where we give the var name in def passorfail(var)

#so with that value the func perform what all inside the function
'''
def passorfail(x):
    if x%2==0:
        print("Even")
    else:
        print("Odd")
passorfail(x=int(input("Enter number:")))

'''
#get num and pas to func and fucion do the number is 35 above means pass below means fail
'''
def prf(x):
    if 35<=x<=100:
        print("pass")
    else:
        print("Fail")

c=int(input("Enter number:"))
prf(c)
'''



def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)

a=int(input("a="))
b=int(input("b="))
printrange(a,b)
#------------------------------


#arbitary function (*)
# to add multiple value in function
#def add(a,b)
#print(10,5)
# this is standard now pass more vvalue in function use

'''
def add(*range):
    print(range)

add("ram","shyam","mam","tam")
'''
#we can pass many argument value to function




















  