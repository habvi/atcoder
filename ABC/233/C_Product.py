from itertools import product

n, x = map(int, input().split())
A = []
for _ in range(n):
    L, *a = map(int, input().split())
    A.append(a)

ans = 0
for pr in product(*A):
    mul = 1
    for p in pr:
        mul *= p
    ans += mul == x

print(ans)