from itertools import product
n, x = map(int, input().split())
A = []
for _ in range(n):
    l, *a = map(int, input().split())
    A.append(a)

ans = 0
for pr in product(*A):
    a = 1
    for p in pr:
        a *= p
    if a == x:
        ans += 1
print(ans)
