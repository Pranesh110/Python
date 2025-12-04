#Encapsulation

#when a calss with fuc created in outside a var value can be change

#so to make the var as private we use encapsulation

#restricting var to access in outside
# to do that we use __self.var(doble underscore behind var)
'''
class test():
    def __init__(self):
        self.company="google"
    def display(self):
        print(self.company)
a=test()
a.company="jio" # in outside we can change the value of var

a.display()

'''
#so to make the var as private and not access by outside
class test():
    def __init__(self):
        self.__company="google" #given double underscore
    def display(self):
        print(self.__company)
a=test()
a.company="jio"
a.display()
#ot will be google not jio
#this var only be access within the Class and not outside of the class

#if only one userscore give behind var
#it is protected var can we use by child classes too
class test():
    def __init__(self):
        self._company="google"
class b(test):
    pass

b1=b()
print(b1._company)

#now the procted var can be access by child class
