from collections import defaultdict

N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

price = defaultdict(int)
for d, p in zip(D, P[1:]):
    price[d] = p

total = 0
for c in C:
    if not price[c]:
        total += P[0]
    else:
        total += price[c]
print(total)