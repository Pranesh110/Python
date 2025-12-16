'''
Pure function: A function that will not chnage or disturb outside var or another functions values it is pure function

Impure function: A function that has side effect that  is if a function chnage or disturb the other function value of var its is impure function
'''
#Pure:
'''
def test(num):
    total=0
    total = total+num
    print(total)
test(2)
'''

#impure:
'''
total =0
def test(num): 
    global total
    total += num 
    print(total)

def nu():
    print(total)

test(2)
nu()

output:
    2
    2
not:
    2
    0 has its change the value of other function
    
'''
        