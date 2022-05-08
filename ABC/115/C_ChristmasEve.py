n, K = map(int, input().split())
h = [int(input()) for _ in range(n)]

h.sort()
ans = float('inf')
for i in range(n - K + 1):
    ans = min(ans, h[i + K - 1] - h[i])
print(ans)