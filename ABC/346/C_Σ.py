def sigma(n):
    return n*(n + 1) // 2


N, K = map(int, input().split())
A = set(map(int, input().split()))

total = sigma(K)
for a in A:
    if a <= K:
        total -= a
print(total)
