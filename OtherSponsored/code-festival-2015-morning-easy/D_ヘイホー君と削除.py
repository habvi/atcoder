def lcs(S, T):
    len_s, len_t = len(S), len(T)
    dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]

    for i, s in enumerate(S):
        for j, t in enumerate(T):
            if s == t:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])

    return dp[len_s][len_t]


n = int(input())
S = input()

ans = float('inf')
for i in range(n + 1):
    common = lcs(S[:i], S[i:])
    ans = min(ans, n - common * 2)
print(ans)