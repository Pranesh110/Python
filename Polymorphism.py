#polymorphism

# For a same function doing different type of activity
#lik data type and passing arg

'''
def tesst(a,b,c=0)
print(a+b+c)

tesst(10,2)
tesst(10,2,3)
'''
#prob

class animal():
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
class bird(animal):
    def sound(self):
        print("bird sing")

d=dog()
b=bird()

d.sound()
b.sound()#Method override dog and bird has inhert animal but same sound in animal will override and put birds func sound only


#2
'''
class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=int(input("l="))
        b=int(input("b="))
        return l*b
r=rectangle()
print("area of rectangle:",r.area())
'''

#3.
class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
        
    def mark(self):
        print("Name:",self.name)
        print("Grade:",self.grade)

s=student("pranesh","A")
s.mark()

#4.
class vehicle():
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started")
h=car()
h.start()

#5
class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def __init__(self,name,salary,dept):
        super().__init__(name, salary)
        self.dept=dept
    def display(self):
        print("Name:",self.name,"Salary:",self.salary,"Dept:",self.dept)
m=manager("pranesh",20000,"it")
m.display()
    



















