'''def add(a,b): #formal argument
    c=a+b
    print(c)
add(5,6) #actual agrument 1.position 2.keyword 3.default 4.var len

#position
def person(name,age):
    print(name)
    print(age)

person("aarthi",25) #position

#keyword
def person(name,age):
    print(name)
    print(age)

person(age=25,name="aarthi") #keyword

#default
def person(name,age=20): #default
    print(name)
    print(age)

person("aarthi")'''

#varable length
def add(*b): #tuple
    c=0
    for i in b:
        c=c+i
    print(c)

add(3,6,8,5) #using var len #multible value passing one argument

#keyword var len argument
def person(name,**data): #tuple
    print(name)
    print(data)

person("aarthi",age=25,city="salem",food="briyani")

#using for loop
def person(name,**data):
    print(name)
    
    for i,j in data.items():
        print(i,j)

person("aarthi",age=25,city="salem",food="briyani")