N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

INF = float("inf")
ans = INF
for left in range(K + 1):
    right = N - K + left - 1
    ans = min(ans, A[right] - A[left])
print(ans)
