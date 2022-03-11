n = int(input())
S = input()

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        if S[i] == S[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1

ans = 0
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        ans = max(ans, min(j - i, dp[i][j]))
print(ans)



# from behind
# dp = [[0] * (n + 1) for _ in range(n + 1)]

# for i in reversed(range(n)):
#     for j in reversed(range(n)):
#         if S[i] == S[j]:
#             dp[i][j] = dp[i + 1][j + 1] + 1

# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         ans = max(ans, min(j - i, dp[i][j]))
# print(ans)