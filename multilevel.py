#multilevel inheritence

class bank:
    def name(self):
        print("AXIS bank")

class bank1(bank):
    def name1(self):
        print("HDFC bank")
class bank2(bank1):
    def name2(self):
        print("INDIAN bank")

a=bank2()
a.name()
a.name1()
a.name2()