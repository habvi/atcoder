from collections import Counter

n, K = map(int, input().split())
S = [input() for _ in range(n)]

ans = 0
for bit in range(1 << n):
    c = Counter()
    for i in range(n):
        if bit >> i & 1:
            c += Counter(S[i])

    total = 0
    for v in c.values():
        if v == K:
            total += 1
    ans = max(ans, total)
print(ans)