def stoi(s):
    return ord(s) - ord('A')


n = int(input())
S = input()
MOD = 998244353
m = 10

ndp = [[0] * m for _ in range(1 << m)]
for s in S:
    si = stoi(s)
    dp = [l[:] for l in ndp]
    ndp[1 << si][si] += 1

    for pre in range(1 << m):
        for last in range(m):
            if si == last:
                ndp[pre][last] += dp[pre][last]
                ndp[pre][last] %= MOD
            else:
                if not pre >> si & 1:
                    ndp[pre | 1 << si][si] += dp[pre][last]
                    ndp[pre | 1 << si][si] %= MOD

ans = 0
for l in ndp:
    ans += sum(l)
    ans %= MOD
print(ans)