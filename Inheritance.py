#Inheritance 

#it is like one class can be inheritaed or use by other classes

# if DAD has phone and son has laptop if SON need to use dads phone he can using inheritance
'''
class dad:
    def phone(self):
        print("phone")
class son:
    def lap(self):
        print("lap")
ram=son()
ram.lap()
'''
#now he can use his lap but no dad class phone

#now we need to link btw dad and son class

#It is a single inheritance using one cls to another cls
'''
class dad():
    def phone(self):
        print("phone")
class son(dad): #we are giving dad class inside son class
    def lap(self):
        print("lap")
ram=son()
ram.lap()
ram.phone()
'''



# for multiple inheritance class can be inherited
'''
class dad():
    def phone(self):
        print("phone")
class mom():
    def sweet(self):
        print("sweet")
class son(dad): #we are giving dad class inside son class
    def lap(self):
        print("lap")
ram=son()
ram.lap()
ram.phone()
ram.sweet() #this throw error coz ram class has only dad class not mom class
'''
class dad():
    def phone(self):
        print("phone")
class mom():
    def sweet(self):
        print("sweet")
class son(dad,mom): #we are giving dad and mom class inside son class to use both class
    def lap(self):
        print("lap")
ram=son()
ram.lap()
ram.phone()
ram.sweet()



#Multi level inheritance

class dad():
    def phone(self):
        print("dad phone")
class mom(dad):
    def sweet(self):
        print("sweet")
class son(mom): 
    def lap(self):
        print("mylap")
ram=son()
ram.lap()
ram.phone()
ram.sweet()

mother=mom()
mother.phone()

#here son has mom calss and mom has dad class 
#so son can use both mom and dad as mom had dad class
#and mom can use dad class




#hierarchy inheritance:
# one base class that is using by many classes
class dad():
    def money(self):
        print("dad money for son's")
class son1(dad):
    pass
class son2(dad):
    pass

s2=son2()
s2.money()
s1=son1()
s1.money()



#Hybrid inheritance:
#mixed of mutiple,hiearchy,single inheritance
class dad(): 
    def money(self):
        print("dad money for son's 2")
class land():
    def land1(self):
        print("land") 
class son1(dad,land):
    pass
class son2(dad):
    pass

s2=son2()
s2.money()
s1=son1()
s1.money()
s1.land1()
    


