 #types of variable in class

#1.Instance variable:(Inside constructor)
    #self.brand,self.price,self.type
    #this obj.var are instance variable
    #For every object the value for that varibale change


#2.Class variable:(inside class)
#If the value for the Object should not change (same for all like that)

#Like if for moblie obj price and model gonna change but charger_type is C for all means
#insted of giving type value for all object

#we are giving the var and value inside class
'''

class mobile:
    charger="c-type"  #class variable
    def __init__(self,price,model):
        self.model=model  #instance var
        self.price=price  #instance var
    def disply(self):
        print("price:",self.price) #calling instance var
        print("type",self.charger) #calling class variable 
redmi=mobile("50","redmi")
redmi.display()


'''
#We can change the class variable in outside class also by
# calling class with that var
# mobile.charger="b-type" now it will replace the c to b

'''
class mobile:
    charger="c-type"  #class variable
    def __init__(self,price,model):
        self.model=model  #instance var
        self.price=price  #instance var
    def disply(self):
        print("price:",self.price) #calling instance var
        print("type",self.charger) #calling class variable 
mobile.charger="b-type" #here
redmi=mobile("50","redmi")
redmi.display()

'''
