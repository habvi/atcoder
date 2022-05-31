score = [25, 39, 51, 76, 163, 111, 136, 128, 133, 138]
n = len(score)

total = sum(score)
score[6] = 58
dp = [0] * (total + 1)
dp[0] = 1

for p in score:
    for i in reversed(range(total + 1)):
        if dp[i] and i + p <= total:
            if p == 58:
                dp[i + p] |= 2
            else:
                dp[i + p] |= dp[i]

res = 136 - 58
for i in reversed(range(total + 1)):
    if i + res <= total and dp[i] >= 2:
        dp[i + res] = 1

for i, ans in enumerate(dp):
    if ans:
        print(i)