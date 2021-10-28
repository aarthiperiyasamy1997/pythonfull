try:
    n=int(input("enter the number"))

except ValueError as e:
    print("value error",e)

else:
    print("number is",n)

finally:
    print("end")