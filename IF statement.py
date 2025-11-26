# if statement
#syntax
'''
var=value
if var is (statement):
          print(condition)
          '''
          
#Example write a program to check the given number is even or not

number=int(input("Enter the number:"))
if number%2==0:
    print("The given number is EVEN")

# if else if condition is not true it will go to else
else:
    print("Not even")

# write program vote elgibility by enter his name and age

name=input("Enter your name:")
age=int(input("Enter your age:"))
if age>=18:
    print(name,"eligible for voting")
else:
    print(name,"not eligible for voting")
    
# elif (if condition is false or true do elif and print)
'''
 if condition
 print (statement)
 elif condition
 print (statement)
 else
 print(statement)
'''
 
 #nested IF
 
'''
 if condition
 if condition
 if condition
 print(statment)
'''

m1 = int(input("mark1: "))
m2 = int(input("mark2: "))
m3 = int(input("mark3: "))

total = m1 + m2 + m3
average = total / 3.0

print("Total:", total)
print("Average:", average)

# First check Pass/Fail
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("You are Pass")

    # Now check grade only if passed
    if 90 <= average <= 100:
        print("You passed with Grade A")
    elif 80 <= average < 90:
        print("You passed with Grade B")
    elif 70 <= average < 80:
        print("You passed with Grade C")
    else:
        print("Pass with Grade D")

else:
    print("You are Failed")
'''
#mini calculater  
a=int(input("num1:"))
b=int(input("num2:"))
Method=input("What to do add/Sub/Multi/Divi:")
if Method=="add":
    print(a+b)
elif Method=="Sub":
    print(a-b)
elif Method=="Multi":
    print(a*b)
elif Method=="Divi":
    print(a/b)
else:
    print("Invalid")
'''

    

  