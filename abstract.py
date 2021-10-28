# blue print of class

from abc import ABC #abstract class does not create objact
class bus(ABC):
    def volvo(self):
        print("Governemnt bus")

class SRT(bus):
    def volvo(self):
        print("luxury bus")

class SETC(bus): 
    def volvo(self):
        print("A/C BUS")

class KPN(bus):
    def volvo(self):
        print("nomal bus")
b=bus()
b.volvo()

s=SRT()
r=SETC()
t=KPN()
s.volvo()
r.volvo()
t.volvo()

