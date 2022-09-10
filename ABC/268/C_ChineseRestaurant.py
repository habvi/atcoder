from collections import Counter

N = int(input())
P = list(map(int, input().split()))

ct = Counter()
for i, p in enumerate(P):
    a = (p - 1 - i) % N
    b = (p - i) % N
    c = (p + 1 - i) % N
    ct[a] += 1
    ct[b] += 1
    ct[c] += 1
print(ct.most_common()[0][1])
