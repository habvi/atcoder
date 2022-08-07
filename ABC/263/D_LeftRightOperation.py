from itertools import accumulate

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ac_a = list(accumulate(A[::-1]))
ac_r = list(accumulate([R] * N))

ac_mn = []
idx = N
total = ac_a[-1]
mn = total
for i, (a, r) in enumerate(zip(ac_a, ac_r)):
    now = r + total - a
    if now <= mn:
        idx = N - i - 1
        mn = now
    ac_mn.append(idx)
ac_mn = ac_mn[::-1]
ac_a = ac_a[::-1] + [0]

ans = sum(A)
l = 0
for i, a in enumerate(A):
    mn = ac_mn[i]
    total = l + ac_a[i] - ac_a[mn] + (N - mn) * R
    ans = min(ans, total)
    l += L
ans = min(ans, l)
print(ans)