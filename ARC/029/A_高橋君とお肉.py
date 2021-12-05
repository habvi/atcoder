from itertools import product
n = int(input())
t = [int(input()) for _ in range(n)]
ans = float('inf')
for pr in product([0, 1], repeat=n):
    a, b = 0, 0
    for i, p in enumerate(pr):
        if p:
            a += t[i]
        else:
            b += t[i]
    ans = min(ans, max(a, b))
print(ans)