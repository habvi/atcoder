n = int(input())
s = set()
A = []
for _ in range(n):
    a = int(input())
    s.add(a)
    A.append(a)

d = {ss : i for i, ss in enumerate(sorted(s))}
for a in A:
    print(d[a])