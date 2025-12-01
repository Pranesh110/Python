#methods is functions
#Diff type of methods in class

#1. Instance method:
    #where ever we use object to call var like:
    #self=obj
    #self.price it is a instance method

#2. Class method:
    #if we are creating function for class varibale
    #like class mobile:
        #charger="c-type"  #class variable
   # we can use function as 
'''
    class mobile:
        charger="c-type" #class var
    def type(cls):   #instead of self use cls coz self is for object
        print("type:,cls.type)
    #it will call the var of class variable
'''


# include of instance and class var and method
class mobile:
    charger="c-type"  #class variable
    def __init__(self,price,model):
        self.price=price  #instance var
        self.model=model  #instance var 
    def display(self): # instance method
        print("price:",self.price) #calling instance var
        print("model",self.model) #calling class variable 
    def type(cls): #class method
        print("type:",cls.charger)
mobile.charger="b-type"
redmi=mobile("50","redmi")
moto=mobile("40", "moto")
redmi.display()
moto.display()
#now calling the fun with class not obj
#mobile.type() if we give empty in brcket it show error it need what cls neeed to define
mobile.type(mobile)
#we can give the cls inside it lik this



#DECORATORS
# OR we can use decorators  to define it is a class method by
# putting @classmethod above the class function
class mobile:
    charger="c-type"  #class variable
    def __init__(self,price,model):
        self.price=price  #instance var
        self.model=model  #instance var 
    def display(self): # instance method
        print("price:",self.price) #calling instance var
        print("model",self.model) #calling class variable 
    @classmethod #decorators
    def type(cls): #class method
        print("type:",cls.charger)
mobile.charger="b-type"
redmi=mobile("50","redmi")
moto=mobile("40", "moto")
redmi.display()
moto.display()
mobile.type() # no need to givve cls name inside decorator will done






# STATIC METHOD
# we are not calling instance or class var and method here
'''
class test:
    def info():
        print("test")
t=test()
t.info() 
'''
#this will throw error

#so here also we can use decorators @staticmethod
#to run this by saying it is static

class test:
    @staticmethod
    def info():
        print("test")
t=test()
t.info() 