K = input()
D = int(input())
MOD = 10**9 + 7

n = len(K)
dp = [[0] * 2 for _ in range(D)]
dp[0][0] = 1

for c in K:
    ndp = [[0] * 2 for _ in range(D)]
    num = int(c)
    for now in range(D):
        for is_less in range(2):
            for nxt in range(10):
                ni = (now + nxt) % D
                nj = is_less
                if is_less == 0:
                    if num < nxt:
                        continue
                    if num > nxt:
                        nj = 1
                ndp[ni][nj] += dp[now][is_less]
                ndp[ni][nj] %= MOD
    dp = [l[:] for l in ndp]

print((sum(dp[0]) - 1) % MOD)