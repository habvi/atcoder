n, l = map(int, input().split())
X = list(map(int, input().split()))
t1, t2, t3 = map(int, input().split())

dp = [float('inf') for _ in range(l+6)]
dp[0] = 0

tf = [False for _ in range(l+6)]
for x in X:
    tf[x] = True

for i in range(l):
    if tf[i+1]:
        dp[i+1] = min(dp[i+1], dp[i] + t1 + t3)
    else:
        dp[i+1] = min(dp[i+1], dp[i] + t1)

    if tf[i+2]:
        dp[i+2] = min(dp[i+2], dp[i] + t1 + t2 + t3)
    else:
        dp[i+2] = min(dp[i+2], dp[i] + t1 + t2)

    if tf[i+4]:
        dp[i+4] = min(dp[i+4], dp[i] + t1 + t2*3 + t3)
    else:
        dp[i+4] = min(dp[i+4], dp[i] + t1 + t2*3)           

for i in range(1, min(l+1, 4)):
    dp[l] = min(dp[l], dp[l-i] + t1*0.5 + t2*(i-0.5))

print(int(dp[l]))