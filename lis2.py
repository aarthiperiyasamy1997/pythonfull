l1=['aa','bb','cc','dd']
l2=['gg','ff']
l1.reverse()
print(l1)
l2.extend(l1)
print(l2)
l1.remove('bb')
print(l1)
l1.clear()
print(l1)
l3=[1,2,3,5,1,6,7]
a=l3.copy()
print(a)
count=a.count(1)
print(count)
print(l3)
val=int(input("enter the value"))
poss=int(input("enter the position"))
l3.insert(poss,val)
print(l3)
