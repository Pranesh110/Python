#Try block 

#Two diff error

#compiler error and run time error

#compile if we miss , ) :
    
#Run time error

# if any runtime error occur i will hang so to check any erorr

#we can use try block to negate the hang
'''
try:
    a=10/0
except Exception as e:
    print(e)
'''
# inside try block we run code to check runtime error and exception will check for error

# here we can also add else statement to say if no runtine print the value of the code

try:
    a=10/5
except Exception as e:
    print(e)
else:
    print(a)

finally:#block to give final note after exception find or code run
    print("thank you")