class fav:
    def movie(self):
        print("family movie")

class b(fav):
    def food(self):
        print("briyani")

class c(fav):
    def game(self):
        print("cricket")

class d(fav):
    def city(self):
        print("salem")
class f(c,b,d):
    def place(self):
        print("cbe")
    

x=f()
x.movie()
x.food()
x.game()
x.city()
x.place()

#another method
class fav:
    def movie(self):
        print("family movie")

class b(fav):
    def food(self):
        print("briyani")

class c(fav):
    def game(self):
        print("cricket")

class d(fav):
    def city(self):
        print("salem")

x=d()
y=c()
z=b()

x.city()
x.movie()
y.game()
z.food()