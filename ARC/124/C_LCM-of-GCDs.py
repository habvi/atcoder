from math import gcd

def div_lis(x):
    div_l, div_r = [], []
    i = 1
    while i * i <= x:
        if x % i == 0:
            div_l.append(i)
            if i != x // i:
                div_r.append(x // i)
        i += 1
    div = div_l + div_r[::-1]
    return div


def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))
    if i == 0:
        X = div_lis(a)
        Y = div_lis(b)

ans = 0
for x in X:
    for y in Y:
        for a, b in ab:
            if not a % x and not b % y:
                continue
            elif not b % x and not a % y:
                continue
            else:
                break
        else:
            ans = max(ans, lcm(x, y))
print(ans)