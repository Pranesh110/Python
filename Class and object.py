# Class is like collections of functions and variables

#Class is like GOA
#object is like Two persons in GOA wants to do Diff things from one other as their wish
#But in same goa so Two set of diff actions(functions) in same Class

#syntax  class goa:
class goa:
    drinks="Have a drink"
    def bar(self):  #for ever function inside class assign self in def
        print("Bar",self.ab)
    def beach(self):
        print("beach")
p1=goa() #calling class goa
p2=goa()
print(p1.drinks)  # calling the var inside the class
p1.ab="test"
p1.bar()  #calling function inside class