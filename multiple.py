#multiple inheritence

class travel:
    def name(self):
        print("car travel")

class travel1:
    def name1(self):
        print("bike travel")

class travel2(travel,travel1):
    def name2(self):
        print("train travel")

a=travel2()
a.name2()
a.name1()
a.name()