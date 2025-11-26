#Types of exceptions

#153 exceptions is there

'''
name error exception- if and name or var is not defined
Zero division error-- cannot use 0 for division
valueError--if value should be int but str given means this will pop
'''
#instead giving common exception we can define indivi exceprion like nameerror valueError

# it will print the output we given
'''
try:
    a=int("str")
except ValueError as e:
    print("its not number")
'''

'''
Indexerror--

filenotfounderror--
'''

#handling multiple exception
'''
try:
    a=int("str")
    print(a)
except ValueError:
    print("its not number")
except ZeroDivisionError:
    print("Zero cannot divide")
'''