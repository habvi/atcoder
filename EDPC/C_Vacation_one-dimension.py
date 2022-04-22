n = int(input())

dp = [0] * 3
for _ in range(n):
    a, b, c = map(int, input().split())

    ndp = [0] * 3
    for pre, num in enumerate((a, b, c)):
        for nxt in range(3):
            if pre == nxt:
                continue
            ndp[nxt] = max(ndp[nxt], dp[pre] + num)
    dp = ndp

print(max(dp))