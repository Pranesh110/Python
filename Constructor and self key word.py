
# Constructor 
'''
constructor is a unique function that can automaticaly called after obfect is created by clas

class laptop():
    def __init__(self):
        print("demo")
    def price():
        print(50)
hp=laptop()  

now output will be deom no need to call that fucntion init
it will automatically call
'''
class laptop:
    def __init__(self):
        self.price=0
        self.proc=""
        self.ram=""
    def display(self):
        print("ram",self.ram)
        print("price",self.price)
hp=laptop()
hp.price=500
hp.proc="gtx"
hp.ram="8gb"
print(hp.price)
hp.display()
# now here the object call the class and hp.price and hp.ram hp.proc var will get created
# and automatically init function will run
#in next we have give value to price ram and proc

#and we call the func disply this will run
#inside display function we printed price and ram
# so the value will be taken from what we gave inside the init and disply will print
'''
Here What this SELF keyword doing:
'''
#whle call display it wil go like hp.display(hp)
#so while calling display(self) here self=hp
#so inside display we have print self.price that is hp.price
#so the valu hp.price will print

#---------------------------------------------------

#example sums:
    
#1. create a class called student create a var= name and reg using constructor
# create a func called display which should display the name and reg number of student

class student:
    def __init__(self):
        self.name=""
        self.reg=0
    def display(self):
        print("Name:",self.name)
        print("Reg number:",self.reg)

pranesh=student()
atchaya=student()
pranesh.name="Pranesh"
pranesh.reg=200
atchaya.name="Atchaya"
atchaya.reg=202

pranesh.display()
atchaya.display()
#----------------------------------

#2. create a class fruit and using constructor create car color
# obj is apple and pas the color var as a parameter through object
'''
class fruit:
    def __init__(self):
        self.color=""
apple=fruit()
apple.color="RED"
print(apple.color)
'''  # this is basic but we have to give red in fruit("red")

'''
class fruit:
    def __init__(self):
        self.color=""
apple=fruit("red")
''' #it willl thorw error as the fruit()has two arg that is apple and red
# By default fruit(apple) will take palce so when we give red instide fruit it a extra one
# it will take like fruit(apple,red) but near self there no extra var for arg red
class fruit:
    def __init__(self,col):
        self.color=col
apple=fruit("red")
print(apple.color)

#now the self take apple and col take the red vaule


#3. create a class teacher and var name and reg using constructor
#create a func display which display name and reg 
#create object t1 and t2 and pass name and reg thrugh object

class teacher: 
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print("Name:",self.name)
        print("reg num:",self.reg)
t1=teacher("Thomas","1")
t2=teacher("Jon", "2")

t1.display()
t2.display()
#here as befor we are pasing arg in call teahcer itself so we name and reg parameter in init


#4. create a class calc
#fucn add,sub,mul and all fuc should take 2 parameter
#pass the a and b value through object

class cal:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("Addition:",self.num1+self.num2)
    def sub(self):
        print("Sub:",self.num1-self.num2)
    def mul(self):
        print("mul:",self.num1*self.num2)
number=cal(2,5)

number.add()
number.sub()
number.mul()

# OR we can do without constructor
class calc:
    def add(self,a,b):
        print("add:",a+b)
num=calc()
num.add(10,2)

    
    