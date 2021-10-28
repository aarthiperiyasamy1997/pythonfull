'''def city():
    a=input("tell ur fav city:")
    if a == 'chennai':print("Mall")
    elif a == 'salem':print("Temple")
    elif a == 'madurai':print("flower")
    else:print("invaild")
city()

def grade(qual,mark):
    if qual == 'B.E' and mark == 70 :print("u r eigible in 1st clss")
    elif qual == 'B.E' and mark == 55 :print("u r eligible in 2nd clss")
    else:print("u r not eligible")
grade("B.E",70)
grade("B.E",45)'''


def vote(name,age,location):
    if age == 18 :print(name,"is eligible for vooting",location)
    elif age == 25 :print(name,"eligible for vooting",location)
    else:print("u r not eligible for vooting")
vote("aarthi",18,"salem")
vote("preethi",20,"chennai")
vote(age=25,location="madurai",name="ip")