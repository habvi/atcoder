from collections import Counter

def comb(x):
    return x * (x - 1) // 2


N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
total = 0
for v in c.values():
    if v >= 2:
        total += comb(v)

for a in A:
    print(total - comb(c[a]) + comb(c[a] - 1))
