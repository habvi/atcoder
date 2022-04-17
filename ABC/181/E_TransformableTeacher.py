from bisect import bisect
from itertools import accumulate

n, m = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()
even = [0]
for i in range(0, n - 1, 2):
    even.append(abs(H[i] - H[i + 1]))

odd = [0]
for i in range(1, n - 1, 2):
    odd.append(abs(H[i] - H[i + 1]))

ac_e = list(accumulate(even))
ac_o = list(accumulate(odd))

ans = float('inf')
for w in W:
    i = bisect(H, w)
    total = ac_e[i // 2] - ac_e[0] \
            + ac_o[-1] - ac_o[i // 2] \
            + (w - H[i - 1] if i % 2 else H[i] - w)

    ans = min(ans, total)
print(ans)