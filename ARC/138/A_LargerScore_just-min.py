n, K = map(int, input().split())
A = list(map(int, input().split()))

num = []
for i, a in enumerate(A):
    if i < K:
        num.append((a, 0, i))
    else:
        num.append((a, 1, i))

num.sort(key=lambda x: (-x[0], x[1]))

INF = float('inf')
mn = INF
ans = INF
for x, k, i in num:
    if k:
        mn = min(mn, i)
    else:
        ans = min(ans, mn - i)

print(ans if ans != INF else -1)