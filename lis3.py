'''name=[]
mark=[]
for i in range(5):
  a=input("enter the name")
  b=int(input("enter the mark"))
  name.append(a)
  mark.append(b)
h=max(mark)
l=min(mark)
print(h)
print(l)
for i in range(5):
  if h==mark[i]:
    print("h name:",name[i])
  if l==mark[i]:
    print("l name:",name[i])

li=[]
for i in range(4):
  a=input("enter the name:")
  li.append(a)
print(li)
li.sort()
print("sort:",li)

a=[]
a.append("aarthi")
a.append("ip")
a.append("nithya")
print("length of list:",len(a))
b=len([1,5,8,9,4])
print(b)'''

a=[1,3,4,5]
b=[6,7,9]
print("concat:",a+b)
print("concat:",[*a,*b])
for i in b:
  a.append(i)
  print("concat:",a)
