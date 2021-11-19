from itertools import accumulate
from bisect import bisect
n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ac = [0] + list(accumulate(A))
bc = list(accumulate(B))

ans = 0
for i in range(n+1):
    if ac[i] > k: break
    bi = bisect(bc, k - ac[i])
    ans = max(ans, i + bi)
print(ans)