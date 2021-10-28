a=" aarthi"
print(a.strip())
print(a[0:3])
b="aarthi,ritham"
print(b.split(','))
c="aarthi"
print(c.capitalize())
d="This Is My World"
print(d.casefold())
print(d.center(30))
print(d[-1])
print(c.replace("t","d"))
print(c.upper())
print(c.lower())
print('a' in c)
print('g' not in c)
e="aarthi"
f="ritham"
print(e[0])
print(e[1])
print(e[2])
print(e[3])
print(e[4])
print(e[5])
print(e*5)
print(e+f)
print(len(e))
for i in a:
    print(i)
g="health is,wealth."
print(g.endswith(","))
print(g.endswith("."))
h="a\ta\tr\tt\th\ti"
print(h.expandtabs(20))
i="aarthi","ritham","ip"
print("*".join(i))
j="aarthi123"
print(j.isalnum())
print(j.isalpha())
k="python \"programing"
print(k)
l="python"
m="programing"
n=f"{l} {m}"
print(n)
