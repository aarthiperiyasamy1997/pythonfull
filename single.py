#single inheritence

class a:
    def name(self):
        print("parent class")

class b(a):
    def name1(self):
        print("child class")

c=b()
c.name()
c.name1()