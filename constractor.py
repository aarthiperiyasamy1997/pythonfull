class A:
    def __init__(self): #constractor to initializze the object
        print("happy to see")

    def b(self):
        print("feeling sad")

a=A() #only called constractor object 
a.b() #calling function 


#constractor using parameter

class com:
    def __init__(self,name,age,college):
        print("name:",name)
        print("age:",age)
        print("college:",college)

c=com("aarthi",25,"MEC") #parameter passing

# accessing constractor object in normal function using self keyword

class comp:
    def __init__(self,palce,company):
        self.a=palce
        self.b=company

    def fun(self):
        print("place:",self.a) #using self keyword access const obj
        print("company:",self.b)

c=comp("chennai","CTS") 
c.fun()

#addtion programe

class a:
    def __init__(self,b,c):
        self.b=b
        self.c=c

    def add(self):
        d=self.b+self.c
        print("ADD",d)

A=a(10,20)
A.add()
