n = int(input())
sp = [list(input().split()) + [i+1] for i in range(n)]
sp.sort(key=lambda x: (x[0], -int(x[1])))
for s, p, i in sp:
    print(i)