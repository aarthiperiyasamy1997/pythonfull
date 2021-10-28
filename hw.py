#how to get calender
import calendar
print(calendar.month(2021,11))

#that will be run but no output
d1={"a":1,"b":2,"c":3}
d1.get("a")

#invaild syntax error
'''a=1
print(a++)

#unsuported operand error will occur
a=3
print(a + "3")'''

#output will display
li=[10,3,4,6,1]
r=li[-1]*li[1]
if r%2==0:
    print(r)
else:
    print("odd num")

#sort order output will display
s={2,0.1,1}
print(s)

#output will display
s="python"
print(s[1:3])

#reverse the string
s="python"
print(s[-1::-1])

#output will display
for i in 'python':
    if i=='o':
        pass
    print(i, end=", ")

#how to print without using print() fun in python
import sys
sys.stdout.write("hello world")