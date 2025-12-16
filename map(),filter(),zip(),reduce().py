# Map funtion:

#Map will do the iteration

#map(function, iterables thats is [1,2,3])
My_list=[1,2,3]
def mul(items):
    return items*2

print(list(map(mul,My_list))) # calls eache value in my list and do the function and put it in My_list var
print(My_list)
#Has it is pure it wont affect the default My_list var
#It will crate new one
    
#So it will call each value in list and do the function looped automatically

#Filter Function

# It will also iterate the list values
# List the value with wht function we defined with True or false
# Filters the value with T or F

My_list=[1,2,4]
test=[4,5,6]
def mul(items):
    return items%2 ==0

print(list(filter(mul,My_list))) # calls eache value in my list and do the function and put it in My_list var
#gives out put only 2 in list format has it is module by 2==0

#zip:
    #take value of diff var values and zip it in together with each indexs

print(list(zip(My_list,test)))
#output [(1,4), (2,5)]

#Reduce function
#reduce function will takes the list of vaule and give cumulative of One vaule

#reduce is not buildin function so import it,# from functools import reduce

from functools import reduce

maxi=reduce(lambda a,b: a if a>b else b,My_list)
print(maxi)

















