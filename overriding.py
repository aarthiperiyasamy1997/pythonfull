class a:
    def name(self):
        print("ip")
class b(a):
    def name(self):
        super().name()
        print("nithya")
class c(b):
    def name(self):
        super().name()
        print("aarthi")
x=c()
x.name()

