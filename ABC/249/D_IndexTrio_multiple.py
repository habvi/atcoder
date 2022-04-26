from collections import Counter

n = int(input())
A = list(map(int, input().split()))

c = Counter(A)

mx = max(A)
ans = 0
for k, v in c.items():
    for i in range(k, mx + 1, k):
        ans += v * c[i] * c[i // k]
print(ans)