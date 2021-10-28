try:
    class a:


        pass
    A=a()
    a.hello()

except AttributeError as e:
    print("attribute error",e)