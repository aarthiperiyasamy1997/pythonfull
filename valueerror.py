try:
    n=int(input("enter the number"))
    print(n)

except ValueError as e:
    print("value error",e)
    
