from bisect import bisect
from itertools import accumulate

def ceil(a, b):
    return (a + b - 1) // b

def calc(A):
    diff = []
    A.append(0)
    for i in range(0, N, 2):
        diff.append(abs(A[i + 1] - A[i]))
    return diff


N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()
diff_l = calc(H[:])
diff_r = calc(H[::-1][:])
ac_l = list(accumulate(diff_l))
ac_r = list(accumulate(diff_r))[::-1]

ans = float('inf')
for w in W:
    i = bisect(H, w)
    if i % 2:
        i -= 1
    tmp = abs(H[i] - w)
    i //= 2
    if i - 1 >= 0:
        tmp += ac_l[i - 1]
    if i + 1 < ceil(N, 2):
        tmp += ac_r[i + 1]
    ans = min(ans, tmp)
print(ans)