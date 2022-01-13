sa = list(input())
sb = list(input())
sc = list(input())
p = 'abc'
cd = [sa, sb, sc]
x = sa[0]

while True:
    i = p.index(x)
    if cd[i]:
        x = cd[i].pop(0)
    else:
        print(p[i].upper())
        break