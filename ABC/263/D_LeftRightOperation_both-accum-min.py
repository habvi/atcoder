from itertools import accumulate

def gen_mn(LR):
    ac_mn = []
    mn = 0
    mn_idx = 0
    for i, (a, lr) in enumerate(zip(ac, LR)):
        now = lr - a
        if now < mn:
            mn = now
            mn_idx = i
        ac_mn.append(LR[mn_idx] + ac[i] - ac[mn_idx])
    return ac_mn


N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ac = list(accumulate(A))
l_mn = [0] + gen_mn(list(accumulate([L] * N)))

ac = list(accumulate(A[::-1]))
r_mn = gen_mn(list(accumulate([R] * N)))
r_mn = r_mn[::-1] + [0]

ans = ac[-1]
for l, r in zip(l_mn, r_mn):
    ans = min(ans, l + r)
print(ans)