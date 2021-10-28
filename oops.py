class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("config is",self.cpu,self.ram)
    
com1=computer(1,16)
com2=computer(2,8)

com1.config()
com2.config()

#find the address 

class com:
    pass

c1=com()
c2=com()

print(id(c1))
print(id(c2))


class a:
    name="aarthi" # public 
    def __init__(self,ss1): #instance attr
        self.ss1=ss1
obj1=a("sam")
obj2=a("ip")
print("play is boy {}".format(obj1.__class__.name))
print("paly is boy {}".format(obj2.__class__.name))
print("car is {}".format(obj1.ss1))
print("name is {}".format(obj2.ss1)) 


        



