from math import pi

def f(x):
    return x ** 3


n, q = map(int, input().split())
xrh = [tuple(map(int, input().split())) for _ in range(n)]

ac = [0]
for x in range(1, 10**4 + 1):
    total = 0
    for L, r, h in xrh:
        R = L + h
        if not (L <= x - 1 and x <= R):
            continue

        v = r * r * pi * h / 3
        base = v * f(R - x + 1) / f(h)
        mul = v * f(R - x) / f(h)
        total += base - mul

    ac.append(ac[-1] + total)

for _ in range(q):
    a, b = map(int, input().split())
    print(ac[b] - ac[a])