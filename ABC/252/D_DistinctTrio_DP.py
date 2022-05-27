from collections import Counter

n = int(input())
A = list(map(int, input().split()))

dp = [0] * 4
dp[0] = 1

c = Counter(A)
for a, v in c.items():
    ndp = [0] * 4
    for pre in range(4):
        ndp[pre] += dp[pre]
        if pre < 3:
            ndp[pre + 1] += dp[pre] * v
    dp = ndp
print(dp[3])