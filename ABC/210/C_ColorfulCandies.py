from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A[:K])
ans = len(c)
for i, a in enumerate(A[K:], K):
    c[a] += 1
    rm = A[i - K]
    c[rm] -= 1
    if c[rm] == 0:
        del c[rm]
    ans = max(ans, len(c))
print(ans)
