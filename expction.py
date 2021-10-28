# how many error accur in python

err=dir(locals()['__builtins__'])
print(err)
print(len(err))
 
try:
    a=10
    b=0
    c=a/b
    print(c)

except Exception as e:
    print(e)