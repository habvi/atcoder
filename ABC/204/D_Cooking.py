n = int(input())
T = list(map(int, input().split()))

total = sum(T)
dp = [0] * (total + 1)
dp[0] = 1

for t in T:
    for i in reversed(range(total + 1)):
        if i + t <= total:
            dp[i + t] |= dp[i]

ans = float('inf')
for i, b in enumerate(dp):
    if b:
        ans = min(ans, max(i, total - i))
print(ans)