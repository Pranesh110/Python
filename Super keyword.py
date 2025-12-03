#Super keyword

# If we need to run a function from parent class first or any where before any funtion of its own we use super keyword

class a():
    def __init__(self):
        print("a")
    def display(self):
        print("hi")
class b(): #to run other class fun first nee to add it
    def __init__(self):
        super().__init__() #super which is used to run the a class init first before b init 
        print("b")
        super().__init__()
    def display(self):
        print("hi form b")
class c(a,b): #if we give multiple inheritance it will take first value insied it that is a so it will super initi of a class  not b
    def __init__(self): 
        super().__init__()
        print("c")
        #output a c
t1=c()


