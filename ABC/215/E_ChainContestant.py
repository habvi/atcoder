def stoi(s):
    return ord(s) - ord('A')


n = int(input())
S = input()
MOD = 998244353
m = 10

dp = [[0] * (1 << m) for _ in range(m)]
for s in S:
    si = stoi(s)
    ndp = [[0] * (1 << m) for _ in range(m)]
    ndp[si][1 << si] += 1

    for pre in range(1 << m):
        for last in range(m):
            if si == last:
                ndp[last][pre] += dp[last][pre] * 2
                ndp[last][pre] %= MOD
            else:
                ndp[last][pre] += dp[last][pre]
                ndp[last][pre] %= MOD

                if not pre >> si & 1:
                    ndp[si][pre | 1 << si] += dp[last][pre]
                    ndp[si][pre | 1 << si] %= MOD
    dp = [l[:] for l in ndp]

ans = 0
for l in dp:
    ans += sum(l)
    ans %= MOD
print(ans)