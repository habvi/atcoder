from itertools import accumulate
from bisect import bisect

n, m = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))
H.sort()
W.sort()

ae = []
for i in range(0, n - 1, 2):
    ae.append(abs(H[i] - H[i + 1]))

ao = []
for i in range(1, n - 1, 2):
    ao.append(abs(H[i] - H[i + 1]))
    
ac1 = [0] + list(accumulate(ae))
ac2 = [0] + list(accumulate(ao))

ans = float('inf')
for w in W:
    bi = bisect(H, w)
    bi = bi if bi % 2 == 0 else bi - 1
    i = bi // 2
    ans = min(ans, ac1[i] - ac1[0] + abs(H[bi] - w) + ac2[-1] - ac2[i])
print(ans)