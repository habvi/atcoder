S = input()
K = int(input())
n = len(S)

dp = [[[0] * 2 for _ in range(K + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1

for i in range(n):
    for j in range(K + 1):
        for k in range(2):
            now = int(S[i])
            for nxt in range(10):
                ni = i + 1
                nj = j
                nk = k
                if nxt != 0:
                    nj += 1
                if nj > K:
                    continue
                if k == 0:
                    if now < nxt:
                        continue
                    if now > nxt:
                        nk = 1
                dp[ni][nj][nk] += dp[i][j][k]

print(sum(dp[n][K]))