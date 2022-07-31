N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

ans = 0
for num in range(1, N + 1):
    dp = [[0] * num for _ in range(num + 1)]
    dp[0][0] = 1
    for a in A:
        for i in reversed(range(num)):
            for mod in range(num):
                nxt = (mod + a) % num
                dp[i + 1][nxt] += dp[i][mod]
                dp[i + 1][nxt] %= MOD
    ans += dp[-1][0]
    ans %= MOD
print(ans)