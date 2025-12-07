#exception handling

#types:
    #complier error

# During complie that is reading the code line there is error
#syntax error


#logical error
#progrsm wiil be run but the value we given might be wrong


#run time error
#Getting error wilhe the code is running 
#like if getting value from user a and b var
#user given a value in int right and b has string it will throw error
#as while running it geeting error while processing

#So to avoid that RED lines error and to make it understanable

#to handle this errors we use try and block
try:
    a=int(input())  
    b=int(input()) 
    print(a+b)
except Exception:
        print("something error")
finally:
    print("it works")
#If any error this will give ot something not red lines

#we can give multiple types of except errors line by line to check
#like value error, type error,name error

#exception if bundle of all errors and give the reason
#finally is like banner at end if output run without error or with error.