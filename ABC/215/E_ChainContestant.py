def ctoi(c):
    return ord(c) - ord('A')


N = int(input())
S = input()
MOD = 998244353
m = 10

dp = [[0] * (1 << m) for _ in range(m)]
for c in S:
    ci = ctoi(c)
    for pre in reversed(range(1 << m)):
        for last in range(m):
            if ci == last:
                dp[last][pre] += dp[last][pre]
                dp[last][pre] %= MOD
            else:
                if pre >> ci & 1:
                    continue
                nxt = pre | 1 << ci
                dp[ci][nxt] += dp[last][pre]
                dp[ci][nxt] %= MOD
    dp[ci][1 << ci] += 1
ans = 0
for d in dp:
    ans += sum(d)
    ans %= MOD
print(ans)