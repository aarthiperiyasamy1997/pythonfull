#two position 1.key 2.value
'''a={"name":"aa","age":25,"name":"bb"}
print(a)
print(type(a))
print(a["age"])
print(len(a))

#methods 1.get 2.keys 3.value 4.add
b={"name":"pp","age":21,"frds":["sam","ip","nithya"]}
print(b)
print(b["age"])
c=b.get("name")
print(c)
c=b.keys()
print(c)
b["bike"]="xy"
print(b)
c=b.values()
print(c)
b["age"]=26
print(b)
b.update({"name":"rr"})
print(b)'''

#remove method 1.pop 2.popitem 3.del 4.clear
x={"name":"pp","age":21,"game":"crkt","frds":["sam","ip","nithya"]}
print(x)
x.pop("name")
print(x)
x.popitem()
print(x)
del x["age"]
print(x)
x.clear()
print(x)

'''#for loop using 
y={"name":"pp","age":21,"game":"crkt","frds":["sam","ip","nithya"]}
print(y)
for i in y:
    print(i)

for i in y:
    print(y[i])

for i in y.keys():
    print(i)

for i in y.values():
    print(i)

for i,j in y.items():
    print(i,j)

#if condition
r={"name":"pp","age":21,"game":"crkt","frds":["sam","ip","nithya"]}
print(r)
b=r.items()
print(b)
r["food"]="briyani"
print(r)
if "age" in r:
    print("yes")
else:
    print("no")

#copy method
s={"name":"pp","age":21,"game":"crkt","frds":["sam","ip","nithya"]}
print(s)
v=s.copy()
print(v)
v=dict(s)
print(v)
b=s.setdefault("food","briyani")
print(b)'''



 