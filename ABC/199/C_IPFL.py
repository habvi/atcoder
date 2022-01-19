n = int(input())
n2 = 2 * n
s = list(input())
q = int(input())

def mask(x):
    return (x + msk) % n2

msk = 0
for _ in range(q):
    t, a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if t == 1:
        s[mask(a)], s[mask(b)] = s[mask(b)], s[mask(a)]
    else:
        msk = (msk + n) % n2

ans = [""] * n2
for i, t in enumerate(s):
    ans[mask(i)] = t
print("".join(ans))