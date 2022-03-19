n = int(input())
A = list(map(int, input().split()))

one = [0]
zero = [0]
for i, a in enumerate(A):
    if a == 1:
        one.append(one[-1] + 1)
        zero.append(zero[-1])
    else:
        one.append(one[-1])
        zero.append(zero[-1] + 1)

ac = []
for o, z in zip(one, zero):
    ac.append((o - z))

mn, mx = 0, 0
ans_mn, ans_mx = 0, 0
for r in ac:
    mn = min(mn, r)
    mx = max(mx, r)
    ans_mn = min(ans_mn, r - mx)
    ans_mx = max(ans_mx, r - mn)

print(ans_mx - ans_mn + 1)