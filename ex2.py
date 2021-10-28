'''for tic_book in range(15):
    paycash=int(input("amount"))
    if(paycash>=200):
        print("ticket booked")
        paycash=0
    else:
        print("sorry u have no balance")

#theatre
count=0
for i in range(5):
    cash=int(input("enter amount"))
    if(cash>=300):
        print("u have booked paltinum ticket")
        count+=1
    else:
        print("u r not eligible for platinum ticket")
print("count=",count)

#stock clearance sale of puma 1dp sneakers of 20 count no of orders
count=20
for i in range(1,20):
    items=int(input("how many items u wants to buy"))
    if(count>0):
        print("u buy {} items".format(items))
        count=-items
        print("count=",count)
    else:
        print("stack empty")'''


stock=20
oders=0
while stock>0:
    items=int(input("how many item u want buy"))
    if items<=stock:
        stock-=items
        oders+=1
    print("avilable is",stock)
print("count",oders)
