n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

dp = A[0]

for i in range(1, n):
    ndp = [0] * 3
    for pre in range(3):
        for now in range(3):
            if pre == now:
                continue
            ndp[now] = max(ndp[now], dp[pre] + A[i][now])
    dp = ndp

print(max(dp))