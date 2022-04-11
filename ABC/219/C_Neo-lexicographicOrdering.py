alph = input()
n = int(input())

d = {a : i for i, a in enumerate(alph)}
name = []
for _ in range(n):
    S = input()
    num = tuple(d[s] for s in S)
    name.append((num, S))

name.sort()
for _, ans in name:
    print(ans)