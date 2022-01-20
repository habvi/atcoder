s = input()
t = input()
ls = len(s)
lt = len(t)

dp = [[0] * (lt + 1) for _ in range(ls + 1)]
for i in range(ls + 1):
    for j in range(lt + 1):
        if i < ls and j < lt:
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        if i < ls:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j < lt:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])

ans = []
i, j = ls, lt
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ans.append(s[i - 1])
        i -= 1
        j -= 1
print(''.join(ans[::-1]))