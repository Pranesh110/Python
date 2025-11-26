s="this is project"
for i in s:
    print(i,end="")
    print(" ")
    
d={"a":1,"b":2} 
for i in d.items():
    print(i)
    
t=[{"name":"pranesh","age":21},{"name":"ram","age":24}]
for i in t: 
    if i["name"]=="pranesh": 
        print(i["age"])
