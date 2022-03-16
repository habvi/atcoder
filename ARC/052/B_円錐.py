from math import pi

def f(x):
    return x ** 3


n, q = map(int, input().split())
xrh = [tuple(map(int, input().split())) for _ in range(n)]

for _ in range(q):
    a, b = map(int, input().split())

    ans = 0
    for X, R, H in xrh:
        l, r = X, X + H

        if r <= a or b <= l:
            continue

        v = pi * R * R * H / 3

        if a <= l and r <= b:
            total = v
        elif l < a and a < r <= b:
            total = v * f(r - a) / f(H)
        elif a <= l < b and b < r:
            mul = v * f(r - b) / f(H)
            total = v - mul
        else:
            total = v * f(r - a) / f(H)
            mul = v * f(r - b) / f(H)
            total -= mul
        ans += total

    print(ans)