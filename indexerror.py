try:
    li=[1,8,6,7]
    print(li[5])

except IndexError as e:
    print("index error",e)
    