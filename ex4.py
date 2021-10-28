count=0
pre=0
for i in range(10):
    amount=int(input("current balance"))
    if amount>pre:
        count+=1
    pre=amount
print(count)