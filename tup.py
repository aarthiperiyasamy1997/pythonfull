#two methods 1.count 2.index
a=tuple((1,4,5,7)) #tuple constructor
print(type(a))
b="aarthi",
print(type(b))
c=("aarthi")
print(type(c))
print(len(a))
i=[1,3,"sam",8,7]
print(i[2])
print(i[-1])
a=("aarthi","ip","nithya","kili")
print(a[0:3])
print(a[:2])
print(a[2:])

#update tuple
g=(1,5,7,4,8,9) 
h=list(g)
h[2]=3
g=tuple(h)
print(g)
d=("sam","karthi","arun","ammu")
e=list(d)
e.append("aarthi")
e.insert(1,"ip")
e.remove("ammu")
d=list(e)
print(d)
f=("raja","mani")
d += f
f=tuple(d)
print(f)
t=f*2
print(t)

#count and Index
a=(1,2,34,5,7,1,3,4,1,8)
b=a.count(1)
print(b)
c=a.index(34)
print(c)






