#Dictionary
#{}
#key:value pair

a={"name":"Rame","age":25}
print(type(a))
print(a["age"])

#keys hsould not be duplicate

#Functions
#to get values
print(a.get("key"))

# to get keys in var 
print(a.keys())

# to get values in var 
print(a.values())

#To get  both keys and values

print(a.items()) 

# use update to add key and value in var

a.update({"address":"chennai"})
print(a)

# to change value in a key
a["name"]="pranesh"
print(a) 

#to clear value in dict
a.clear()
'''
# to have nested dict put 
user: {
"user1": {
        }
"user2":{
       }

}
'''
