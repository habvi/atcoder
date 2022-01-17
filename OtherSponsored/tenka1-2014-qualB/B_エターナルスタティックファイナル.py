n = int(input())
s = input()
ls = len(s)
T = [input() for _ in range(n)]
MOD = 10**9 + 7

dp = [0] * (ls + 1)
dp[0] = 1
for i in range(ls + 1):
    for t in T:
        if len(t) <= i:
            if s[i-len(t) : i] == t:
                dp[i] += dp[i - len(t)]
                dp[i] %= MOD
print(dp[-1])