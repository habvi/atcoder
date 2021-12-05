n = int(input())
t = list(map(int, input().split()))
mx = n * 1000 + 1
dp = [0] * mx
dp[0] = 1
for i in range(n):
    for j in range(mx - 1, -1, -1):
        if j + t[i] < mx:
            dp[j + t[i]] = dp[j + t[i]] | dp[j]

tot = sum(t)
ans = float('inf')
for i in range(mx):
    if dp[i]:
        ans = min(ans, max(i, tot - i))
print(ans)