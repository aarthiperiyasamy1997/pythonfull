#fun with parameter using list

bal=[10000,8000,75000,40000]

def debit(money=0,pos=0):
    if money<=bal[pos]:
        bal[pos]-=money
        print(money,"debited")
        return bal[pos]
    else:print("can't debited")

a=debit(1000,1)
print(a)

#fun without parameter  with return type
def job():
    exp=int(input("tell us exp:"))
    skill=input("tell us skill")
    if exp<=4 and exp>=6 and skill=='python' or skill=='java':
        return "promoted us team lead"
    elif exp>=6 and exp<=10 and skill=='agile' or skill=='develop':
        return "promoted us manager"
    else:print("u r not eligible")
job()
