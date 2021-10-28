a=4
for i in range(1,a):
    for j in range(1,a-i):
        print(" ",end=" ")
    for j in range(1,(2*i-1)+1):
        print("*",end=" ")
    print()

a=4
n=1
for i in range(1,a):
    for j in range(1,a-i):
        print(" ",end=" ")
    for j in range(1,(2*i-1)+1):
        print(n,end=" ")
        n=n+1
    print()
    