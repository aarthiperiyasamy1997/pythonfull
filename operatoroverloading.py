class operator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)

obj=operator(10,20)

#diff self and object

class oper:
    def __init__(self,a):
        self.a=a
        print(self.a+self.a) #same value add double time

object=oper(10)
object1=oper(20)
#print(object.a+object1.a) #val 1 and val 2 added 


#using add method in operator overloading

class op:
    def __init__(self,a):
        self.a=a
    def __add__(self,b): # or def __sub__(self,b):
        self.b=b
        return self.a+b.a

o=op(50)
o1=op(10)
print("sum",o+o1)
