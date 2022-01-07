n = int(input())
A = [int(input()) for _ in range(n)]
s = set(A)
d = {ss : i for i, ss in enumerate(sorted(s))}
for a in A:
    print(d[a])