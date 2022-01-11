n = int(input())
a = []
for i in range(n):
    s, p = input().split()
    a.append((s, p, i + 1))
a.sort(key=lambda x: (x[0], -int(x[1])))

for s, p, i in a:
    print(i)