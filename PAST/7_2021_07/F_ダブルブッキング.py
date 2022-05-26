from itertools import accumulate

n = int(input())

imos = [0] * (10**5 * 24 + 1)
for _ in range(n):
    d, s, t = map(int, input().split())
    d -= 1
    l = 24 * d + s
    r = 24 * d + t
    imos[l] += 1
    imos[r] -= 1

ac = list(accumulate(imos))
print('Yes' if any(a >= 2 for a in ac) else 'No')