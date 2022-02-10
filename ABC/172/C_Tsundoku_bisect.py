from bisect import bisect
from itertools import accumulate

n, m, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

aca = [0, *accumulate(A)]
acb = list(accumulate(B))

ans = 0
for i, a in enumerate(aca):
    if a > K:
        break
    bi = bisect(acb, K - a)
    ans = max(ans,  i + bi)
print(ans)