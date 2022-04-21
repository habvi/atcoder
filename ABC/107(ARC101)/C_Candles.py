n, K = map(int, input().split())
A = list(map(int, input().split()))

ans = float('inf')
for i in range(n - K + 1):
    l = A[i]
    r = A[i + K - 1]

    mn = min(abs(l), abs(r))
    mx = max(abs(l), abs(r))
    if l * r >= 0:
        ans = min(ans, mx)
    else:
        ans = min(ans, mn * 2 + mx)
print(ans)