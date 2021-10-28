class computer:
    def __init__(self) :
        self.name="aarthi"
        self.age=25
    
    def update(self):
        self.age=24

c1=computer()
c2=computer()


c1.name="navin"
c1.age=23

c1.update() #self poiting to c1 age will change


print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)

 
l=[4,3,2,1]
x=l.sort()
print(l)

l1=[10,3,5,4,1]
r=l1[-1]*l1[1]
if(r%2==0):
    print(r)
else:
    print("odd num")

